import asyncio
import os
import sys
from pathlib import Path

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from skills.ingest_book_content import IngestBookContent


async def ensure_content_ingested():
    """
    Function to ensure textbook content is ingested into the vector database
    """
    print("Checking if textbook content needs to be ingested...")

    # Initialize the ingestion skill
    ingest_skill = IngestBookContent()

    # Define the paths to the textbook content
    textbook_paths = [
        "../../../frontend/docs/chapter-01-introduction-to-physical-ai-robotics",
        "../../../frontend/docs/chapter-02-mathematics-for-robotics",
        "../../../frontend/docs/chapter-03-robot-kinematics",
        "../../../frontend/docs/chapter-04-robot-dynamics",
        "../../../frontend/docs/chapter-05-sensors-for-humanoid-robotics"
    ]

    # Convert relative paths to absolute paths
    base_dir = Path(__file__).parent
    absolute_paths = [str(base_dir / path) for path in textbook_paths]

    print(f"Ingesting documents from: {absolute_paths}")

    try:
        results = await ingest_skill.ingest_documents(absolute_paths)
        print(f"Successfully ingested {len(results)} document chunks into the vector database")

        # Print summary of ingestion
        chapters = set()
        for result in results:
            if result.get('chapter'):
                chapters.add(result['chapter'])

        print(f"Chapters processed: {list(chapters)}")
        print(f"Total chunks ingested: {len(results)}")

        return True

    except Exception as e:
        print(f"Error during ingestion: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_ingestion():
    """
    Synchronous wrapper for the ingestion function
    """
    return asyncio.run(ensure_content_ingested())


if __name__ == "__main__":
    run_ingestion()