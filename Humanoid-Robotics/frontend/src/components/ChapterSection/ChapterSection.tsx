import React, { useState, useEffect } from 'react';
import { ChapterSectionProps } from './types';
import styles from './ChapterSection.module.css';
import ChapterActions from '../ChapterActions';

const ChapterSection: React.FC<ChapterSectionProps> = ({
  id,
  title,
  concepts,
  examples,
  summary,
  defaultExpanded = false,
  onToggle,
  className = ''
}) => {
  const [isExpanded, setIsExpanded] = useState(defaultExpanded);

  useEffect(() => {
    setIsExpanded(defaultExpanded);
  }, [defaultExpanded]);

  const handleToggle = () => {
    const newExpandedState = !isExpanded;
    setIsExpanded(newExpandedState);
    onToggle?.(newExpandedState);
  };

  const sectionClasses = `${styles.chapterSection} ${isExpanded ? styles['chapterSection--expanded'] : ''} ${className}`;
  const contentClasses = `${styles.content} ${isExpanded ? styles['content--expanded'] : ''}`;
  const toggleIconClasses = `${styles.toggleIcon} ${isExpanded ? styles['toggleIcon--rotated'] : ''}`;

  return (
    <section className={sectionClasses} aria-labelledby={`chapter-section-title-${id}`}>
      <header
        className={styles.header}
        role="button"
        tabIndex={0}
        aria-expanded={isExpanded}
        aria-controls={`chapter-section-content-${id}`}
        onClick={handleToggle}
        onKeyDown={(e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            handleToggle();
          }
        }}
      >
        <h3 id={`chapter-section-title-${id}`} className={styles.title}>
          {title}
        </h3>
        <span
          className={toggleIconClasses}
          aria-hidden="true"
        >
          <svg
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M4 6L8 10L12 6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </span>
      </header>
      <div
        id={`chapter-section-content-${id}`}
        className={contentClasses}
        role="region"
        aria-labelledby={`chapter-section-title-${id}`}
        aria-hidden={!isExpanded}
      >
        <div className={styles.categorySection}>
          <h4 className={styles.categoryTitle}>Concepts</h4>
          <div className={styles.categoryContent}>{concepts}</div>
        </div>
        <div className={styles.categorySection}>
          <h4 className={styles.categoryTitle}>Examples</h4>
          <div className={styles.categoryContent}>{examples}</div>
        </div>
        <div className={styles.categorySection}>
          <h4 className={styles.categoryTitle}>Summary</h4>
          <div className={styles.categoryContent}>{summary}</div>
        </div>
      </div>
      <div className={styles.chapterActions}>
        <ChapterActions chapterTitle={title} chapterId={id} />
      </div>
    </section>
  );
};

export default ChapterSection;