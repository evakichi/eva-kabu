import common
import dailyquotes
import tokentaker
import brand
import tradingcalendar

import math
from multiprocessing import Process



if __name__ == '__main__':

    __token_taker = tokentaker.TokenTaker()
    __token = __token_taker.get_token()

    __brand_data_list = brand.Brand.get_brand_data_list(__token)
    tradingcalendar.TradingCalendar.dump(__token)
    
    __brand_data_length = len(__brand_data_list)
    __outerloop_count = math.floor(__brand_data_length / common.NUM_OF_THREADS)
    __last_innerloop_count = __brand_data_length % common.NUM_OF_THREADS

    for __outerloop_index in range(__outerloop_count):
        __process_list = list()
        for __innerloop_index in range(common.NUM_OF_THREADS):
            __count = __outerloop_index * common.NUM_OF_THREADS + __innerloop_index
            __brand_data = __brand_data_list[__count]
            __process_list.append(Process(
                target=dailyquotes.DailyQuotes.store_daily_quotes_data, args=(__token, __brand_data,5)))
        for n in range(common.NUM_OF_THREADS):
            __process_list[n].start()
        for n in range(common.NUM_OF_THREADS):
            __process_list[n].join()

    __process_list = list()
    for __innerloop_index in range(__last_innerloop_count):
        __count = __outerloop_index * common.NUM_OF_THREADS + __innerloop_index
        __brand_data = __brand_data_list[__count]
        __process_list.append(Process(
            target=dailyquotes.DailyQuotes.store_daily_quotes_data, args=(__token, __brand_data, 5)))
    for n in range(__last_innerloop_count):
        __process_list[n].start()
    for n in range(__last_innerloop_count):
        __process_list[n].join()
