import requests
import os
import json


class Token:

    def __init__(self, mail, passwd, debug=False) -> None:
        self.mail = mail
        self.passwd = passwd
        self.debug = debug

    def get_tokens(self) -> str:

        data = {"mailaddress": self.mail, "password": self.passwd}
        refresh_token_post = requests.post(
            "https://api.jquants.com/v1/token/auth_user", data=json.dumps(data))
        refresh_token = refresh_token_post.json()['refreshToken']

        id_token_post = requests.post(
            f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={refresh_token}")
        id_token = id_token_post.json()['idToken']
        if self.debug:
            print(self.mail, id_token)
        return id_token
