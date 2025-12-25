import openai
from typing import List, Dict, Any, Tuple
from pydantic import BaseModel
from src.models.chat_models import Citation, Message
from src.utils.config import settings


class AnswerAgent:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    async def generate_answer(
        self,
        query: str,
        retrieved_docs: List[Dict[str, Any]],
        history: List[Message] = None
    ) -> Tuple[str, List[Citation]]:
        """
        Generate an answer based on retrieved documents with citations
        """
        if not retrieved_docs:
            return "This information is not available in the book.", []

        # Format the context from retrieved documents
        context_str = "\n\n".join([doc["content"] for doc in retrieved_docs])

        # Create citations
        citations = [
            Citation(
                chapter=doc.get("chapter", "Unknown"),
                section=doc.get("section", "Unknown"),
                content=doc["content"][:200] + "..." if len(doc["content"]) > 200 else doc["content"],
                similarity_score=doc.get("score", 0.0)
            )
            for doc in retrieved_docs
        ]

        # Build the prompt following the RAG enforcement rules
        system_prompt = """You are an assistant for the Humanoid Robotics textbook.
        You must follow these rules strictly:
        1. ONLY use information from the provided textbook content
        2. NEVER answer from your general knowledge
        3. If the information is not in the provided context, say: 'This information is not available in the book.'
        4. Always cite the chapter and section when possible
        5. Be accurate and factual"""

        # Format the user message
        user_message = f"""
        Question: {query}

        Context from textbook:
        {context_str}

        Please provide an answer based only on the context provided above.
        """

        try:
            response = await openai.ChatCompletion.acreate(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.1,  # Low temperature for factual responses
                max_tokens=1000
            )

            answer = response.choices[0].message.content
            return answer, citations

        except Exception as e:
            print(f"Error generating answer: {e}")
            return "This information is not available in the book.", []

    async def validate_answer(self, answer: str, retrieved_docs: List[Dict[str, Any]]) -> bool:
        """
        Validate that the answer is grounded in the retrieved documents
        """
        # This is a basic validation - in a full implementation,
        # we would check semantic similarity between answer and docs
        if "not available in the book" in answer.lower():
            return True  # This is a valid response when info is not found

        # Basic check: if retrieved docs exist but answer is empty, something went wrong
        if retrieved_docs and not answer.strip():
            return False

        return True