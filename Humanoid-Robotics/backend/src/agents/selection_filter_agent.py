from typing import List, Dict, Any, Tuple
from src.models.chat_models import ChatRequest, ChatResponse, Citation, Message
from src.utils.database import VectorDB
from src.utils.embedding import EmbeddingService
from src.agents.answer_agent import AnswerAgent


class SelectionFilterAgent:
    def __init__(self):
        self.answer_agent = AnswerAgent()
        self.vector_db = VectorDB()
        self.embedding_service = EmbeddingService()

    async def process_selected_text_request(self, request: ChatRequest) -> ChatResponse:
        """
        Process a request that should only use the selected text
        Enforce the rule that only selected text can be used
        """
        if not request.selected_text:
            # If no selected text is provided, this is an error
            return ChatResponse(
                response="No selected text provided. Please select text from the textbook to ask about.",
                citations=[]
            )

        # For selected text mode, we'll use the selected text directly
        # without retrieving from the database
        retrieved_docs = [{
            "id": "selected_text",
            "content": request.selected_text,
            "chapter": "Selected Text",
            "section": "User Selection",
            "source_file": "user_input",
            "score": 1.0,
            "metadata": {}
        }]

        # Generate answer based on selected text only
        answer, citations = await self.answer_agent.generate_answer(
            query=request.query,
            retrieved_docs=retrieved_docs,
            history=request.history
        )

        # Validate that the answer is based on the selected text
        # (This is more of a conceptual validation in this implementation)
        is_valid = await self.validate_answer_against_selection(
            answer, request.selected_text
        )

        if not is_valid and "not available in the book" not in answer.lower():
            # If the answer doesn't seem to be based on the selection,
            # and it's not a "not found" response, return a warning
            answer = f"Could not find specific information in the selected text. Selected text does not contain the requested information.\n\nSelected text: {request.selected_text[:200]}..."

        return ChatResponse(
            response=answer,
            citations=citations
        )

    async def validate_answer_against_selection(self, answer: str, selected_text: str) -> bool:
        """
        Validate that the answer is relevant to the selected text
        """
        # This is a basic validation - in a full implementation,
        # we would use more sophisticated semantic analysis
        if "not available in the book" in answer.lower():
            return True  # This is a valid response when info is not found in selection

        # Basic check: see if there's any overlap between answer and selected text
        answer_lower = answer.lower()
        selected_lower = selected_text.lower()

        # Look for some common words between the answer and selected text
        answer_words = set(answer_lower.split()[:20])  # First 20 words for efficiency
        selected_words = set(selected_lower.split())

        common_words = answer_words.intersection(selected_words)
        if len(common_words) > 0:
            return True

        # If no common words but it's not a "not found" response,
        # the answer might not be based on the selection
        return False