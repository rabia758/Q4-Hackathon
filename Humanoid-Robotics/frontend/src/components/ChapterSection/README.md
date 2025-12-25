# ChapterSection Component

A reusable React component that displays chapter content in expandable sections for Concepts, Examples, and Summary.

## Features

- Expandable/collapsible sections with smooth animations
- Content organized under Concepts, Examples, and Summary categories
- Smooth open/close animations (under 300ms)
- Accessible with proper ARIA attributes and keyboard navigation
- Mobile-responsive design
- Reusable and customizable

## Props

| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| id | string | Yes | - | Unique identifier for the section |
| title | string | Yes | - | Title displayed in the expandable header |
| concepts | string \| ReactNode | Yes | - | Content for the Concepts section |
| examples | string \| ReactNode | Yes | - | Content for the Examples section |
| summary | string \| ReactNode | Yes | - | Content for the Summary section |
| defaultExpanded | boolean | No | false | Whether the section is initially expanded |
| onToggle | (expanded: boolean) => void | No | - | Callback for when section expansion state changes |
| className | string | No | '' | Additional CSS class name |

## Usage

```jsx
import ChapterSection from '@site/src/components/ChapterSection';

<ChapterSection
  id="introduction"
  title="Chapter 1: Introduction to Robotics"
  concepts="This section covers the fundamental concepts of robotics..."
  examples="Here are some practical examples of robotics applications..."
  summary="In summary, robotics combines mechanical, electrical, and software engineering..."
/>
```

## Accessibility

- Keyboard navigable (Tab key)
- Space or Enter keys toggle expansion state
- Proper ARIA attributes for screen readers
- Focus management with visible focus indicators
- Touch-friendly targets (minimum 44px)

## Styling

The component uses CSS modules for styling and integrates with the Docusaurus theme using Infima CSS variables. You can add custom styles using the `className` prop.

The component uses the following Docusaurus theme variables:
- `--ifm-color-primary`: For the category titles and toggle icon
- `--ifm-color-emphasis-*`: For borders and backgrounds
- `--ifm-font-color-base`: For text content
- `--ifm-background-surface-color`: For the component background

## Performance

- Section expansion/collapse completes in under 300ms
- 60fps smooth transitions maintained
- Efficient rendering with React hooks