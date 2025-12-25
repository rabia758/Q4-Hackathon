---
description: "Tasks for Physical AI and Humanoid Robotics Course development"
---

# Tasks: Physical AI and Humanoid Robotics Course

**Input**: Design documents from `/specs/001-robotics-edu-system/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`

---

## Phase 1: Planning and Initial Setup

**Purpose**: Clarify unknowns and set up foundational elements.

- [x] T001 [P] [US1] Research suitable testing frameworks for Docusaurus/React frontend and Python backend.
- [x] T002 Create project directory structure for `backend/` and `frontend/` as per plan.md.

---

## Phase 2: Requirements Understanding and Book Structure Design

**Purpose**: Define the content and its organization.

### Tasks for User Story 1 - Learn Robotics Concepts (Priority: P1)

- [x] T003 [US1] Review user-provided course outline to understand content scope. (Confirmed from spec input)
- [x] T004 [US1] Identify required chapters, modules, diagrams, examples, and exercises. (Confirmed from spec input)
- [x] T005 [US1] Confirm target audience as beginners and intermediate learners. (Confirmed from spec input)
- [x] T006 [US1] Confirm UI requirements: Docusaurus v3, custom theme, RAG chatbot panel. (Confirmed from plan input)
- [x] T007 [US1] Create a detailed book outline with 12-15 chapters. (Outline in book-outline.md)
- [x] T008 [US1] Define chapter naming conventions, subtopics, and learning objectives. (Defined in book-outline.md)
- [x] T009 [US1] Create Docusaurus folder and file structure within `frontend/docs/`.
- [x] T010 [US1] Prepare placeholders for glossary, index, and summary pages within `frontend/docs/`.

---

## Phase 3: Content Generation (Book Chapters)

**Purpose**: Populate the textbook with detailed content.

### Tasks for User Story 1 - Learn Robotics Concepts (Priority: P1)

- [x] T011 [P] [US1] Write Chapter 1 as an .mdx file in `frontend/docs/chapter-01-introduction-to-physical-ai-robotics/index.mdx`.
- [x] T012 [P] [US1] Write Chapter 2 as an .mdx file in `frontend/docs/chapter-02-mathematics-for-robotics/index.mdx`.
- [x] T013 [P] [US1] Write Chapter 3 as an .mdx file in `frontend/docs/chapter-03-robot-kinematics/index.mdx`.
- [x] T014 [P] [US1] Write Chapter 4 as an .mdx file in `frontend/docs/chapter-04-robot-dynamics/index.mdx`.
- [x] T015 [P] [US1] Write Chapter 5 as an .mdx file in `frontend/docs/chapter-05-sensors-for-humanoid-robotics/index.mdx`.
- [x] T016 [P] [US1] Write Chapter 6 as an .mdx file in `frontend/docs/chapter-06-actuators-and-mechatronics/index.mdx`.
- [x] T017 [P] [US1] Write Chapter 7 as an .mdx file in `frontend/docs/chapter-07-control-systems-for-robotics/index.mdx`.
- [x] T018 [P] [US1] Write Chapter 8 as an .mdx file in `frontend/docs/chapter-08-locomotion-and-balance/index.mdx`.
- [x] T019 [P] [US1] Write Chapter 9 as an .mdx file in `frontend/docs/chapter-09-perception-and-computer-vision/index.mdx`.
- [x] T020 [P] [US1] Write Chapter 10 as an .mdx file in `frontend/docs/chapter-10-robot-manipulation-and-grasping/index.mdx`.
- [x] T021 [P] [US1] Write Chapter 11 as an .mdx file in `frontend/docs/chapter-11-introduction-to-ros2/index.mdx`.
- [x] T022 [P] [US1] Write Chapter 12 as an .mdx file in `frontend/docs/chapter-12-ai-models-for-robotics/index.mdx`.
- [ ] T023 [US1] Integrate diagrams (Mermaid), tables, and formulas into relevant chapters.
- [x] T024 [US1] Add programming examples to relevant chapters.
- [ ] T025 [US1] Incorporate case studies on intelligent agents, humanoid robots, mechatronics, sensors, actuators, control systems, and AI models into chapters.
- [ ] T026 [US1] Add hands-on labs using Python + ROS2 (text-only instructions) to relevant chapters.

---

## Phase 4: RAG Knowledge Base Preparation

**Purpose**: Prepare the course content for AI retrieval.

### Tasks for User Story 2 - Ask AI for Clarification (Priority: P1) & User Story 3 - Access RAG-Enhanced Information (Priority: P2)

- [ ] T027 [P] [US2, US3] Chunk all generated chapters and supporting documents into vector-friendly text.
- [ ] T028 [US2, US3] Create a Qdrant collection for storing document embeddings.
- [ ] T029 [US2, US3] Initialize the OpenAI / ChatGPT Agent for retrieval and response generation in `backend/src/ai_service/`.
- [ ] T030 [P] [US2, US3] Prepare metadata (chapter number, heading, tags) for each chunked document.
- [ ] T031 [US2, US3] Populate the Qdrant collection with chunked text and metadata.

---

## Phase 5: Docusaurus Website Setup

**Purpose**: Deploy the textbook and integrate the RAG chatbot.

### Tasks for User Story 1 - Learn Robotics Concepts (Priority: P1), User Story 2 - Ask AI for Clarification (Priority: P1)

- [ ] T032 [US1] Create a new Docusaurus deployment with the custom theme in `frontend/`.
- [ ] T033 [US2] Deploy the backend RAG/AI services to a cloud platform (e.g., Render/Railway).
- [ ] T034 [US2] Connect the frontend chatbot UI (in `frontend/src/components/` or `frontend/src/pages/`) to the backend API.

---

## Phase 6: Delivery & Documentation

**Purpose**: Finalize project output and provide operational guidance.

- [ ] T035 Provide the final project folder structure in a `README.md` or similar file.
- [ ] T036 Document install and run instructions for both frontend and backend components.
- [ ] T037 Add a maintenance guide for future content updates and system enhancements.
