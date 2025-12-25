import React, { useState, useEffect, useRef } from 'react';
import Layout from '@theme/Layout';
import './chat.css'; // Import the CSS file

const ChatPage = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState('');
  const messagesEndRef = useRef(null);

  // Function to scroll to bottom of messages
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Function to handle text selection
  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection();
      if (selection.toString().trim() !== '') {
        setSelectedText(selection.toString().trim());
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    // Add user message
    const userMessage = {
      id: Date.now(),
      text: inputValue,
      sender: 'user',
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Determine if we're in selected text mode
      const requestBody = {
        query: inputValue,
        selected_text: selectedText || null,
        history: messages.map(msg => ({
          role: msg.sender,
          content: msg.text
        }))
      };

      const endpoint = selectedText ? 'http://localhost:8000/chat/selected' : 'http://localhost:8000/chat';

      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      const data = await response.json();

      if (response.ok) {
        const botMessage = {
          id: Date.now() + 1,
          text: data.response,
          sender: 'bot',
          citations: data.citations || [],
          timestamp: new Date()
        };

        setMessages(prev => [...prev, botMessage]);
      } else {
        const errorMessage = {
          id: Date.now() + 1,
          text: 'Sorry, I encountered an error. Please try again.',
          sender: 'bot',
          timestamp: new Date()
        };
        setMessages(prev => [...prev, errorMessage]);
      }
    } catch (error) {
      const errorMessage = {
        id: Date.now() + 1,
        text: 'Sorry, I encountered an error. Please try again.',
        sender: 'bot',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const clearChat = () => {
    setMessages([]);
    setSelectedText('');
  };

  return (
    <Layout title="AI Chat" description="Humanoid Robotics Textbook Assistant">
      <div className="chat-container">
        <div className="chat-header">
          <div className="header-content">
            <h1>🤖 Humanoid Robotics Assistant</h1>
            <p>Ask me anything about the textbook content!</p>
          </div>
          <div className="header-actions">
            {selectedText && (
              <div className="selected-text-indicator">
                <span>Using selected text: "{selectedText.substring(0, 50)}{selectedText.length > 50 ? '...' : ''}"</span>
                <button onClick={() => setSelectedText('')} className="clear-selection-btn">
                  Clear
                </button>
              </div>
            )}
            {messages.length > 0 && (
              <button onClick={clearChat} className="clear-chat-btn">
                Clear Chat
              </button>
            )}
          </div>
        </div>

        <div className="chat-messages">
          {messages.length === 0 ? (
            <div className="welcome-message">
              <div className="welcome-content">
                <h2>Hello! I'm your Humanoid Robotics textbook assistant.</h2>
                <p>Ask me anything about the textbook content and I'll provide answers based on the material.</p>
                <div className="suggestions">
                  <div className="suggestion-item" onClick={() => setInputValue("What is humanoid robotics?")}>
                    What is humanoid robotics?
                  </div>
                  <div className="suggestion-item" onClick={() => setInputValue("Explain bipedal locomotion")}>
                    Explain bipedal locomotion
                  </div>
                  <div className="suggestion-item" onClick={() => setInputValue("How do robots maintain balance?")}>
                    How do robots maintain balance?
                  </div>
                  <div className="suggestion-item" onClick={() => setInputValue("What are the key challenges in humanoid robotics?")}>
                    What are the key challenges?
                  </div>
                </div>
              </div>
            </div>
          ) : (
            messages.map((message) => (
              <div
                key={message.id}
                className={`message ${message.sender}`}
              >
                <div className="message-content">
                  {message.text}
                </div>
                {message.citations && message.citations.length > 0 && (
                  <div className="citations">
                    <details>
                      <summary>Citations</summary>
                      <ul>
                        {message.citations.map((citation, idx) => (
                          <li key={idx}>
                            <strong>{citation.chapter} - {citation.section}</strong>
                            <p>{citation.content.substring(0, 100)}...</p>
                          </li>
                        ))}
                      </ul>
                    </details>
                  </div>
                )}
                <div className="message-timestamp">
                  {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </div>
              </div>
            ))
          )}
          {isLoading && (
            <div className="message bot">
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="chat-input-area">
          <div className="chat-input-container">
            <textarea
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder={selectedText
                ? "Ask about the selected text..."
                : "Ask about the textbook..."}
              className="chat-input"
              rows="1"
            />
            <button
              onClick={sendMessage}
              disabled={!inputValue.trim() || isLoading}
              className="chat-send-button"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M22 2L11 13" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M22 2L15 22L11 13L2 9L22 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ChatPage;