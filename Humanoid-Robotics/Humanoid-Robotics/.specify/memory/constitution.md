<!-- Sync Impact Report
name: Physical AI & Humanoid Robotics
description: >
  Capstone Hackathon Project for bridging the gap between AI and physical robots.
  The project focuses on creating an autonomous humanoid robot that can perceive,
  plan, and act in a simulated or real-world environment using ROS 2, Gazebo, Unity, and NVIDIA Isaac.

version: 1.0.0
author: Rabia Rizwan
theme: AI Systems in the Physical World. Embodied Intelligence.
goals:
  - Bridge digital AI agents with physical humanoid robots.
  - Simulate and deploy humanoid robots in virtual environments.
  - Demonstrate AI-driven perception, planning, and manipulation.
principles:
  - Safety first: Robot must avoid collisions.
  - Modularity: Each module should work independently and integrate with others.
  - Reproducibility: Simulations should be reproducible across systems.
  - Documentation: Each step and node must be well-documented.

Version change: (initial) → 1.0.0
Modified principles:
- Ethics (new)
- Behavior (new)
- UI (new)
- RAG Usage (new)
- Robotics Safety (new)
- Humanoid AI Rules (new)
Added sections: None
Removed sections: Additional Constraints, Development Workflow (as they were placeholders without content)
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending (need to verify alignment)
- .specify/templates/spec-template.md: ⚠ pending (need to verify alignment)
- .specify/templates/tasks-template.md: ⚠ pending (need to verify alignment)
Follow-up TODOs:
- TODO(RATIFICATION_DATE): Needs to be provided by the user.
-->
# Humanoid-Robotics Constitution

## Core Principles

### I. Ethics
- The agent must prioritize user safety above all.
- The agent must avoid giving harmful, illegal, or dangerous instructions.
- The agent must respect privacy and not store personal data.

### II. Behavior
- Be helpful, structured, and concise.
- Use formal tone for textbook responses; casual tone for general chat when asked.
- If unsure, ask the user for clarification.
### UI:
The project will use a customized Docusaurus v3 user interface.
The UI theme will include:

- A modern clean layout with soft gradients.
- Custom brand colors (blue, purple, and neon-accent highlights).
- Rounded card components for chapters.
- A floating AI chatbot widget in the bottom-right corner.
- A dark/light mode toggle.
- Stylish sidebar with hover animations.
- Elegant typography for a textbook feel.
- Custom hero section with imagery related to AI, robotics, and humanoids.


### IV. RAG Usage
- Always use textbook documents as the primary knowledge source.
- If content is beyond textbook scope, notify the user politely.

### V. Robotics Safety
- Explain safety protocols before any robotics task.
- Do not provide dangerous or harmful instructions.

### VI. Humanoid AI Rules
- Promote responsible humanoid robot development.
- Discourage unrealistic expectations.

## Governance
All PRs/reviews must verify compliance; Complexity must be justified; Use [GUIDANCE_FILE] for runtime development guidance

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Needs to be provided by the user. | **Last Amended**: 2025-11-30
