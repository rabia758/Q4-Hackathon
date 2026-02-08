import React from 'react';
import './ChapterActions.module.css';

interface ChapterActionsProps {
  chapterTitle?: string;
  chapterId?: string;
}

const ChapterActions: React.FC<ChapterActionsProps> = ({
  chapterTitle = 'Current Chapter',
  chapterId = 'current'
}) => {
  const handleAskAI = () => {
    // Trigger the chatbot with a context about the current chapter
    const event = new CustomEvent('openChatbotWithChapterContext', {
      detail: { chapterTitle, chapterId }
    });
    window.dispatchEvent(event);
  };

  const handlePersonalize = () => {
    alert('Personalization feature coming soon!');
  };

  const handleTranslateUrdu = () => {
    alert('Urdu translation feature coming soon!');
  };

  return (
    <div className="chapter-actions">
      <div className="action-buttons">
        <button
          className="action-button ai-button"
          onClick={handleAskAI}
          title="Ask AI about this chapter"
        >
          <span className="button-icon">🤖</span>
          <span className="button-text">Ask AI</span>
        </button>

        <button
          className="action-button personalize-button"
          onClick={handlePersonalize}
          title="Personalize content"
        >
          <span className="button-icon">👤</span>
          <span className="button-text">Personalize</span>
        </button>

        <button
          className="action-button translate-button"
          onClick={handleTranslateUrdu}
          title="Translate to Urdu"
        >
          <span className="button-icon">🇵🇰</span>
          <span className="button-text">Urdu</span>
        </button>
      </div>
    </div>
  );
};

export default ChapterActions;