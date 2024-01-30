import common
import requests


class Brand:

    __date = ""
    __brand_code = 0
    __company_name = ""
    __company_name_english = ""
    __sector17_code = ""
    __sector17_code_name = ""
    __sector33_code = ""
    __sector33_code_name = ""
    __scale_category = ""
    __market_code = ""
    __market_code_name = ""

    def get_brand_data_list(id_token):
        _brand_data_list = [Brand(
            info) for info in Brand.get_brand_info(id_token)]
        if common.DEBUG_LEVEL > 0:
            for _brand_data in _brand_data_list:
                _brand_data.print()
        return _brand_data_list

    def get_brand_info(id_token):
        _headers = {'Authorization': 'Bearer {}'.format(id_token)}
        _information_get = requests.get(
            f"https://api.jquants.com/v1/listed/info", headers=_headers)
        return _information_get.json()['info']

    def __init__(self, data) -> None:
        self.__date = data['Date']
        self.__brand_code = data['Code']
        self.__company_name = data['CompanyName']
        self.__company_name_english = data['CompanyNameEnglish']
        self.__sector17_code = data['Sector17Code']
        self.__sector17_code_name = data['Sector17CodeName']
        self.__sector33_code = data['Sector33Code']
        self.__sector33_code_name = data['Sector33CodeName']
        self.__scale_category = data['ScaleCategory']
        self.__market_code = data['MarketCode']
        self.__market_code_name = data['MarketCodeName']
        pass

    def print(self):
        print(f'{self.get_date()}:{self.get_code()}:{self.get_company_name()}({self.get_company_name_english()}):', end="")
        print(f'{self.get_sector17code_name()}({self.get_sector17code()}):{self.get_sector33code_name()}({self.get_sector33code()}):', end="")
        print(
            f'{self.get_scale_category()}:{self.get_marketcode_name()}({self.get_marketcode()}):')

    def get_date(self):
        return self.__date

    def get_code(self):
        return self.__brand_code

    def get_company_name(self):
        return self.__company_name

    def get_company_name_english(self):
        return self.__company_name_english

    def get_sector17code(self):
        return self.__sector17_code

    def get_sector17code_name(self):
        return self.__sector17_code_name

    def get_sector33code(self):
        return self.__sector33_code

    def get_sector33code_name(self):
        return self.__sector33_code_name

    def get_scale_category(self):
        return self.__scale_category

    def get_marketcode(self):
        return self.__market_code

    def get_marketcode_name(self):
        return self.__market_code_name
