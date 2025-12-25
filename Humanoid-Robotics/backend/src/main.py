from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# Import agent modules
from src.agents.rag_manager import RAGManager
from src.agents.retriever_agent import RetrieverAgent
from src.agents.answer_agent import AnswerAgent
from src.agents.selection_filter_agent import SelectionFilterAgent

# Import skills
from src.skills.ingest_book_content import IngestBookContent
from src.skills.retrieve_chunks import RetrieveChunks
from src.skills.answer_with_citations import AnswerWithCitations

# Import models
from src.models.chat_models import ChatRequest, ChatResponse, IngestRequest, IngestResponse

app = FastAPI(
    title="Humanoid Robotics RAG API",
    description="RAG Chatbot API for Humanoid Robotics textbook",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import startup module for content ingestion
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from startup import run_ingestion

@app.on_event("startup")
async def startup_event():
    print("Running startup tasks...")
    # Run content ingestion on startup
    success = run_ingestion()
    if success:
        print("Content ingestion completed successfully")
    else:
        print("Content ingestion failed, but the API will still start")

# Initialize agents and skills
rag_manager = RAGManager()
retriever_agent = RetrieverAgent()
answer_agent = AnswerAgent()
selection_filter_agent = SelectionFilterAgent()

ingest_skill = IngestBookContent()
retrieve_skill = RetrieveChunks()
answer_skill = AnswerWithCitations()

@app.get("/")
async def root():
    return {"message": "Humanoid Robotics RAG API is running!"}

@app.post("/ingest", response_model=IngestResponse)
async def ingest_documents(request: IngestRequest):
    """Ingest Docusaurus markdown files into the vector store"""
    try:
        result = await ingest_skill.ingest_documents(request.file_paths)
        return IngestResponse(success=True, message=f"Successfully ingested {len(result)} documents")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error ingesting documents: {str(e)}")

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat endpoint for full book queries"""
    try:
        response = await rag_manager.process_request(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

@app.post("/chat/selected", response_model=ChatResponse)
async def chat_selected_text(request: ChatRequest):
    """Chat endpoint for selected text only queries"""
    try:
        response = await selection_filter_agent.process_selected_text_request(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing selected text request: {str(e)}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)