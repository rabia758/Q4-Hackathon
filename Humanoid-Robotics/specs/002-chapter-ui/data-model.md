# Data Model: Chapter UI with Expandable Sections

## Component Interface

### ChapterSection Props
```typescript
interface ChapterSectionProps {
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
```

### Section Content Structure
```typescript
interface SectionContent {
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
```

## State Management

### Internal Component State
- `expandedSections: Set<string>` - Tracks which sections are currently expanded
- `animationState: 'idle' | 'expanding' | 'collapsing'` - Tracks animation state for smooth transitions

## Accessibility Attributes

### ARIA Properties
- `aria-expanded`: Indicates whether the section is expanded or collapsed
- `aria-controls`: Points to the content that is controlled by the expandable header
- `role="button"`: Applied to the expandable header for keyboard navigation
- `tabIndex={0}`: Makes the header focusable for keyboard navigation

## CSS Classes

### Component Styling
- `chapter-section`: Main container class
- `chapter-section--expanded`: Applied when section is expanded
- `chapter-section__header`: Header area containing the title and toggle icon
- `chapter-section__content`: Content wrapper that expands/collapses
- `chapter-section__category`: Individual category sections (Concepts, Examples, Summary)