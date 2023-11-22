import pandas as pd
from pandas import DataFrame
import sys
import os
from dotenv import load_dotenv

load_dotenv()
folder_directory = os.getenv("FOLDER_DIRECTORY")
sys.path.insert(1,f'{folder_directory}/src/')
from utils.helper_functions import getAccessToken
from etl.extract.spotify_api import getRecentlyPlayedTracks

access_token = getAccessToken()
songs = getRecentlyPlayedTracks(access_token)

def transformTrackData(songs):
    tracks = []
    columns=['id','name', 'duration_ms', 'popularity', 'album_id',
    'type', 'track_number', 'available_markets','explicit','is_local']
    try:
        for i in range(0,len(songs['items'])):
            tracks.append([
                songs['items'][i]['track']['id'],
                songs['items'][i]['track']['name'],
                songs['items'][i]['track']['duration_ms'],
                songs['items'][i]['track']['popularity'],
                songs['items'][i]['track']['album']['id'],
                songs['items'][i]['track']['type'],
                songs['items'][i]['track']['track_number'],
                ', '.join(songs['items'][i]['track']['available_markets']),
                songs['items'][i]['track']['explicit'],
                songs['items'][i]['track']['is_local']
            ])
        dm_track = pd.DataFrame(tracks, columns=columns)
        print('Successfuly transformed tracks data')
        return dm_track
    except:
        print('Error while transforming tracks data.')

if __name__ == '__main__':
    transformTrackData(songs)