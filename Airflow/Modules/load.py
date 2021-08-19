import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import exc

#LOAD DATA INTO SPOTIFY DATABASE TABLE
def postgre_engine_load(df):
    engine = create_engine('postgresql+psycopg2://', connect_args={'sslmode':'allow'})

    try:
        df.to_sql("spotify_played_tracks", engine, index=False, if_exists='append')
        print('\n* ETL process complete *\n')
    except exc.IntegrityError: 
        print('\n* Spotify Data already exists in the database, terminating ETL process *\n')  