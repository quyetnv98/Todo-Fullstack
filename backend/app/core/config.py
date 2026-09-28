import os

class Settings:
    PROJECT_NAME: str = "Todo App REST API"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./todos.db"

settings = Settings()
