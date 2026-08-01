from database import get_db_connection
from src.client_token_getter import igdb_client_token_getter
from src.extract import get_games
from src.init_db import init_db
from src.load import load
from src.transform import transform

client_id, token = igdb_client_token_getter()

init_db()

offset = 0
limit = 500

db = get_db_connection()
cursor = db.cursor()

while True:
    games = get_games(client_id, token, offset, limit)

    if not games:
        print("Finished downloading all games.")
        break

    transformed_games = transform(games)
    load(transformed_games, db, cursor)
    offset += limit

db.close()
cursor.close()
print("Finished saving all games.")