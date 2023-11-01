import os
import base64
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

def getAccessToken():
    """
    Retrieves an access token for the Spotify API
    using the user credentials from environment variables.

    Returns:
        str: The access token.
    """

    auth_url = "https://accounts.spotify.com/api/token"
    auth_params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope':'user-read-recently-played'
    }
    
    auth_response = requests.get('https://accounts.spotify.com/authorize', params=auth_params)

    if auth_response.status_code == 200:
        
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
    
def getRecentlyPlayedTracks(access_token):
    """
    Retrieves data about user recently played tracks.

    Args:
        access_token (str): The access token for the Spotify API.

    Returns:
        dict: Information about played tracks.
    """

    played_tracks = 'https://api.spotify.com/v1/me/player/recently-played'
    headers = {
        'Authorization':f'Bearer {access_token}'
    }

    r = requests.get(played_tracks, headers=headers)

    if r.status_code == 200:
        recently_played_data = r.json()
        return recently_played_data
    else:
        print(f'Error: {r.status_code}')

# Usage example:
if __name__ == '__main__':
    access_token = getAccessToken()

    if access_token:
        played_songs = getRecentlyPlayedTracks(access_token)

        if played_songs:
            for item in played_songs['items']:
                track = item['track']
                print(f'Track Name: {track["name"]}')
                print(f'Artist: {", ".join([artist["name"] for artist in track["artists"]])}')
                print(f'Album: {track["album"]["name"]}')
        else:
            print('Error getting recently played tracks')