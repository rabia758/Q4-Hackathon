---
sidebar_position: 1
---

# Chapter UI Example

This page demonstrates the Chapter UI with expandable sections.

import ChapterSection from '@site/src/components/ChapterSection';

## Example Chapter

<ChapterSection
  id="example-chapter"
  title="Introduction to Robotics"
  concepts="Robotics is an interdisciplinary branch of engineering and science that includes mechanical engineering, electrical engineering, computer science, and others. It deals with the design, construction, operation, and application of robots, as well as computer systems for their control, sensory feedback, and information processing."
  examples={<>
    <p>Industrial robots used in manufacturing lines for welding, painting, and assembly.</p>
    <p>Service robots like vacuum cleaners and lawn mowers that assist in daily tasks.</p>
    <p>Medical robots used in surgeries for precision and minimal invasiveness.</p>
  </>}
  summary="Robotics combines multiple engineering disciplines to create machines that can assist humans. These machines range from industrial applications to personal assistants, with the field constantly evolving with advances in AI and machine learning."
/>

<ChapterSection
  id="advanced-robotics"
  title="Advanced Robotics Concepts"
  concepts="Advanced robotics involves complex systems that integrate artificial intelligence, machine learning, computer vision, and sophisticated control systems. These robots can adapt to their environment, learn from experience, and make autonomous decisions."
  examples={<>
    <p>Autonomous vehicles that navigate complex traffic scenarios using sensors and AI.</p>
    <p>Swarm robotics where multiple robots coordinate to achieve a common goal.</p>
    <p>Cognitive robots that can understand and respond to human emotions.</p>
  </>}
  summary="Advanced robotics pushes the boundaries of what machines can do by incorporating AI and learning capabilities. These systems represent the future of human-robot interaction and autonomous operations."
/>