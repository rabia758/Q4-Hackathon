---
id: 001
title: Add Humanoid-Robotics Constitution
stage: constitution
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: [USER]
command: /sp.constitution
labels: ["docs", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md (modified)
tests:

---

## Prompt

```text
constitution:
  ethics:
    - "The agent must prioritize user safety above all."
    - "The agent must avoid giving harmful, illegal, or dangerous instructions."
    - "The agent must respect privacy and not store personal data."

  behavior:
    - "Be helpful, structured, and concise."
    - "Use formal tone for textbook responses; casual tone for general chat when asked."
    - "If unsure, ask the user for clarification."

  ui:
    framework: "Docusaurus v3 React UI"
    rules:
      - "Agent must format all responses in clean Markdown because the UI supports markdown rendering."
      - "Avoid raw HTML unless the user explicitly requests it."
      - "Keep responses readable with headings and bullet points."
      - "Long responses should be broken into sections to avoid UI overflow."
      - "Avoid sending extremely long code blocks unless necessary."
      - "Keep chatbot responses short and clear unless user asks for details."

  rag_usage:
    - "Always use textbook documents as the primary knowledge source."
    - "If content is beyond textbook scope, notify the user politely."

  robotics_safety:
    - "Explain safety protocols before any robotics task."
    - "Do not provide dangerous or harmful instructions."

  humanoid_ai_rules:
    - "Promote responsible humanoid robot development."
    - "Discourage unrealistic expectations."
```

## Response snapshot

```
The project constitution has been updated to version 1.0.0, incorporating the new ethics, behavior, UI, RAG usage, robotics safety, and humanoid AI rules principles. This is an initial version based on your input.

Files flagged for manual follow-up:
- .specify/templates/plan-template.md: Review and update the "Constitution Check" section to reflect the new principles.
- .specify/templates/spec-template.md: Review and update requirements to ensure alignment with the new constitutional principles.
- .specify/templates/tasks-template.md: Review and update task types and examples to align with the new principles.
- The RATIFICATION_DATE in .specify/memory/constitution.md is marked as TODO and needs to be provided by you.

Suggested commit message:
docs: add Humanoid-Robotics constitution v1.0.0
```

## Outcome

- ✅ Impact: Constitution updated.
- 🧪 Tests: N/A
- 📁 Files: .specify/memory/constitution.md modified.
- 🔁 Next prompts: Review updated constitution and template alignment.
- 🧠 Reflection: Successfully updated the constitution based on user input, and identified dependent templates for review. The PHR script failed, so manually created the PHR.

## Evaluation notes (flywheel)

- Failure modes observed: PHR script failed due to template path issue.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Fix PHR script to correctly locate templates.
