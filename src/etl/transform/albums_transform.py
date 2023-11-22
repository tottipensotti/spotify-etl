## Still work in progress

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
    columns=['id','name', 'artist_id', 'album_type', 'release_date',
    'total_tracks', 'available_markets','disc_number']

    def getArtists(i):
        if len(songs['items'][i]['track']['album']['artists'])>1:
            artist = []
            for a in range(0,len(songs['items'][i]['track']['album']['artists'])):
                artist.append(songs['items'][i]['track']['album']['artists'][a]['name'])
                return artist
        else:
            return songs['items'][i]['track']['album']['artists'][a]['name']
    
    try:
        for i in range(0,len(songs['items'])):
            tracks.append([
                songs['items'][i]['track']['album']['id'],
                songs['items'][i]['track']['album']['name'],
                getArtists(i),
                songs['items'][i]['track']['album']['album_type'],
                songs['items'][i]['track']['album']['release_date'],
                songs['items'][i]['track']['album']['total_tracks'],
                ', '.join(songs['items'][i]['track']['available_markets']),
                songs['items'][i]['track']['album']['disc_number']
            ])
        dm_track = pd.DataFrame(tracks, columns=columns)
        print('Successfuly transformed tracks data')
        return dm_track
    except:
        print('Error while transforming tracks data.')

if __name__ == '__main__':
    transformTrackData(songs)