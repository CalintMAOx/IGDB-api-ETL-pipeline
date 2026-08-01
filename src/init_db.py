
from src.database import get_db_connection

def init_db():
    print("Initializing database...")

    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY,
                name VARCHAR(255),
                genres INTEGER[],
                rating FLOAT,
                number_of_ratings INTEGER
            );
                """)
            conn.commit()

    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()