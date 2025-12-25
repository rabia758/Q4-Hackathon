import qdrant_client
from qdrant_client.http import models
from typing import List, Dict, Any, Optional
import uuid
from .config import settings


class VectorDB:
    def __init__(self):
        self.client = qdrant_client.QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            # If using local Qdrant, use:
            # host="localhost",
            # port=6333
        )
        self.collection_name = settings.QDRANT_COLLECTION_NAME
        self._ensure_collection_exists()

    def _ensure_collection_exists(self):
        """Create the collection if it doesn't exist"""
        try:
            self.client.get_collection(self.collection_name)
        except:
            # Create collection with vector configuration
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=settings.EMBEDDING_DIM,  # e.g., 1536 for OpenAI embeddings
                    distance=models.Distance.COSINE
                )
            )

    async def add_documents(self, documents: List[Dict[str, Any]]) -> bool:
        """Add documents to the vector store"""
        try:
            points = []
            for doc in documents:
                point = models.PointStruct(
                    id=str(uuid.uuid4()),
                    vector=doc["embedding"],  # This should be the embedding vector
                    payload={
                        "content": doc["content"],
                        "chapter": doc.get("chapter", ""),
                        "section": doc.get("section", ""),
                        "source_file": doc.get("source_file", ""),
                        "metadata": doc.get("metadata", {})
                    }
                )
                points.append(point)

            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            return True
        except Exception as e:
            print(f"Error adding documents: {e}")
            return False

    async def search(self, query_embedding: List[float], limit: int = 10) -> List[Dict[str, Any]]:
        """Search for similar documents"""
        try:
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
                with_payload=True
            )

            documents = []
            for result in results:
                documents.append({
                    "id": result.id,
                    "content": result.payload["content"],
                    "chapter": result.payload["chapter"],
                    "section": result.payload["section"],
                    "source_file": result.payload["source_file"],
                    "score": result.score,
                    "metadata": result.payload["metadata"]
                })

            return documents
        except Exception as e:
            print(f"Error searching documents: {e}")
            return []

    async def search_with_filter(self, query_embedding: List[float], selected_text: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for similar documents but only from selected text"""
        try:
            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                query_filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="content",
                            match=models.MatchText(text=selected_text[:100])  # Using first 100 chars as filter
                        )
                    ]
                ) if selected_text else None,
                limit=limit,
                with_payload=True
            )

            documents = []
            for result in results:
                documents.append({
                    "id": result.id,
                    "content": result.payload["content"],
                    "chapter": result.payload["chapter"],
                    "section": result.payload["section"],
                    "source_file": result.payload["source_file"],
                    "score": result.score,
                    "metadata": result.payload["metadata"]
                })

            return documents
        except Exception as e:
            print(f"Error searching documents with filter: {e}")
            return []