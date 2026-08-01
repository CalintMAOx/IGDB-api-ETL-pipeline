import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    DATABASE_URL = os.getenv("DATABASE_URL")

    return psycopg.connect(DATABASE_URL)