import React, { useEffect } from 'react';
import Chatbot from '../Chatbot';

const Root = ({ children }) => {
  useEffect(() => {
    const handleOpenChatbotWithChapterContext = (event) => {
      // Dispatch a custom event that the Chatbot component can listen to
      window.dispatchEvent(new CustomEvent('openChatbotForChapter', {
        detail: event.detail
      }));
    };

    window.addEventListener('openChatbotWithChapterContext', handleOpenChatbotWithChapterContext);

    return () => {
      window.removeEventListener('openChatbotWithChapterContext', handleOpenChatbotWithChapterContext);
    };
  }, []);

  return (
    <>
      {children}
      <Chatbot />
    </>
  );
};

export default Root;