import pandas as pd 
from Spotify_ETL_Modules import transform
from Spotify_ETL_Modules import load


def info_extraction(recently_played_json):
    song_name = []
    artist_name = []
    played_at = []
    time_stamp = []

    for i in recently_played_json["items"]:
        song_name.append(i["track"]["name"])
        artist_name.append(i["track"]["album"]["artists"][0]["name"])
        played_at.append(i["played_at"])
        time_stamp.append(i["played_at"][0:10])


    spotify_songs_dictionary = {
    "song_name" : song_name,
    "artist_name" : artist_name,
    "played_at" : played_at,
    "time_stamp" : time_stamp
    }

    df = pd.DataFrame(spotify_songs_dictionary, columns = ("song_name", "artist_name", "played_at", "time_stamp"))
    #CREATE SPARK DF

    if transform.data_validation(df):
        load.postgre_engine_load(df)







