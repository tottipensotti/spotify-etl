import requests
from spotipy.oauth2 import SpotifyOAuth

def getRecentlyPlayedTracks(access_token: str) -> dict:
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

def getArtistData(artist_id: str, access_token: str) -> dict:
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