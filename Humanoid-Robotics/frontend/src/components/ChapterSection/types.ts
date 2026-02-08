/**
 * TypeScript interfaces for the ChapterSection component
 */

export interface ChapterSectionProps {
  /**
   * Unique identifier for the section
   */
  id: string;

  /**
   * Title displayed in the expandable header
   */
  title: string;

  /**
   * Content for the Concepts section
   */
  concepts: string | React.ReactNode;

  /**
   * Content for the Examples section
   */
  examples: string | React.ReactNode;

  /**
   * Content for the Summary section
   */
  summary: string | React.ReactNode;

  /**
   * Whether the section is initially expanded
   * @default false
   */
  defaultExpanded?: boolean;

  /**
   * Callback for when section expansion state changes
   */
  onToggle?: (expanded: boolean) => void;

  /**
   * Additional CSS class name
   */
  className?: string;
}

export interface SectionContent {
  /**
   * The content to be displayed in the section
   */
  content: string | React.ReactNode;

  /**
   * Whether this section is currently expanded
   */
  expanded: boolean;

  /**
   * Callback to toggle expansion state
   */
  onToggle: () => void;
}