import os
import requests
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

def igdb_client_token_getter():
    """Authenticates with Twitch to provide a temporary IGDB access token"""

    auth_url = "https://id.twitch.tv/oauth2/token"
    auth_params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }

    print("Requesting Twitch access token...")
    response = requests.post(auth_url, params=auth_params)

    if response.status_code == 200:
        token_data = response.json()
        print("Token acquired successfully!")
        return CLIENT_ID, token_data['access_token']
    else:
        print(f"Failed to get token. Status: {response.status_code}")
        print(response.text)
        return None, None

# Test the function if this script is run directly
if __name__ == "__main__":
    client_id, token = igdb_client_token_getter()
    if token:
        # Print just the first 4 characters so we don't expose the whole token
        print(f"Your token starts with: {token[:4]}")

