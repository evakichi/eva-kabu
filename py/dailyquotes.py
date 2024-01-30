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
        _current_dir = common.create_dir(
            os.path.join(common.DATA_DIR, _brand_code))

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

    def __init__(self, brand) -> None:
        self.__brand = brand
        self.__daily_quotes_list = list()

    def append(self, json_data):
        if json_data['Date'] is None or json_data['Open'] is None or json_data['High'] is None or json_data['Low'] is None or json_data['Close'] is None:
            return None
        print(json_data['Date'])
        __date = json_data['Date']
        __open = float(json_data['Open'])
        __high = float(json_data['High'])
        __low = float(json_data['Low'])
        __close = float(json_data['Close'])

        self.__daily_quotes_list.append(quote.Quote(
            __date, __open, __high, __low, __close))

    def brand(self):
        return self.__brand

    def list(self):
        return self.__daily_quotes_list

    def write_xlsx_header(self, worksheet, row):
        worksheet[f'A{row}'] = 'date'
        worksheet[f'B{row}'] = 'open'
        worksheet[f'C{row}'] = 'high'
        worksheet[f'D{row}'] = 'low'
        worksheet[f'E{row}'] = 'close'

    def write_xslx(self, workbook, begin_row):
        worksheet = workbook.create_sheet(title=self.brand())
        self.write_xlsx_header(worksheet, begin_row)
        for __daily_quotes_index, __daily_quotes in enumerate(self.__daily_quotes_list, begin_row + 1):
            worksheet[f'A{__daily_quotes_index}'] = __daily_quotes.period()
            worksheet[f'B{__daily_quotes_index}'] = __daily_quotes.open()
            worksheet[f'C{__daily_quotes_index}'] = __daily_quotes.high()
            worksheet[f'D{__daily_quotes_index}'] = __daily_quotes.low()
            worksheet[f'E{__daily_quotes_index}'] = __daily_quotes.close()

    def load(brand_data):
        __current_dir = os.path.join(common.DATA_DIR, brand_data)
        __json_file_list = sorted(
            glob.glob(__current_dir+'/*.json', recursive=False))

        __daily_quotes = DailyQuotes(brand_data)
        for __quotes_file_index, __quotes_file in enumerate(__json_file_list):
            with open(__quotes_file) as _file:
                __daily_quotes.append(json.load(_file))
        return __daily_quotes
