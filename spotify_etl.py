from pyspark.sql import SparkSession 
from pyspark.sql import SQLContext
from sqlalchemy import create_engine
from datetime import datetime
import datetime
import json
import pandas as pd
import requests
import psycopg2
from sqlalchemy import exc #Handles sqlalchemy errors


#-------------------------------------------------------------------------DATA LOAD START---------------------------------------------------------------------------------------
#LOAD DATA INTO SPOTIFY DATABASE TABLE
def postgre_engine_load(df_spark):
    engine = create_engine('postgresql+psycopg2://', connect_args={'sslmode':'allow'})

    try:
        load_pandas_df = df_spark.toPandas()
        load_pandas_df.to_sql("sql_table", engine, index=False, if_exists='append')
        print('\n* ETL process complete *\n')
    except exc.IntegrityError: 
        print('* Data already exists in the database, terminating ETL process *\n')  
#-------------------------------------------------------------------------DATA LOAD END-----------------------------------------------------------------------------------------

#-------------------------------------------------------------------------DATA EXTRACTION START---------------------------------------------------------------------------------
#SPARK SESSION CREATION/ SPOTIFY API DATA EXTRACTION
if __name__ == '__main__':

    #SPARK SESSION INITIALIZED
    scSpark = SparkSession.builder.appName("Spotify ETL Postgresql").getOrCreate()  
   
    #CONSTANTS 
    ENCODED_CLIENT_ID_CLIENT_SECRET = 'DATA' 
    API_URL = "https://api.spotify.com/v1/me/player/recently-played?after={time}"
    REFRESH_TOKEN = 'DATA'

    #API CREDENTIALS FOR TOKEN REQUEST (RESPONSE 200 MEANS REQUEST ACHIEVED)
    headers = {
        "Authorization": "Basic {client_id_client_secret}".format(client_id_client_secret=ENCODED_CLIENT_ID_CLIENT_SECRET)
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": "{token}".format(token=REFRESH_TOKEN)
    }

    #TOKEN POST REQUEST
    token_post = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    token_data = token_post.json()
    access_token = token_data["access_token"]

    #CONSTRAINTS
    TOKEN = access_token

    #API CREDENTIALS FOR DATA REQUEST
    headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json",
    "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    #TODAY/YESTERDAY CREATION. UNIX MILISECONDS
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1) 
    yesterday_unix = int(yesterday.timestamp() * 1000)

    #REQUEST DATA FROM SPOTIFY API
    #webpage -> https://developer.spotify.com/console/get-recently-played/
    data_request = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix), headers=headers) 

   #MAKE DATA REQUEST JSON FILE
    spotify_data = data_request.json()

    #LISTS
    song_name = []
    artist_name = []
    played_at = []
    time_stamp = []

    #APPEND VALUES FROM JSON TO LIST
    try:
        for i in spotify_data["items"]:
            song_name.append(i["track"]["name"])
            artist_name.append(i["track"]["album"]["artists"][0]["name"])
            played_at.append(i["played_at"])
            time_stamp.append(i["played_at"][0:10])
    except KeyError:
        print('\n* Token has expired. Requesting Refresh *')


    #CREATE A DICTIONARY
    spotify_songs_dictionary = {
    "song_name" : song_name,
    "artist_name" : artist_name,
    "played_at" : played_at,
    "time_stamp" : time_stamp
    }

    #CREATE PANDAS DF
    df_pd =pd.DataFrame(spotify_songs_dictionary, columns = ("song_name", "artist_name", "played_at", "time_stamp"))

#-------------------------------------------------------------------------DATA EXTRACTION END--------------------------------------------------------------------------------------

#-------------------------------------------------------------------------DATA TRANSFORMATION (VALIDATION) START-------------------------------------------------------------------
#DATA VALIDATION
def data_validation(df: pd.DataFrame) -> bool: 
    if df.empty:
        print('\n* No songs were downloaded *\n ')
        return False

    if not pd.Series(df["played_at"]).is_unique:
        print('\n* Primary key check violated. Terminating extraction *\n ')

    #Check for null values
    if df_pd.isnull().values.any():
        raise Exception('\n* Null values found. Terminating extraction *\n ')

    return True

#CREATE SPARK DF
if data_validation(df_pd):
    df_spark = scSpark.createDataFrame(df_pd) 
    df_spark.show(df_spark.count(), False) 
    postgre_engine_load(df_spark)
#-------------------------------------------------------------------------DATA TRANSFORMATION (VALIDATION) END----------------------------------------------------------------------













