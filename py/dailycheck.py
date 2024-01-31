import common
import dailyquotes
import weeklyquotes
import monthlyquotes
import tokentaker
import brand
import os
import datetime


if __name__ == '__main__':

    __token_taker = tokentaker.TokenTaker()
    __token = __token_taker.get_token()
    __brand_data_list = brand.Brand.get_brand_data_list(__token)
    for __brand_data_index, __brand_data in enumerate(__brand_data_list):
        if common.TEST and __brand_data_index > 0:
            break
        if common.DEBUG_LEVEL > 0:
            print (f'{__brand_data.code()}')
            dailyquotes.DailyQuotes.store_daily_quotes_data(
                __token, __brand_data, -1)

    for __brand_data_index, __brand_data in enumerate(__brand_data_list):
        if common.TEST and __brand_data_index > 0:
            break

        __daily_quotes = dailyquotes.DailyQuotes.load(__brand_data)
        __daily_quotes.re_calc()

        __workbook = common.brank_workbook()
        __daily_quotes.write_xslx(__workbook, 1)

        __daily_xlsx_path = os.path.join(
            common.XLSX_DIR, __brand_data.code(), datetime.datetime.today().strftime('%Y-%m-%d')+"-daily.xlsx")
        common.save_and_close_workbook(__workbook, __daily_xlsx_path)

        __weekly_quotes = weeklyquotes.WeeklyQuotes.calc(__daily_quotes)
        __weekly_quotes.re_calc()

        __workbook = common.brank_workbook()
        __weekly_quotes.write_xslx(__workbook, 1)

        __weekly_xlsx_path = os.path.join(
            common.XLSX_DIR, __brand_data.code(), datetime.datetime.today().strftime('%Y-%m-%d')+"-weekly.xlsx")
        common.save_and_close_workbook(__workbook, __weekly_xlsx_path)

        __monthly_quotes = weeklyquotes.WeeklyQuotes.calc(__daily_quotes)
        __monthly_quotes.re_calc()

        __workbook = common.brank_workbook()
        __monthly_quotes.write_xslx(__workbook, 1)

        __monthly_xlsx_path = os.path.join(
            common.XLSX_DIR, __brand_data.code(), datetime.datetime.today().strftime('%Y-%m-%d')+"-monthly.xlsx")
        common.save_and_close_workbook(__workbook, __monthly_xlsx_path)
