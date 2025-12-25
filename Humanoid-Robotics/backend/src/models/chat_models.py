from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime


class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: Optional[datetime] = None


class ChatRequest(BaseModel):
    query: str
    history: Optional[List[Message]] = []
    selected_text: Optional[str] = None  # For selected text mode
    max_tokens: Optional[int] = 1000
    temperature: Optional[float] = 0.1  # Low temperature for factual responses


class Citation(BaseModel):
    chapter: str
    section: str
    content: str
    similarity_score: float


class ChatResponse(BaseModel):
    response: str
    citations: List[Citation]
    tokens_used: Optional[int] = None
    processing_time: Optional[float] = None


class IngestRequest(BaseModel):
    file_paths: List[str]
    chunk_size: Optional[int] = 1000
    chunk_overlap: Optional[int] = 200


class IngestResponse(BaseModel):
    success: bool
    message: str
    documents_processed: Optional[int] = None