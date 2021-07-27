# Pyspark Spotify ETL

***Description:***
 
This a Data Engineer project that extracts data from the user's recently played tracks console using Spotify's API, transforms data and then loads it into Postgresql using SQLAlchemy engine. The ETL job is executed with crontab (midnight) and the data is shown as a Spark Dataframe before loading. Token never expires since an HTTP POST method with Spotify's token API is used in the beginning of the script. 

***Essentials:***

- Extra libraries that must be imported: sys, json, datetime.

***ETL Execution:***

- Install all the necessary libraries from the Pipfile.
- Read the "Token_request_instructions" to get your own refresh token. In case you don't want that you can get one from this website "https://developer.spotify.com/console/get-recently-played/"	which will have to be requested every hour. 
- Add your you postgreSQL credentials for the engine creation. In case you'll be using another RDBMS, search in this website "https://docs.sqlalchemy.org/en/14/core/engines.html" the engine that fits you. 
- Create SQL Database/Table (Optional).
- Create .sh file.
- Create crontab or use the existing one if you want the job to run on midnight every day. 

**Extras**

- To verify that your scheduled job is running, change the crontab time to "* * * * *"
- In case you don't want your scope to be "recently played tracks", check this list "https://developer.spotify.com/documentation/general/guides/scopes/"