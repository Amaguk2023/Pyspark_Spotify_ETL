# Pyspark Spotify ETL

***Description:***
 
This is my first Data Engineering project, it extracts data from the user's recent played tracks using Spotify's API, transforms data and then loads it into Postgresql using SQLAlchemy engine. Data is shown as a Spark Dataframe before loading and The ETL job is scheduled with crontab. Token never expires since an HTTP POST method with Spotify's token API is used in the beginning of the script. 

***Essentials:***

- Extra libraries that must be imported: sys, json, datetime.

***ETL Execution:***

- Install all the necessary libraries from the Pipfile.
- Read the "Token_request_instructions" to get your own refresh token. In case you don't want that you can get one from this website https://developer.spotify.com/console/get-recently-played/ which will have to be requested every hour. 
- Add your you postgreSQL credentials for the engine creation. In case you'll be using another RDBMS, use this website https://docs.sqlalchemy.org/en/14/core/engines.html.
- Create SQL Database/Table (Optional).
- Create .sh file.
- Create a new crontab or use the existing one if you want the job to run on midnight every day. 

**Extras**

- To verify that your scheduled job is running you can change the crontab to "* * * * *".
- Here is the website https://developer.spotify.com/documentation/general/guides/scopes/ with other scopes in case you don't want to use "recently played tracks".