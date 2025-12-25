import qdrant_client
from typing import List, Dict, Any, Optional
from .config import settings
from .mock_database import MockVectorDB


class VectorDBFactory:
    @staticmethod
    def create_vector_db():
        """Create and return either a real VectorDB or a MockVectorDB based on availability"""
        if settings.QDRANT_URL and settings.QDRANT_API_KEY:
            try:
                # Try to connect to the real Qdrant service
                client = qdrant_client.QdrantClient(
                    url=settings.QDRANT_URL,
                    api_key=settings.QDRANT_API_KEY,
                )
                # Test the connection
                client.get_collections()
                # If successful, return the real database
                from .database import VectorDB
                return VectorDB()
            except Exception as e:
                print(f"Real Qdrant connection failed: {e}. Using mock database.")
                return MockVectorDB()
        else:
            print("Qdrant credentials not provided. Using mock database.")
            return MockVectorDB()