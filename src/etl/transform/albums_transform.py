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
    'total_tracks', 'available_markets','type']

    def getArtists(album):
        if len(album['artists']) > 1:
            return ', '.join([artist['name'] for artist in album['artists']])
        else:
            return album['artists'][0]['name']
    
    try:
        for i in range(0, len(songs['items'])):
            tracks.append([
                songs['items'][i]['track']['album']['id'],
                songs['items'][i]['track']['album']['name'],
                getArtists(songs['items'][i]['track']['album']),
                songs['items'][i]['track']['album']['album_type'],
                songs['items'][i]['track']['album']['release_date'],
                songs['items'][i]['track']['album']['total_tracks'],
                ', '.join(songs['items'][i]['track']['available_markets']),
                songs['items'][i]['track']['album']['type']
            ])
        
        dm_track = DataFrame(tracks, columns=columns)
        print('Successfully transformed tracks data')
        return dm_track
    
    except Exception as e:
        print(f'Error while transforming tracks data: {i}:{e}')

if __name__ == '__main__':
    transformTrackData(songs)
