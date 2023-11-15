import pandas as pd
from etl.extract.spotify_api import getRecentlyPlayedTracks
from utils.helper_functions import getAccessToken

access_token = getAccessToken()
played_songs = getRecentlyPlayedTracks(access_token)


### Create the ft_activity dataframe with columns: played_at, client_id, track_id
# def activity():

### Create the dm_tracks table with: id, name, duration_ms, popularity, album_id, type, track_number, available_markets, explicit, is_local
# def tracks():

### Create the dm_album table with: id, name, artist_id, album_type, release_date, total_tracks, available_markets, disc_number
# def albums():

### Create the dm_artist table with: id, name, type