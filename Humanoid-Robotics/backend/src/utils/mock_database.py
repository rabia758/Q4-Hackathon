from typing import List, Dict, Any, Optional
import uuid
from .config import settings


class MockVectorDB:
    def __init__(self):
        self.documents = []
        self.collection_name = settings.QDRANT_COLLECTION_NAME

    async def add_documents(self, documents: List[Dict[str, Any]]) -> bool:
        """Mock adding documents to the vector store"""
        try:
            for doc in documents:
                doc_with_id = {
                    "id": str(uuid.uuid4()),
                    **doc
                }
                self.documents.append(doc_with_id)
            return True
        except Exception as e:
            print(f"Error adding documents: {e}")
            return False

    async def search(self, query_embedding: List[float], limit: int = 10) -> List[Dict[str, Any]]:
        """Mock search for similar documents"""
        try:
            # In a real implementation, this would perform vector similarity search
            # For the mock, we'll return documents that have some similarity to the query
            # based on simple keyword matching in content

            # For now, return the first few documents as mock results
            results = []
            for i, doc in enumerate(self.documents[:limit]):
                results.append({
                    "id": doc["id"],
                    "content": doc.get("content", ""),
                    "chapter": doc.get("chapter", ""),
                    "section": doc.get("section", ""),
                    "source_file": doc.get("source_file", ""),
                    "score": 0.8,  # Mock similarity score
                    "metadata": doc.get("metadata", {})
                })

            return results
        except Exception as e:
            print(f"Error searching documents: {e}")
            return []

    async def search_with_filter(self, query_embedding: List[float], selected_text: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Mock search for similar documents but only from selected text"""
        try:
            # For the mock, return documents that contain the selected text
            results = []
            for doc in self.documents:
                if selected_text.lower() in doc.get("content", "").lower():
                    results.append({
                        "id": doc["id"],
                        "content": doc.get("content", ""),
                        "chapter": doc.get("chapter", ""),
                        "section": doc.get("section", ""),
                        "source_file": doc.get("source_file", ""),
                        "score": 0.9,  # Higher score for filtered match
                        "metadata": doc.get("metadata", {})
                    })
                    if len(results) >= limit:
                        break

            return results[:limit]
        except Exception as e:
            print(f"Error searching documents with filter: {e}")
            return []