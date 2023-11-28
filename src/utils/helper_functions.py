import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import requests

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
        print(access_info)
        return None
    else:
        access_token = access_info["access_token"]
        return access_token
    
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