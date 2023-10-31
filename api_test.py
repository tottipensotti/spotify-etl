import os
import base64
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env
load_dotenv()

def getAccessToken():
    """
    Retrieves an access token for the Spotify API
    using the user credentials from environment variables.

    Returns:
        str: The access token.
    """
    
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    auth_url = "https://accounts.spotify.com/api/token"
    base64_auth = base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()

    data = {
        'grant_type': 'client_credentials'
    }

    headers = {
        'Authorization': f'Basic {base64_auth}'
    }

    response = requests.post(auth_url, data=data, headers=headers)

    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info["access_token"]
        return access_token
    else:
        print(f"Error: {response.status_code}")
        return None

def getArtistData(artist_id, access_token):
    """
    Retrieves data about a Spotify artist.

    Args:
        artist_id (str): The Spotify artist ID.
        access_token (str): The access token for the Spotify API.

    Returns:
        dict: Information about the artist.
    """

    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        'Authorization':f'Bearer {access_token}'
    }

    r = requests.get(artist_url, headers=headers)

    if r.status_code == 200:
        artist_info = r.json()
        return artist_info
    else:
        print(f"Error getting requested artist data: {r.status_code}")
        return None

# Usage example:
if __name__ == '__main__':
    access_token = getAccessToken()

    if access_token:
        artist_id = '3WrFJ7ztbogyGnTHbHJFl2'
        artist_info = getArtistData(artist_id, access_token)

        if artist_info:
            print(f'Artist Name: {artist_info["name"]}')
            print(f'Followers: {artist_info["followers"]["total"]}')
            print(f'Popularity: {artist_info["popularity"]}')
            print(f'Genres: {", ".join(artist_info["genres"])}')