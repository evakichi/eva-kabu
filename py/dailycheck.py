import common
import dailyquotes
import weeklyquotes
import monthlyquotes
import tokentaker
import brand
import candlestick
import os
import datetime


if __name__ == '__main__':

    __token_taker = tokentaker.TokenTaker()
    __token = __token_taker.get_token()
    __brand_data_list = brand.Brand.get_brand_data_list(__token)
    for __brand_data_index, __brand_data in enumerate(__brand_data_list):
        if common.TEST and __brand_data_index > 0:
            break
        dailyquotes.DailyQuotes.store_daily_quotes_data(
            __token, __brand_data_list, 1)

    __daily_xlsx_path = os.path.join(
        common.DATA_DIR, datetime.datetime.today().strftime('%Y-%m-%d')+"-daily.xlsx")
    __weekly_xlsx_path = os.path.join(
        common.DATA_DIR, datetime.datetime.today().strftime('%Y-%m-%d')+"-weekly.xlsx")
    __monthly_xlsx_path = os.path.join(
        common.DATA_DIR, datetime.datetime.today().strftime('%Y-%m-%d')+"-monthly.xlsx")

    __daily_quotes_list = list()
    for __brand_data_index, __brand_data in enumerate(__brand_data_list):
        if common.TEST and __brand_data_index > 0:
            break
        __daily_quotes_list.append(dailyquotes.DailyQuotes.load(__brand_data))

    for __daily_quotes_index, __daily_quotes in enumerate(__daily_quotes_list):
        __daily_quotes.re_calc()

    __workbook = common.brank_workbook()
    for __daily_quotes_index, __daily_quotes in enumerate(__daily_quotes_list):
        __daily_quotes.write_xslx(__workbook, 1)
    common.save_and_close_workbook(__workbook, __daily_xlsx_path)

    __weekly_quotes_list = list()
    for __daily_quotes_index, __daily_quotes in enumerate(__daily_quotes_list):
        __weekly_quotes_list.append(
            weeklyquotes.WeeklyQuotes.calc(__daily_quotes))

    for __weekly_quotes_index, __weekly_quotes in enumerate(__weekly_quotes_list):
        __weekly_quotes.re_calc()

    __workbook = common.brank_workbook()
    for __weekly_quotes_index, __weekly_quotes in enumerate(__weekly_quotes_list):
        __weekly_quotes.write_xslx(__workbook, 1)
    common.save_and_close_workbook(__workbook, __weekly_xlsx_path)

    __monthly_quotes_list = list()
    for __daily_quotes_index, __daily_quotes in enumerate(__daily_quotes_list):
        __monthly_quotes_list.append(
            weeklyquotes.WeeklyQuotes.calc(__daily_quotes))

    for __monthly_quotes_index, __monthly_quotes in enumerate(__monthly_quotes_list):
        __monthly_quotes.re_calc()

    __workbook = common.brank_workbook()
    for __monthly_quotes_index, __monthly_quotes in enumerate(__monthly_quotes_list):
        __monthly_quotes.write_xslx(__workbook, 1)
    common.save_and_close_workbook(__workbook, __monthly_xlsx_path)
