from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pathlib import Path

# Path to the .env file in the project root directory
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(env_path)

class Settings(BaseSettings):
    PROJECT_TITLE: str = "na-order-producer"
    PROJECT_VERSION: str = "0.1"
    
    KAFKA_TOPIC_NAME: str
    KAFKA_BOOTSTRAP_SERVERS: str  # Corrected attribute name
    KAFKA_REPLICATION_FACTOR: int  # Corrected type (assuming it's an integer)
    KAFKA_NUM_PARTITION: int       # Corrected type (assuming it's an integer)
    KAFKA_ACK: str
    
    # Database Details
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int  # Corrected type (assuming it's an integer)
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    
    # Basic Setup
    TITLE: str
    VERSION: str
    PYTHONDONTWRITEBYTECODE: int  # Corrected type (assuming it's an integer)
    
    class Config:
        env_path = env_path
        
settings = Settings()
