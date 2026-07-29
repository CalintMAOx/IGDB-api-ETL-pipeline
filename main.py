from src.client_token_getter import igdb_client_token_getter
from src.extract import get_games_top100


client_id, token = igdb_client_token_getter()
data = get_games_top100(client_id, token)


print(data)