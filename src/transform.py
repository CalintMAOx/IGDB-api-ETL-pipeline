def transform(games):
    transformed_games = []

    for game in games:
        transformed_games.append({
            "id": game.get('id'),
            "name": game.get('name'),
            "genres": game.get('genres'),
            "rating": game.get('total_rating') if game.get('total_rating') else float(-1),
            "number_of_ratings": game.get('total_rating_count') if game.get('total_rating_count') else -1
        })

    return transformed_games