import asyncio
import os
import sys
from pathlib import Path

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.skills.ingest_book_content import IngestBookContent
from src.agents.rag_manager import RAGManager
from src.models.chat_models import ChatRequest, Message


async def test_ingestion():
    """Test the ingestion system"""
    print("Testing document ingestion...")

    ingest_skill = IngestBookContent()

    # Test with a single file to make sure it works
    test_paths = ["../frontend/docs/chapter-01-introduction-to-physical-ai-robotics/index.md"]

    try:
        results = await ingest_skill.ingest_documents(test_paths)
        print(f"✓ Successfully ingested {len(results)} chunks")
        if results:
            print(f"  First chunk: {results[0]['content'][:100]}...")
        return True
    except Exception as e:
        print(f"✗ Ingestion failed: {e}")
        return False


async def test_retrieval():
    """Test the retrieval system"""
    print("\nTesting retrieval system...")

    try:
        rag_manager = RAGManager()

        # Create a test request
        request = ChatRequest(
            query="What is Physical AI Robotics?",
            history=[]
        )

        # Process the request (this will test retrieval and answer generation)
        response = await rag_manager.process_request(request)

        print(f"✓ Retrieved and generated response")
        print(f"  Response: {response.response[:200]}...")
        print(f"  Citations: {len(response.citations)} found")

        return True
    except Exception as e:
        print(f"✗ Retrieval/Generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_selected_text():
    """Test the selected text functionality"""
    print("\nTesting selected text functionality...")

    try:
        rag_manager = RAGManager()

        # Create a test request with selected text
        sample_text = "Physical AI Robotics is an interdisciplinary field that combines artificial intelligence with physical robotic systems. It focuses on creating robots that can perceive, reason, and act in the physical world."

        request = ChatRequest(
            query="What is Physical AI Robotics?",
            selected_text=sample_text,
            history=[]
        )

        # Process the request using the selected text method
        response = await rag_manager.process_selected_text_request(request)

        print(f"✓ Processed selected text request")
        print(f"  Response: {response.response[:200]}...")
        print(f"  Citations: {len(response.citations)} found")

        return True
    except Exception as e:
        print(f"✗ Selected text test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def run_all_tests():
    """Run all tests for the RAG system"""
    print("Starting RAG system tests...\n")

    results = []

    # Test 1: Ingestion
    results.append(("Ingestion", await test_ingestion()))

    # Test 2: Retrieval and Generation
    results.append(("Retrieval & Generation", await test_retrieval()))

    # Test 3: Selected Text
    results.append(("Selected Text", await test_selected_text()))

    # Print summary
    print("\n" + "="*50)
    print("TEST RESULTS SUMMARY:")
    print("="*50)

    all_passed = True
    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{test_name:.<30} {status}")
        if not passed:
            all_passed = False

    print("="*50)
    if all_passed:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed.")

    return all_passed


if __name__ == "__main__":
    asyncio.run(run_all_tests())