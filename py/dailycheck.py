import common
import tokentaker
import brand
import os
import requests
import json


class DailyCheck:

    def __init__(self, debug=False) -> None:

        self.mail = os.environ.get('J_QUANTS_MAIL_ADDRESS')
        self.passwd = os.environ.get('J_QUANTS_PASSWD')
        self.debug = debug

    def get_token(self):
        self.token_taker = tokentaker.Token(self.mail, self.passwd, self.debug)
        self.id_token = self.token_taker.get_tokens()
        if self.debug:
            print(f'token:{self.id_token}')

    def get_brand_data(self):
        self.brand_data_list = [brand.Brand(
            info) for info in brand.Brand.get_brand_info(self.id_token)]
        if self.debug:
            for brand_data in self.brand_data_list:
                print(brand_data)


def daily_check(id_token, brand_data, past_days=-1, debug=False):

    headers = {'Authorization': f'Bearer {id_token}'}
    brand_code = brand_data.getCode()
    current_path = common.create_dir(common.DATA_DIR)

    if past_days == -1:
        dailyQuotesGet = requests.get(
            f"https://api.jquants.com/v1/prices/daily_quotes?code={brand_code}", headers=headers)
    else:
        date = common.get_date().strftime('%Y-%m-%d')
        dailyQuotesGet = requests.get(
            f"https://api.jquants.com/v1/prices/daily_quotes?code={brand_code}&date={date}", headers=headers)

    dailyQuotesJson = dailyQuotesGet.json()

    if 'daily_quotes' in dailyQuotesJson and len(dailyQuotesJson['daily_quotes']) != 0:
        for dailyQuote in dailyQuotesJson['daily_quotes']:
            current = dailyQuote['Date']
            currentFilePath = os.path.join(current_path, current+".json")
            if not os.path.exists(currentFilePath):
                with open(currentFilePath, 'w') as f:
                    json.dump(dailyQuote, f)


if __name__ == '__main__':

    daily_check = DailyCheck(debug=True)
    daily_check.get_token()
    daily_check.get_brand_data()
