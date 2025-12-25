import os
import asyncio
from typing import List, Dict, Any
from pathlib import Path
from src.utils.vector_db_factory import VectorDBFactory
from src.utils.embedding import EmbeddingService
from src.utils.config import settings
import markdown
from bs4 import BeautifulSoup


class IngestBookContent:
    def __init__(self):
        self.vector_db = VectorDBFactory.create_vector_db()
        self.embedding_service = EmbeddingService()

    async def ingest_documents(self, file_paths: List[str]) -> List[Dict[str, Any]]:
        """
        Ingest markdown documents from Docusaurus into the vector store
        """
        all_chunks = []

        for file_path in file_paths:
            if os.path.isfile(file_path) and file_path.endswith('.md'):
                chunks = await self._process_markdown_file(file_path)
                all_chunks.extend(chunks)
            elif os.path.isdir(file_path):
                # Process all markdown files in the directory
                for root, dirs, files in os.walk(file_path):
                    for file in files:
                        if file.endswith('.md'):
                            file_path_full = os.path.join(root, file)
                            chunks = await self._process_markdown_file(file_path_full)
                            all_chunks.extend(chunks)

        # Add all chunks to the vector database
        if all_chunks:
            success = await self.vector_db.add_documents(all_chunks)
            if success:
                return all_chunks

        return []

    async def _process_markdown_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Process a single markdown file and extract content with metadata
        """
        chunks = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract chapter and section info from file path
            path_parts = file_path.split(os.sep)
            chapter = ""
            section = ""

            # Look for chapter in path
            for part in path_parts:
                if 'chapter' in part.lower():
                    chapter = part
                    break

            # Parse markdown to extract sections
            html = markdown.markdown(content)
            soup = BeautifulSoup(html, 'html.parser')

            # Get the main title (first H1)
            title_tag = soup.find('h1')
            if title_tag:
                section = title_tag.get_text().strip()

            # Split content into chunks
            content_chunks = self._chunk_text(content, chunk_size=1000, overlap=200)

            for i, chunk in enumerate(content_chunks):
                # Create embedding for the chunk
                embedding = await self.embedding_service.create_embedding(chunk)

                chunk_data = {
                    "content": chunk,
                    "embedding": embedding,
                    "chapter": chapter,
                    "section": f"{section} - Part {i+1}" if section else f"Part {i+1}",
                    "source_file": file_path,
                    "metadata": {
                        "file_path": file_path,
                        "chunk_index": i,
                        "total_chunks": len(content_chunks)
                    }
                }

                chunks.append(chunk_data)

        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

        return chunks

    def _chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """
        Split text into overlapping chunks
        """
        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size

            # If we're near the end, just take the remainder
            if end > len(text):
                end = len(text)

            chunk = text[start:end]
            chunks.append(chunk)

            # Move start forward by chunk_size - overlap
            start = end - overlap

            # If start is >= len(text), we're done
            if start >= len(text):
                break

        return chunks

    async def _extract_sections_from_markdown(self, content: str) -> List[Dict[str, str]]:
        """
        Extract sections from markdown content based on headers
        """
        sections = []

        lines = content.split('\n')
        current_section = {"title": "Introduction", "content": ""}

        for line in lines:
            if line.startswith('# '):  # H1
                if current_section["content"].strip():
                    sections.append(current_section)
                current_section = {"title": line[2:].strip(), "content": ""}
            elif line.startswith('## '):  # H2
                if current_section["content"].strip():
                    sections.append(current_section)
                current_section = {"title": line[3:].strip(), "content": ""}
            else:
                current_section["content"] += line + "\n"

        # Add the last section
        if current_section["content"].strip():
            sections.append(current_section)

        return sections