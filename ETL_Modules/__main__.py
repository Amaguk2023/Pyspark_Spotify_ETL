import requests
import data_request

if __name__ == '__main__':

    ENCODED_CLIENT_ID_CLIENT_SECRET = 'MWRhNzkxYjA3MjkyNDU5NmFhMDIwZGE2Mjc5M2MzZDM6NWY4ZmQyMGM4NmViNDQ1ZWExODVkYjM1NDAyNzVmZTY='
    TOKEN_URL = 'https://accounts.spotify.com/api/token'
    REFRESH_TOKEN = 'AQBYXIOttnhSQ9E-NIE5dG0snrxmi0UX_0iID7fvngQERMaHqtTQuK2X-78sjdqFXGlDay-Ku8pQ_RU5GoAHt6TAUfYc2D5sriV4xNhliJZKhbcdYAUQrsPEW7jauFvceUc'

    #API CREDENTIALS FOR TOKEN REQUEST (RESPONSE 200 MEANS REQUEST ACHIEVED)
    headers = {
        "Authorization": "Basic {client_id_client_secret}".format(client_id_client_secret=ENCODED_CLIENT_ID_CLIENT_SECRET)
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": "{token}".format(token=REFRESH_TOKEN)
    }

    #TOKEN POST REQUEST
    token_post = requests.post(TOKEN_URL, headers=headers, data=data)
    token_data = token_post.json()
    access_token = token_data["access_token"]

    #CONSTRAINTS
    ACCESS_TOKEN = access_token
    data_request.spotify_data_request(ACCESS_TOKEN)