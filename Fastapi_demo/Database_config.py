import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load DB credentials from the .env file next to this script (not committed to git)
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.environ["DB_NAME"]

db_url = (
    f"postgresql+psycopg://{quote_plus(DB_USER)}:{quote_plus(DB_PASSWORD)}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine=create_engine(db_url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
