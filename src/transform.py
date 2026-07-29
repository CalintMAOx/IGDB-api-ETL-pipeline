from src.models import Game

def transform(games):
    transformed_games = []

    for game in games:
        new_game = Game(
            id = game.get('id'),
            name = game.get('name'),
            game_type = game.get('game_type'),
            genre = game.get('genres')[0],
            rating = game.get('total_rating'),
            number_of_ratings = game.get('total_rating_count'),
        )
        transformed_games.append(new_game)

    return transformed_games