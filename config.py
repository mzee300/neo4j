import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "Test")
    NEO4J_HOST = os.getenv("NEO4J_HOST", "neo4j")
    NEO4J_PORT = os.getenv("NEO4J_PORT", "7687")
    NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
    NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

    NEO4J_URI = f"bolt://{NEO4J_HOST}:{NEO4J_PORT}/{NEO4J_DATABASE}"

    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
