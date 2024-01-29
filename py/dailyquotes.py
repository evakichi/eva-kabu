import common
import quote

import requests
import json
import os
import glob


class DailyQuotes:

    def store_daily_quotes_data(id_token, brand_data, past_days=-1):
        _headers = {'Authorization': f'Bearer {id_token}'}
        _brand_code = brand_data.getCode()
        _current_dir = common.create_dir(os.path.join(common.DATA_DIR,_brand_code))

        if past_days == -1:
            _daily_quotes_get = requests.get(
                f"https://api.jquants.com/v1/prices/daily_quotes?code={_brand_code}", headers=_headers)
        else:
            date = common.get_date().strftime('%Y-%m-%d')
            _daily_quotes_get = requests.get(
                f"https://api.jquants.com/v1/prices/daily_quotes?code={_brand_code}&date={date}", headers=_headers)

        _daily_quotes_json = _daily_quotes_get.json()

        if 'daily_quotes' in _daily_quotes_json and len(_daily_quotes_json['daily_quotes']) != 0:
            for _daily_quotes in _daily_quotes_json['daily_quotes']:
                _current_date = _daily_quotes['Date']
                _current_file_path = os.path.join(
                    _current_dir, _current_date+".json")
                if not os.path.exists(_current_file_path):
                    with open(_current_file_path, 'w') as _file:
                        json.dump(_daily_quotes, _file)

    def __init__(self,brand_data) -> None:
        self.__brand_data = brand_data
        self.__list=list()
    
    def append(self,json_data):

        __date              = json_data['Date']
        __open  = float(json_data['Open'])
        __high  = float(json_data['High'])
        __low   = float(json_data['Low'])
        __close = float(json_data['Close'])

        self.__list.append(quote.Quote(__date,__open,__high,__low,__close))

    def get_daily_quotes_data_list(brand_data):
        __current_dir = os.path.join(common.DATA_DIR,brand_data)
        __quotes_file_list = sorted(glob.glob(__current_dir+'/*.json',recursive=False))

        __daily_quotes = DailyQuotes(brand_data)
        for _quotes_gile_index,_quotes_file in enumerate(__quotes_file_list):
            with open(_quotes_file,'rt') as _file:
                __daily_quotes.append()