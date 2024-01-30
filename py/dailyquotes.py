import common
import quote
import candlestick

import requests
import json
import os
import glob


class DailyQuotes:

    def store_daily_quotes_data(id_token, brand_data, past_days=-1):

        if common.TEST:
            return

        __headers = {'Authorization': f'Bearer {id_token}'}
        __brand_code = brand_data.code()
        __current_dir = common.create_dir(
            os.path.join(common.DATA_DIR, __brand_code))

        if past_days == -1:
            __daily_quotes_get = requests.get(
                f"https://api.jquants.com/v1/prices/daily_quotes?code={__brand_code}", headers=__headers)
        else:
            __date = common.get_date(past_days).strftime('%Y-%m-%d')
            __daily_quotes_get = requests.get(
                f"https://api.jquants.com/v1/prices/daily_quotes?code={__brand_code}&date={__date}", headers=__headers)

        __daily_quotes_json = __daily_quotes_get.json()

        if 'daily_quotes' in __daily_quotes_json and len(__daily_quotes_json['daily_quotes']) != 0:
            for __daily_quotes in __daily_quotes_json['daily_quotes']:
                __current_date = __daily_quotes['Date']
                __current_file_path = os.path.join(
                    __current_dir, __current_date+".json")
                if not os.path.exists(__current_file_path):
                    with open(__current_file_path, 'w') as _file:
                        json.dump(__daily_quotes, _file)

    def __init__(self, brand) -> None:
        self.__brand = brand
        self.__daily_quotes_list = list()

    def append(self, json_data):
        if json_data['Date'] is None or json_data['Open'] is None or json_data['High'] is None or json_data['Low'] is None or json_data['Close'] is None:
            return None
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

    def re_calc(self):
        for __daily_quotes_index, __daily_quotes in enumerate(self.__daily_quotes_list):
            __daily_quotes.re_set(candlestick.BasicCandleStick.calc(__daily_quotes),
                                  candlestick.AdvancedCandleStick.calc(
                                      __daily_quotes),
                                  candlestick.DetailedCandleStick.calc(__daily_quotes))

    def write_xlsx_header(self, worksheet, row):
        worksheet[f'A{row}'] = 'date'
        worksheet[f'B{row}'] = 'open'
        worksheet[f'C{row}'] = 'high'
        worksheet[f'D{row}'] = 'low'
        worksheet[f'E{row}'] = 'close'

        worksheet[f'F{row}'] = 'basic'
        worksheet[f'G{row}'] = 'advanced'
        worksheet[f'H{row}'] = 'detailed'

    def write_xslx(self, workbook, begin_row):
        worksheet = workbook.create_sheet(title=self.brand().code())
        self.write_xlsx_header(worksheet, begin_row)
        for __daily_quotes_index, __daily_quotes in enumerate(self.__daily_quotes_list, begin_row + 1):
            worksheet[f'A{__daily_quotes_index}'] = __daily_quotes.period()
            worksheet[f'B{__daily_quotes_index}'] = __daily_quotes.open()
            worksheet[f'C{__daily_quotes_index}'] = __daily_quotes.high()
            worksheet[f'D{__daily_quotes_index}'] = __daily_quotes.low()
            worksheet[f'E{__daily_quotes_index}'] = __daily_quotes.close()

            worksheet[f'F{__daily_quotes_index}'] = __daily_quotes.basic_candle_stick(
            ).to_string()
            worksheet[f'G{__daily_quotes_index}'] = __daily_quotes.advanced_candle_stick(
            ).to_string()
            worksheet[f'H{__daily_quotes_index}'] = __daily_quotes.detailed_candle_stick(
            ).to_string()

    def load(brand_data):
        __current_dir = os.path.join(common.DATA_DIR, brand_data.code())
        __json_file_list = sorted(
            glob.glob(__current_dir+'/*.json', recursive=False))
        __daily_quotes = DailyQuotes(brand_data)
        for __quotes_file_index, __quotes_file in enumerate(__json_file_list):
            with open(__quotes_file) as _file:
                __daily_quotes.append(json.load(_file))
        return __daily_quotes
