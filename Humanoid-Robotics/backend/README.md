# Humanoid Robotics RAG Backend

This is the backend service for the Humanoid Robotics textbook RAG (Retrieval-Augmented Generation) system.

## Architecture

The backend consists of:
- FastAPI web framework
- OpenAI integration for embeddings and responses
- Qdrant vector database for document storage and retrieval
- Multiple specialized agents for different aspects of the RAG process

## Components

### Agents
- `RAGManager`: Orchestrates the entire RAG process
- `RetrieverAgent`: Handles document retrieval from the vector store
- `AnswerAgent`: Generates answers based on retrieved documents
- `SelectionFilterAgent`: Enforces selected-text-only queries

### Skills
- `IngestBookContent`: Processes and ingests textbook content
- `RetrieveChunks`: Retrieves relevant text chunks
- `AnswerWithCitations`: Generates answers with proper citations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
# Edit .env with your actual API keys and configuration
```

3. Run the application:
```bash
cd src
python main.py
```

Or with uvicorn:
```bash
cd src
uvicorn main:app --reload --port 8000
```

## API Endpoints

- `GET /` - Health check
- `POST /ingest` - Ingest documents into the vector store
- `POST /chat` - Chat with the full textbook
- `POST /chat/selected` - Chat with only selected text

## Environment Variables

- `QDRANT_URL`: URL for your Qdrant instance
- `QDRANT_API_KEY`: API key for Qdrant
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: OpenAI model to use (default: gpt-3.5-turbo)
- `PORT`: Port to run the server on (default: 8000)