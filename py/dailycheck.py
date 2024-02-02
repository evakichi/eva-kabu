import common
import dailyquotes
import weeklyquotes
import monthlyquotes
import tokentaker
import brand

import os
import math
import datetime
from multiprocessing import Process


def calc(brand_data, count):
    if common.TEST and count > common.NUM_OF_THREADS:
        return

    common.create_dir(os.path.join(common.XLSX_DIR, brand_data.code()))

    __xlsx_path = os.path.join(
        common.XLSX_DIR, brand_data.code(), datetime.datetime.today().strftime('%Y-%m-%d')+".xlsx")

    __workbook = common.brank_workbook()

    __daily_quotes = dailyquotes.DailyQuotes.load(brand_data)
    __daily_quotes.write_xslx(__workbook,brand_data.code(), 1)

    __weekly_quotes = weeklyquotes.WeeklyQuotes.calc(__daily_quotes)
    __weekly_quotes.write_xslx(__workbook,brand_data.code(), 1)

    __monthly_quotes = monthlyquotes.MonthlyQuotes.calc(__daily_quotes)
    __monthly_quotes.write_xslx(__workbook,brand_data.code(), 1)

    common.save_and_close_workbook(__workbook, __xlsx_path)
    print(f'{brand_data.code()} is converted!')

if __name__ == '__main__':

    __token_taker = tokentaker.TokenTaker()
    __token = __token_taker.get_token()

    __brand_data_list = brand.Brand.get_brand_data_list(__token)

    __brand_data_length = len(__brand_data_list)
    __outerloop_count = math.floor(__brand_data_length / common.NUM_OF_THREADS)
    __last_innerloop_count = __brand_data_length % common.NUM_OF_THREADS

    for __outerloop_index in range(__outerloop_count):
        __process_list = list()
        for __innerloop_index in range(common.NUM_OF_THREADS):
            __count = __outerloop_index * common.NUM_OF_THREADS + __innerloop_index
            __brand_data = __brand_data_list[__count]
            __process_list.append(Process(
                target=dailyquotes.DailyQuotes.store_daily_quotes_data, args=(__token, __brand_data, 1)))
        for n in range(common.NUM_OF_THREADS):
            __process_list[n].start()
        for n in range(common.NUM_OF_THREADS):
            __process_list[n].join()

    __process_list = list()
    for __innerloop_index in range(__last_innerloop_count):
        __count = __outerloop_index * common.NUM_OF_THREADS + __innerloop_index
        __brand_data = __brand_data_list[__count]
        __process_list.append(Process(
            target=dailyquotes.DailyQuotes.store_daily_quotes_data, args=(__token, __brand_data, 1)))
    for n in range(__last_innerloop_count):
        __process_list[n].start()
    for n in range(__last_innerloop_count):
        __process_list[n].join()

    for __outerloop_index in range(__outerloop_count):
        __process_list = list()
        for __innerloop_index in range(common.NUM_OF_THREADS):
            __count = __outerloop_index * common.NUM_OF_THREADS + __innerloop_index
            __brand_data = __brand_data_list[__count]
            __process_list.append(
                Process(target=calc, args=(__brand_data, __count)))
        for n in range(common.NUM_OF_THREADS):
            __process_list[n].start()
        for n in range(common.NUM_OF_THREADS):
            __process_list[n].join()

    __process_list = list()
    for __innerloop_index in range(__last_innerloop_count):
        __count = __outerloop_index * common.NUM_OF_THREADS + __innerloop_index
        __brand_data = __brand_data_list[__count]
        __process_list.append(
            Process(target=calc, args=(__brand_data, __count)))
    for n in range(__last_innerloop_count):
        __process_list[n].start()
    for n in range(__last_innerloop_count):
        __process_list[n].join()
