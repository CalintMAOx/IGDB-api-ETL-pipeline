import requests

def get_games_top100(client_id, access_token):
    url = "https://api.igdb.com/v4/games"
    headers = {
        'Client-ID' : client_id,
        'Authorization' : f'Bearer {access_token}'
    }

    body = "fields id,name,game_type,genres,platforms,release_dates,themes,total_rating,total_rating_count,url,websites,videos; where total_rating_count >= 20; sort total_rating desc; limit 100;"

    response = requests.post(url, headers=headers, data=body)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None