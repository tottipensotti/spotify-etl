import requests
from spotipy.oauth2 import SpotifyOAuth

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