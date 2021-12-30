import json

import requests


class Authorization:
    """ How to obtain Access Token"""

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.clients_secret = client_secret

    def get_token(self):
        response = requests.post(
            url="https://www.olx.ua/api/open/oauth/token",
            json={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.clients_secret,
                "scope": "v2 read write"
            }
        )
        content = json.loads(response.content.decode())
        access_token = content['access_token']
        return access_token
