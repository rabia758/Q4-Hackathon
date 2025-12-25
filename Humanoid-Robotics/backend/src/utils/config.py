from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Qdrant settings
    QDRANT_URL: Optional[str] = None
    QDRANT_API_KEY: Optional[str] = None
    QDRANT_COLLECTION_NAME: str = "humanoid_robotics_textbook"
    EMBEDDING_DIM: int = 1536  # Default for OpenAI embeddings

    # OpenAI settings
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-3.5-turbo"

    # Application settings
    APP_NAME: str = "Humanoid Robotics RAG API"
    DEBUG: bool = False
    PORT: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()