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
        print(f'{self.getDate()}:{self.getCode()}:{self.getCompanyName()}({self.getCompanyNameEnglish()}):', end="")
        print(f'{self.getSector17CodeName()}({self.getSector17Code()}):{self.getSector33CodeName()}({self.getSector33Code()}):', end="")
        print(
            f'{self.getScaleCategory()}:{self.getMarketCodeName()}({self.getMarketCode()}):')

    def getDate(self):
        return self.__date

    def getCode(self):
        return self.__brand_code

    def getCompanyName(self):
        return self.__company_name

    def getCompanyNameEnglish(self):
        return self.__company_name_english

    def getSector17Code(self):
        return self.__sector17_code

    def getSector17CodeName(self):
        return self.__sector17_code_name

    def getSector33Code(self):
        return self.__sector33_code

    def getSector33CodeName(self):
        return self.__sector33_code_name

    def getScaleCategory(self):
        return self.__scale_category

    def getMarketCode(self):
        return self.__market_code

    def getMarketCodeName(self):
        return self.__market_code_name
