# src/config.py
from dataclasses import dataclass
import os

@dataclass
class Settings:
    openai_api_key: str | None
    model: str

def load_settings() -> Settings:
    return Settings(
        openai_api_key=os.environ.get("OPENAI_API_KEY"),
        model=os.environ.get("AI_ASSISTANT_MODEL", "gpt-3.5-turbo")
    )
