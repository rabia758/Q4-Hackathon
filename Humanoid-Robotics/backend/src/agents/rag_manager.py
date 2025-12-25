from typing import Dict, Any, List
from pydantic import BaseModel
from src.models.chat_models import ChatRequest, ChatResponse, Citation
from src.agents.retriever_agent import RetrieverAgent
from src.agents.answer_agent import AnswerAgent
from src.utils.database import VectorDB
from src.utils.embedding import EmbeddingService


class RAGManager:
    def __init__(self):
        self.retriever_agent = RetrieverAgent()
        self.answer_agent = AnswerAgent()
        self.vector_db = VectorDB()
        self.embedding_service = EmbeddingService()

    async def process_request(self, request: ChatRequest) -> ChatResponse:
        """
        Process a chat request using the RAG approach
        """
        # Step 1: Create embedding for the query
        query_embedding = await self.embedding_service.create_embedding(request.query)

        # Step 2: Retrieve relevant documents
        retrieved_docs = await self.retriever_agent.retrieve(
            query_embedding=query_embedding,
            query_text=request.query,
            history=request.history,
            selected_text=request.selected_text
        )

        # Step 3: Generate answer based on retrieved documents
        answer, citations = await self.answer_agent.generate_answer(
            query=request.query,
            retrieved_docs=retrieved_docs,
            history=request.history
        )

        # Step 4: Return response with citations
        response = ChatResponse(
            response=answer,
            citations=citations
        )

        return response

    async def process_selected_text_request(self, request: ChatRequest) -> ChatResponse:
        """
        Process a chat request that should only use selected text
        """
        # Step 1: Create embedding for the query
        query_embedding = await self.embedding_service.create_embedding(request.query)

        # Step 2: Retrieve relevant documents from selected text only
        retrieved_docs = await self.retriever_agent.retrieve_selected_text(
            query_embedding=query_embedding,
            query_text=request.query,
            selected_text=request.selected_text or "",
            history=request.history
        )

        # Step 3: Generate answer based on retrieved documents
        answer, citations = await self.answer_agent.generate_answer(
            query=request.query,
            retrieved_docs=retrieved_docs,
            history=request.history
        )

        # Step 4: Return response with citations
        response = ChatResponse(
            response=answer,
            citations=citations
        )

        return response