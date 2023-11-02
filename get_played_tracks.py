import os
import base64
import requests
from dotenv import load_dotenv
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
scope = 'user-read-recently-played'

def getAccessToken():
    """
    Retrieves an access token for the Spotify API
    using Spotipy to the OAuth2.0 with user credentials from environment variables.

    Returns:
        str: The access token.
    """
    spotify_auth = SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope=scope)
    
    access_info = spotify_auth.get_cached_token()

    if access_info is None:
        print("No access token found.")
        return None
    else:
        access_token = access_info["access_token"]
        return access_token

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
            print('Success getting recently played tracks')
        else:
            print('Error getting recently played tracks')