from pandas import DataFrame
import sys
import os
from dotenv import load_dotenv

load_dotenv()
folder_directory = os.getenv("FOLDER_DIRECTORY")
sys.path.insert(1,f'{folder_directory}/src/')
from utils.helper_functions import getAccessToken, getArtistData
from etl.extract.spotify_api import getRecentlyPlayedTracks

access_token = getAccessToken()
songs = getRecentlyPlayedTracks(access_token)

def transformArtistData(songs):
    artists_ids = set()
    columns = ['id', 'name', 'type','genres','popularity']

    try:
        """
        Transformations for each unique id.
        Validation because some albums/tracks can have +1 artist
        """
        artists = []
        for i in range(0, len(songs['items'])):
            for a in range(0, len(songs['items'][i]['track']['artists'])):
                artist_id = songs['items'][i]['track']['artists'][a]['id']
                if artist_id not in artists_ids:
                    artists_ids.add(artist_id)
                    artist_info = getArtistData(artist_id, access_token)
                    artists.append([
                        artist_info['id'],
                        artist_info['name'],
                        artist_info['type'],
                        artist_info['genres'],
                        artist_info['popularity'],
                    ])
                else:
                    pass
        dm_artist = DataFrame(artists, columns=columns)
        print('Successfully transformed artists data')
        return dm_artist
    except Exception as e:
        print(f'Error while transforming artists data at: {i}:{e}')

if __name__ == '__main__':
    transformArtistData(songs)