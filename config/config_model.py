from pydantic import BaseModel, Field
from pathlib import Path
import json


class AppConfig(BaseModel):
    base_url: str = Field(default="http://localhost:8080")
    encryption_key: str = Field(default="beautiful_rock_hello")


class ConfigManager:
    CONFIG_FILE = Path("config.json")

    @classmethod
    def load_config(cls) -> AppConfig:
        if cls.CONFIG_FILE.exists():
            with open(cls.CONFIG_FILE, "r", encoding="utf-8") as f:
                return AppConfig(**json.load(f))
        return AppConfig()

    @classmethod
    def save_config(cls, config: AppConfig):
        with open(cls.CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config.model_dump(), f, indent=2, ensure_ascii=False)
