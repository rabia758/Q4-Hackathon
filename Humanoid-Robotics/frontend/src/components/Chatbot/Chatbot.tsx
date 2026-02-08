import React, { useState, useEffect, useRef } from 'react';
import './Chatbot.css';

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
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

  // Function to handle chapter context events
  useEffect(() => {
    const handleOpenChatbotForChapter = (event) => {
      setIsOpen(true);
      setInputValue(`I have a question about the chapter "${event.detail.chapterTitle}"`);
    };

    window.addEventListener('openChatbotForChapter', handleOpenChatbotForChapter);

    return () => {
      window.removeEventListener('openChatbotForChapter', handleOpenChatbotForChapter);
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

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="chatbot">
      {/* Chatbot widget button */}
      <button className="chatbot-button" onClick={toggleChat}>
        <span>🤖</span>
      </button>

      {/* Chatbot popup */}
      {isOpen && (
        <div className="chatbot-popup">
          <div className="chatbot-header">
            <h3>Textbook Assistant</h3>
            <button className="chatbot-close" onClick={toggleChat}>
              ×
            </button>
          </div>

          <div className="chatbot-messages">
            {messages.length === 0 ? (
              <div className="chatbot-welcome">
                <p>Hello! I'm your Humanoid Robotics textbook assistant.</p>
                <p>
                  {selectedText
                    ? "I'm in selected text mode. I'll answer only from the highlighted text."
                    : "Ask me anything about the textbook content!"}
                </p>
                {selectedText && (
                  <p className="selected-text-preview">
                    Selected: "{selectedText.substring(0, 50)}..."
                  </p>
                )}
              </div>
            ) : (
              messages.map((message) => (
                <div
                  key={message.id}
                  className={`chatbot-message ${message.sender}`}
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
              <div className="chatbot-message bot">
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

          <div className="chatbot-input-area">
            {selectedText && (
              <div className="selected-text-indicator">
                Using selected text: "{selectedText.substring(0, 30)}..."
                <button
                  className="clear-selection"
                  onClick={() => setSelectedText('')}
                >
                  Clear
                </button>
              </div>
            )}
            <div className="chatbot-input-container">
              <textarea
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder={selectedText
                  ? "Ask about the selected text..."
                  : "Ask about the textbook..."}
                className="chatbot-input"
                rows="1"
              />
              <button
                onClick={sendMessage}
                disabled={!inputValue.trim() || isLoading}
                className="chatbot-send-button"
              >
                Send
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chatbot;