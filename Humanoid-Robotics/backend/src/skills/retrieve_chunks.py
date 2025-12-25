from typing import List, Dict, Any
from src.utils.vector_db_factory import VectorDBFactory
from src.utils.embedding import EmbeddingService


class RetrieveChunks:
    def __init__(self):
        self.vector_db = VectorDBFactory.create_vector_db()
        self.embedding_service = EmbeddingService()

    async def retrieve_chunks(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieve relevant text chunks based on the query
        """
        # Create embedding for the query
        query_embedding = await self.embedding_service.create_embedding(query)

        # Search in the vector database
        results = await self.vector_db.search(
            query_embedding=query_embedding,
            limit=limit
        )

        return results

    async def retrieve_chunks_with_filter(self, query: str, filters: Dict[str, Any], limit: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieve relevant text chunks with specific filters (e.g., by chapter)
        """
        # Create embedding for the query
        query_embedding = await self.embedding_service.create_embedding(query)

        # In a full implementation, we would apply the filters to the search
        # For now, we'll just return the regular search results
        results = await self.vector_db.search(
            query_embedding=query_embedding,
            limit=limit
        )

        # Apply any post-retrieval filtering if needed
        if filters:
            filtered_results = []
            for result in results:
                match = True
                for key, value in filters.items():
                    if result.get(key) != value:
                        match = False
                        break
                if match:
                    filtered_results.append(result)
            return filtered_results

        return results

    async def retrieve_similar_chunks(self, text: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve chunks similar to the provided text
        """
        # Create embedding for the input text
        text_embedding = await self.embedding_service.create_embedding(text)

        # Search in the vector database
        results = await self.vector_db.search(
            query_embedding=text_embedding,
            limit=limit
        )

        return results