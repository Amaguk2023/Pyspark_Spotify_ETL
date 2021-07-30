import requests
import json
from datetime import datetime
import datetime
import extract

def spotify_data_request(ACCESS_TOKEN):

	#API CREDENTIALS FOR DATA REQUEST
	headers = {
		"Accept" : "application/json",
		"Content-Type" : "application/json",
		"Authorization" : "Bearer {token}".format(token=ACCESS_TOKEN)
	}

	#TODAY/YESTERDAY CREATION. UNIX MILISECONDS
	today = datetime.datetime.now()
	yesterday = today - datetime.timedelta(days=1)
	yesterday_unix = int(yesterday.timestamp() * 1000)

	#REQUEST DATA FROM SPOTIFY API
	recently_played_data_request = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix), headers=headers) 

	#MAKE DATA REQUEST JSON FILE
	recently_played_json = recently_played_data_request.json()
	extract.data_extraction(recently_played_json)



