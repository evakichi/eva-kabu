import common
import os
import requests
import json

class TradingCalendar:

    def __init__(self) -> None:
        pass

    def dump(id_token):
        __calender_data_path = os.path.join(
            common.create_dir(common.CALENDAR_DIR), common.curren_date()+".json")

        __headers = {'Authorization': 'Bearer {}'.format(id_token)}
        __information_get = requests.get(
            f"https://api.jquants.com/v1/markets/trading_calendar", headers=__headers)
        with open(__calender_data_path, 'wt') as __file:
            json.dump(__information_get.json(), __file)

