from typing import List, Dict, Any
from pydantic import BaseModel
from src.utils.vector_db_factory import VectorDBFactory
from src.utils.embedding import EmbeddingService
from src.models.chat_models import Message


class RetrieverAgent:
    def __init__(self):
        self.vector_db = VectorDBFactory.create_vector_db()
        self.embedding_service = EmbeddingService()

    async def retrieve(
        self,
        query_embedding: List[float],
        query_text: str,
        history: List[Message] = None,
        selected_text: str = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevant documents from the vector store
        """
        if selected_text:
            # If selected text is provided, only search within that text
            return await self.retrieve_selected_text(
                query_embedding=query_embedding,
                query_text=query_text,
                selected_text=selected_text,
                history=history
            )
        else:
            # Search in the full database
            return await self.vector_db.search(
                query_embedding=query_embedding,
                limit=10
            )

    async def retrieve_selected_text(
        self,
        query_embedding: List[float],
        query_text: str,
        selected_text: str,
        history: List[Message] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevant documents but only from the selected text
        This enforces the "selected text only" requirement
        """
        # Check if the vector_db has the search_with_filter method (real DB)
        if hasattr(self.vector_db, 'search_with_filter'):
            return await self.vector_db.search_with_filter(
                query_embedding=query_embedding,
                selected_text=selected_text,
                limit=10
            )
        else:
            # For mock DB or fallback, return the selected text as context
            return [{
                "id": "selected_text_chunk",
                "content": selected_text,
                "chapter": "Selected Text",
                "section": "User Selection",
                "source_file": "user_input",
                "score": 1.0,  # High score since it's exact match
                "metadata": {}
            }]

    async def retrieve_with_context(
        self,
        query_embedding: List[float],
        context_window: int = 2
    ) -> List[Dict[str, Any]]:
        """
        Retrieve documents with surrounding context
        """
        results = await self.vector_db.search(
            query_embedding=query_embedding,
            limit=5
        )

        # Enhance with context if needed
        enhanced_results = []
        for result in results:
            enhanced_results.append(result)

        return enhanced_results