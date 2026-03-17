from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Finance AI Assistant"
    LOG_LEVEL: str = "INFO"
    DATABASE_URL: str = "sqlite:///data/expenses.db"
    OLLAMA_MODEL: str = "llama3.2"
    OLLAMA_URL: str = "http://localhost:11434"
    CHROMA_PATH: str = "data/chroma"

    model_config = SettingsConfigDict(env_file=".env")
    

settings = Settings()