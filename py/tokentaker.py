import common
import requests
import os
import json


class TokenTaker:

    def __init__(self) -> None:
        self.__mail = os.environ.get('J_QUANTS_MAIL_ADDRESS')
        self.__passwd = os.environ.get('J_QUANTS_PASSWD')

    def get_token(self) -> str:

        if common.TEST:
            print(self.__mail, 'dummy')
            return 'dummy'

        __data = {"mailaddress": self.__mail, "password": self.__passwd}
        __refresh_token_post = requests.post(
            "https://api.jquants.com/v1/token/auth_user", data=json.dumps(__data))
        __refresh_token = __refresh_token_post.json()['refreshToken']

        __id_token_post = requests.post(
            f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={__refresh_token}")
        __id_token = __id_token_post.json()['idToken']
        if common.DEBUG_LEVEL > 0:
            print(self.__mail, __id_token)
        return __id_token
