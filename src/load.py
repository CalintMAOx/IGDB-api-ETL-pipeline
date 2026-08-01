from sqlalchemy.dialects.postgresql import insert
from database import get_db_connection



def load(transformed_games, db, cursor):
    try:
        if not transformed_games:
            return

        records_to_insert = (
            (
                game.get('id'),
                game.get('name'),
                game.get('genres'),
                game.get('rating'),
                game.get('number_of_ratings')
            )
            for game in transformed_games
        )

        cursor.execute("""
            CREATE TEMP TABLE temp_games
            (
                id                INTEGER,
                name              VARCHAR(255),
                genres            INTEGER[],
                rating            FLOAT,
                number_of_ratings INTEGER
            ) ON COMMIT DROP;
        """)

        with cursor.copy("COPY temp_games (id, name, genres, rating, number_of_ratings) FROM STDIN") as copy:
            for record in records_to_insert:
                copy.write_row(record)

        cursor.execute("""
            INSERT INTO games (id, name, genres, rating, number_of_ratings)
            SELECT id, name, genres, rating, number_of_ratings
            FROM temp_games
            ON CONFLICT (id) DO UPDATE SET
                    name = EXCLUDED.name, 
                    genres = EXCLUDED.genres,
                    rating = EXCLUDED.rating, 
                    number_of_ratings = EXCLUDED.number_of_ratings
            """)
        db.commit()
        print("Data saved to cloud database.")

    except Exception as e:
        print("Error while saving data:")
        print(e)
        db.rollback()