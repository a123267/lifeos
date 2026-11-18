import os
from pathlib import Path
from dotenv import load_dotenv

# Locate the project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# Application configuration
APP_NAME = os.getenv("APP_NAME")
APP_ENV = os.getenv("APP_ENV")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Database configuration
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

if not DB_USER:
    raise ValueError("DB_USER is missing from the .env file")