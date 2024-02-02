import common
import quoteslist
import quote

import openpyxl


class WeeklyQuotes(quoteslist.QuoteList):

    def __init__(self, brand) -> None:
        super().__init__(brand)

    def calc(daily_quotes):
        __period = '1900-01'
        __brand = daily_quotes.brand()
        __weekly_quotes = WeeklyQuotes(__brand)
        __last_index = len(daily_quotes.list()) - 1

        for __quotes_index, __quotes in enumerate(daily_quotes.list()):
            __quotes_period = common.year_week_number(__quotes.period())
            if __quotes_index == 0:
                __period = __quotes_period
                __open = __quotes.open()
                __high = __quotes.high()
                __low = __quotes.low()
                __volume = __quotes.volume()

            if __period != __quotes_period:
                __weekly_quotes.append(
                    __period, __open, __high, __low, __close, __volume)
                __period = __quotes_period
                __open = __quotes.open()
                __high = __quotes.high()
                __low = __quotes.low()
                __volume = __quotes.volume()

            if __period == __quotes_period:
                __high = max(__high, __quotes.high())
                __low = min(__low, __quotes.low())
                __volume += __quotes.volume()
                __close = __quotes.close()

            if __quotes_index == __last_index:
                __high = max(__high, __quotes.high())
                __low = min(__low, __quotes.low())
                __volume += __quotes.volume()
                __close = __quotes.close()
                __weekly_quotes.append(
                    __period, __open, __high, __low, __close, __volume)

        return __weekly_quotes
