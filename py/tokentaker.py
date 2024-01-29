import common
import requests
import os
import json


class TokenTaker:

    def __init__(self) -> None:
        self._mail = os.environ.get('J_QUANTS_MAIL_ADDRESS')
        self._passwd = os.environ.get('J_QUANTS_PASSWD')

    def get_token(self) -> str:

        _data = {"mailaddress": self._mail, "password": self._passwd}
        _refresh_token_post = requests.post(
            "https://api.jquants.com/v1/token/auth_user", data=json.dumps(_data))
        _refresh_token = _refresh_token_post.json()['refreshToken']

        _id_token_post = requests.post(
            f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={_refresh_token}")
        _id_token = _id_token_post.json()['idToken']
        if common.DEBUG_LEVEL > 0:
            print(self._mail, _id_token)
        return _id_token
