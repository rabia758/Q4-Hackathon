# Quickstart: Chapter UI with Expandable Sections

## Installation

The ChapterSection component is built into the Docusaurus project and requires no additional installation.

## Basic Usage

```jsx
import ChapterSection from '@site/src/components/ChapterSection';

<ChapterSection
  id="introduction"
  title="Chapter 1: Introduction to Robotics"
  concepts={`This section covers the fundamental concepts of robotics...`}
  examples={`Here are some practical examples of robotics applications...`}
  summary={`In summary, robotics combines mechanical, electrical, and software engineering...`}
/>
```

## Advanced Usage

### Controlled Expansion
```jsx
function MyChapterPage() {
  const [expanded, setExpanded] = useState(false);

  return (
    <ChapterSection
      id="advanced-topics"
      title="Advanced Robotics Concepts"
      concepts="Complex robotics concepts..."
      examples="Advanced examples..."
      summary="Chapter summary..."
      defaultExpanded={expanded}
      onToggle={setExpanded}
    />
  );
}
```

### With Custom Styling
```jsx
<ChapterSection
  id="custom-style"
  title="Custom Styled Chapter"
  concepts="Concepts content..."
  examples="Examples content..."
  summary="Summary content..."
  className="custom-chapter-style"
/>
```

## Development Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. The ChapterSection component will be available at `src/components/ChapterSection/`

## Testing

### Unit Tests
```bash
npm test -- src/components/ChapterSection
```

### End-to-End Tests
```bash
npm run e2e
```

## Component Structure
```
src/components/ChapterSection/
├── ChapterSection.tsx          # Main component implementation
├── ChapterSection.module.css   # Component-specific styles
├── index.ts                    # Export file
└── types.ts                    # TypeScript type definitions
```