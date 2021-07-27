# Pyspark Spotify ETL

***Description:***
 
This a Data Engineer project that extracts data from the user's recently played tracks console using Spotify's API, transforms data and then loads it into Postgresql using SQLAlchemy engine. The ETL job is executed with crontab on midnight and the data is shown as a Spark Dataframe before loading. Access Token never expires since an HTTP POST method with Spotify's token API is used in the beginning of the script. 

***Essentials:***
- Extra libraries that must be imported: sys, json, datetime.

***ETL Execution:***

- Install all the necessary libraries from the Pipfile.
- Read the Token_request_instructions to create your refresh token or in case you don't want that you can get one from this website "https://developer.spotify.com/console/get-recently-played/"	which will have to be requested every hour. 
- Add your you postgreSQL credentials or in case you'll be using another one search in this website "https://docs.sqlalchemy.org/en/14/core/engines.html" the engine that fits you. 
- Create your database and table in your SQL Server in case you don't have none.
- Create .sh file.
- Create crontab or use the existing one in case you want the job to run on midnight every day. 