project:
  name: "Physical AI Humanoid Robotics"
  description: >
    A unified AI-authored book project built using Docusaurus, Claude Code,
    and Spec-Kit Plus. The book includes an embedded RAG chatbot,
    reusable intelligence via subagents and skills, authentication-based
    personalization, and Urdu translation.

  deliverables:
    - Docusaurus book deployed to GitHub Pages
    - Embedded RAG chatbot answering from book content
    - Selected-text-only question answering
    - Reusable intelligence via Claude subagents and skills
    - Personalized learning experience
    - Urdu translation support

principles:
  - spec_first_development
  - ai_assisted_authoring
  - modular_agents_and_skills
  - reusable_intelligence
  - cloud_native
  - privacy_by_design
  - progressive_enhancement

architecture:
  frontend:
    framework: "Docusaurus"
    deployment: "GitHub Pages"
    ui_reference: "Spec-Kit Frontend Hackathon UI"
    features:
      - left_sidebar_navigation
      - dropdown_chapter_groups
      - card_based_layout
      - dark_mode_default
      - chapter_action_buttons
      - floating_rag_chatbot

  backend:
    framework: "FastAPI"
    responsibilities:
      - rag_chat_api
      - selected_text_qa
      - user_personalization
      - translation_service
      - agent_skill_execution

  database:
    provider: "Neon Serverless Postgres"
    usage:
      - users
      - auth_sessions
      - personalization_profiles
      - chat_history

  vector_store:
    provider: "Qdrant Cloud Free Tier"
    usage:
      - book_embeddings
      - selected_text_embeddings
      - semantic_search

  ai_stack:
    authoring_llm: "Claude Code"
    runtime_llm: "OpenAI Agents / ChatKit"
    embeddings: "OpenAI Embeddings"
    orchestration: "Spec-Kit Plus"

ui_ux:
  reference_ui:
    name: "Spec-Kit Frontend Hackathon"
    url: "https://speckit-frontend-hackathon-gz7a.vercel.app/"

  design_principles:
    - modern_minimal
    - developer_focused
    - card_based_layout
    - readable_typography
    - dark_mode_first
    - consistent_spacing

  layout:
    navigation:
      type: "left_sidebar"
      collapsible: true
      dropdowns: true
    content:
      max_width: "1100px"
      centered: true
    header:
      sticky: true
      minimal: true

  components:
    cards:
      border_radius: "12px"
      shadow: "soft"
      hover_effect: true

    buttons:
      primary:
        - personalize
        - translate_urdu
        - ask_ai
      style:
        rounded: true
        icon_based: true

    chatbot:
      placement: "right_drawer"
      trigger: "floating_button"
      modes:
        - full_book
        - selected_text_only

  typography:
    font: "system-ui"
    headings: "semibold"
    body_line_height: "comfortable"

  colors:
    mode: "dark_default"
    accents:
      - indigo
      - violet
      - cyan

agents:
  core_agents:
    - name: BookAuthorAgent
      purpose: >
        Write structured, high-quality Docusaurus chapters
        following the approved outline.

    - name: RAGArchitectAgent
      purpose: >
        Design and implement the RAG pipeline including
        chunking, embedding, and retrieval.

    - name: FrontendIntegratorAgent
      purpose: >
        Implement the Spec-Kit UI style, chatbot drawer,
        and chapter-level buttons.

    - name: BackendServiceAgent
      purpose: >
        Build FastAPI services, database access,
        and vector search endpoints.

  bonus_agents:
    - name: PersonalizationAgent
      purpose: >
        Adapt chapter explanations based on user background.

    - name: TranslationAgent
      purpose: >
        Translate technical content into accurate Urdu.

    - name: AuthIntegrationAgent
      purpose: >
        Integrate Better-Auth for signup and signin.

    - name: UIDesignAgent
      purpose: >
        Ensure UI matches Spec-Kit Hackathon reference.

skills:
  reusable:
    - name: MarkdownChapterGeneration
      description: >
        Generate Docusaurus-ready markdown chapters.

    - name: RAGChunkingStrategy
      description: >
        Convert chapters into optimized embedding chunks.

    - name: SelectedTextQA
      description: >
        Answer questions strictly using selected text.

    - name: UserProfileInference
      description: >
        Infer learning preferences from signup data.

    - name: UrduTechnicalTranslation
      description: >
        Translate AI and software engineering content to Urdu.

authentication:
  provider: "Better-Auth"
  signup_questions:
    - software_background
    - programming_experience
    - ai_experience
    - hardware_knowledge
  usage:
    - personalize_content
    - adjust_difficulty
    - tailor_examples

rag:
  requirements:
    - answer_from_book_only
    - support_selected_text_only
    - prevent_hallucination
    - cite_chunks
  pipeline:
    - chunk_book
    - embed_chunks
    - store_in_qdrant
    - retrieve_top_k
    - generate_answer

quality:
  documentation:
    - clear
    - beginner_friendly
    - technically_correct
  code:
    - modular
    - readable
    - well_commented
  ux:
    - accessible
    - responsive
    - fast

evaluation:
  base_score_100:
    - published_book
    - working_rag_chatbot
    - github_pages_deployment

  bonus_points:
    reusable_intelligence: 50
    auth_personalization: 50
    chapter_personalization_button: 50
    urdu_translation_button: 50
