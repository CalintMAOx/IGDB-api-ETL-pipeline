from src.client_token_getter import igdb_client_token_getter
from src.extract import get_games_top100
from src.init_db import init_db
from src.load import load
from src.transform import transform

client_id, token = igdb_client_token_getter()
games = get_games_top100(client_id, token)

transformed_games = transform(games)

init_db()

load(transformed_games)