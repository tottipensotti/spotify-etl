from etl.extract.spotify_api import getRecentlyPlayedTracks
from utils.helper_functions import getAccessToken

access_token = getAccessToken()
played_songs = getRecentlyPlayedTracks(access_token)
