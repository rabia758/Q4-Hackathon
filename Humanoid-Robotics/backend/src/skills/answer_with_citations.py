from typing import List, Dict, Any, Tuple
from src.models.chat_models import Citation
from src.utils.config import settings
import openai


class AnswerWithCitations:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    async def generate_answer_with_citations(
        self,
        query: str,
        context: List[Dict[str, Any]],
        temperature: float = 0.1
    ) -> Tuple[str, List[Citation]]:
        """
        Generate an answer with proper citations from the context
        """
        if not context:
            return "This information is not available in the book.", []

        # Format the context
        formatted_context = ""
        citations = []

        for i, doc in enumerate(context):
            content = doc.get("content", "")
            chapter = doc.get("chapter", "Unknown")
            section = doc.get("section", "Unknown")
            score = doc.get("score", 0.0)

            formatted_context += f"\n\n[Source {i+1} - Chapter: {chapter}, Section: {section}]\n{content}"

            citations.append(
                Citation(
                    chapter=chapter,
                    section=section,
                    content=content[:200] + "..." if len(content) > 200 else content,
                    similarity_score=score
                )
            )

        # Create the prompt
        system_prompt = """You are an assistant for the Humanoid Robotics textbook.
        You must follow these rules strictly:
        1. ONLY use information from the provided textbook content
        2. NEVER answer from your general knowledge
        3. If the information is not in the provided context, say: 'This information is not available in the book.'
        4. Always cite the chapter and section when possible
        5. Be accurate and factual
        6. Reference the sources you're using in your response"""

        user_message = f"""
        Question: {query}

        Context from textbook:
        {formatted_context}

        Please provide an answer based only on the context provided above and cite the sources.
        """

        try:
            response = await openai.ChatCompletion.acreate(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=temperature,
                max_tokens=1000
            )

            answer = response.choices[0].message.content
            return answer, citations

        except Exception as e:
            print(f"Error generating answer: {e}")
            return "This information is not available in the book.", []

    async def validate_answer_factualness(self, answer: str, context: List[Dict[str, Any]]) -> bool:
        """
        Validate that the answer is factually consistent with the provided context
        """
        # This is a basic validation - in a full implementation,
        # we would use more sophisticated techniques
        if "not available in the book" in answer.lower():
            return True  # This is a valid response when info is not found

        # Check if the answer contains information from the context
        context_text = " ".join([doc.get("content", "") for doc in context])
        answer_lower = answer.lower()
        context_lower = context_text.lower()

        # Simple overlap check - in a real implementation we'd use semantic similarity
        answer_words = set(answer_lower.split()[:50])  # First 50 words
        context_words = set(context_lower.split())

        overlap = len(answer_words.intersection(context_words))
        total_answer_words = len(answer_words)

        # If at least 30% of the answer words appear in the context, consider it valid
        if total_answer_words > 0 and (overlap / total_answer_words) >= 0.3:
            return True

        return False

    async def format_citations_properly(self, citations: List[Citation]) -> str:
        """
        Format citations in a proper academic style
        """
        if not citations:
            return ""

        formatted = "Sources:\n"
        for i, citation in enumerate(citations, 1):
            formatted += f"{i}. {citation.chapter} - {citation.section}\n"

        return formatted