import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
scope = 'user-read-recently-played'

def getAccessToken() -> str:
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
    
    access_info = spotify_auth.get_access_token()

    if access_info is None:
        print(access_info)
        return None
    else:
        access_token = access_info["access_token"]
        return access_token