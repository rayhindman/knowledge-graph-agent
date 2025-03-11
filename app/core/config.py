from pydantic import BaseSettings

class Settings(BaseSettings):
    # Neo4j Aura specific settings
    NEO4J_URI: str = "neo4j+ssc://3762d196.databases.neo4j.io"  # Using neo4j+ssc protocol to avoid certificate issues
    NEO4J_USERNAME: str = "neo4j"  # Default username, adjust if different
    NEO4J_PASSWORD: str
    NEO4J_DATABASE: str = "neo4j"  # Default database name
    NEO4J_INSTANCE_ID: str = "3762d196"
    NEO4J_QUERY_API_URL: str = "https://3762d196.databases.neo4j.io/db/{databaseName}/query/v2"
    
    # Service settings
    DEBUG: bool = False
    API_PORT: int = 8000
    API_HOST: str = "0.0.0.0"

    class Config:
        env_file = ".env"

settings = Settings()