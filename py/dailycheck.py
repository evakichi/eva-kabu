import common
import dailyquotes
import weeklyquotes
import monthlyquotes
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

    __daily_xlsx_path = os.path.join(
        common.DATA_DIR, datetime.datetime.today().strftime('%Y-%m-%d')+"-daily.xlsx")
    __weekly_xlsx_path = os.path.join(
        common.DATA_DIR, datetime.datetime.today().strftime('%Y-%m-%d')+"-weekly.xlsx")
    __monthly_xlsx_path = os.path.join(
        common.DATA_DIR, datetime.datetime.today().strftime('%Y-%m-%d')+"-monthly.xlsx")

    __daily_quotes = dailyquotes.DailyQuotes.load('13010')

    __workbook = common.brank_workbook()
    __daily_quotes.write_xslx(__workbook, 1)
    common.save_and_close_workbook(__workbook, __daily_xlsx_path)

    __weekly_quotes = weeklyquotes.WeeklyQuotes.calc(__daily_quotes)

    __workbook = common.brank_workbook()
    __weekly_quotes.write_xslx(__workbook, 1)
    common.save_and_close_workbook(__workbook, __weekly_xlsx_path)

    __monthly_quotes = monthlyquotes.MonthlyQuotes.calc(__daily_quotes)

    __workbook = common.brank_workbook()
    __monthly_quotes.write_xslx(__workbook, 1)
    common.save_and_close_workbook(__workbook, __monthly_xlsx_path)
