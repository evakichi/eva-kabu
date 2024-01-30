import common
import dailyquotes
import weeklyquotes
import openpyxl
import os
import datetime


class DailyCheck:

    def __init__(self) -> None:
        pass


if __name__ == '__main__':

    daily_check = DailyCheck()
    # _token_taker = tokentaker.TokenTaker()
    # _token = _token_taker.get_token()
    # _brand_data_list = brand.Brand.get_brand_data_list(_token)
    # dailyquotes.DailyQuotes.store_daily_quant_data(_token,_brand_data_list[0],-1)

    __daily_quotes = dailyquotes.DailyQuotes.load('13010')

    __daily_xlsx_path = os.path.join(
        common.DATA_DIR, datetime.datetime.today().strftime('%Y-%m-%d')+"-daily.xlsx")
    __workbook = openpyxl.Workbook()
    __worksheet = __workbook['Sheet']
    __workbook.remove(__worksheet)

    __daily_quotes.write_xslx(__workbook,1)

    __workbook.save(__daily_xlsx_path)
    __workbook.close()

    __weekly_quotes = weeklyquotes.WeeklyQuotes.calc(__daily_quotes)

    __weekly_xlsx_path = os.path.join(
        common.DATA_DIR, datetime.datetime.today().strftime('%Y-%m-%d')+"-weekly.xlsx")
    __workbook = openpyxl.Workbook()
    __worksheet = __workbook['Sheet']
    __workbook.remove(__worksheet)

    __weekly_quotes.write_xslx(__workbook,1)

    __workbook.save(__weekly_xlsx_path)
    __workbook.close()
