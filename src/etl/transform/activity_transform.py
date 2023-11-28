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

def transformActivityData(songs):
    activity=[]
    columns=['played_at','track_id','type']
    try:
        for i in range(len(songs['items'])):
            played_at = songs['items'][i]['played_at']
            track_id = songs['items'][i]['track']['id']

            try:
                context_type = songs['items'][i]['context']['type']
            except (KeyError, TypeError):
                context_type = None

            activity.append([played_at, track_id, context_type])

        ft_activity = DataFrame(activity, columns=columns)
        print('Successfully transformed activity data.')
        return ft_activity
    except:
        print('Error while transforming activity data.')


if __name__ == '__main__':
    transformActivityData(songs)