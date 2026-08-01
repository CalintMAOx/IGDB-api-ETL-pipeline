import requests

def get_games(client_id, access_token, offset, limit):
    url = "https://api.igdb.com/v4/games"
    headers = {
        'Client-ID' : client_id,
        'Authorization' : f'Bearer {access_token}'
    }

    while True:
        body = f"fields id,name,game_type,genres,total_rating,total_rating_count;where game_type = 0;limit 500; offset {offset};"
        offset += limit

        response = requests.post(url, headers=headers, data=body)

        if response.status_code == 200:
                return response.json()
        else:
            print(f"Error: {response.status_code}")
        return None