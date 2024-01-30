import common
import quote
import dailyquotes


class WeeklyQuotes:

    def __init__(self, brand) -> None:
        self.__brand = brand
        self.__weekly_quotes_list = list()

    def append(self, period, open, high, low, close):
        self.__weekly_quotes_list.append(
            quote.Quote(period, open, high, low, close))

    def brand(self):
        return self.__brand

    def list(self):
        return self.__weekly_quotes_list

    def write_xlsx_header(self, worksheet, row):
        worksheet[f'A{row}'] = 'week'
        worksheet[f'B{row}'] = 'open'
        worksheet[f'C{row}'] = 'high'
        worksheet[f'D{row}'] = 'low'
        worksheet[f'E{row}'] = 'close'

    def write_xslx(self, workbook, begin_row):
        worksheet = workbook.create_sheet(title=self.brand())
        self.write_xlsx_header(worksheet, begin_row)
        for __weekly_quotes_index, __weekly_quotes in enumerate(self.__weekly_quotes_list, begin_row + 1):
            worksheet[f'A{__weekly_quotes_index}'] = __weekly_quotes.period()
            worksheet[f'B{__weekly_quotes_index}'] = __weekly_quotes.open()
            worksheet[f'C{__weekly_quotes_index}'] = __weekly_quotes.high()
            worksheet[f'D{__weekly_quotes_index}'] = __weekly_quotes.low()
            worksheet[f'E{__weekly_quotes_index}'] = __weekly_quotes.close()

    def calc(daily_quotes):
        __period = '1900-01'
        __brand = daily_quotes.brand()
        __weekly_quotes = WeeklyQuotes(__brand)

        for __quotes_index, __quotes in enumerate(daily_quotes.list()):
            __quotes_period = common.year_week_number(__quotes.period())
            if __period != __quotes_period:
                if __period != '1900-01':
                    __weekly_quotes.append(
                        __period, __open, __high, __low, __close)
                __period = __quotes_period
                __open = __quotes.open()
                __high = __quotes.high()
                __low = __quotes.low()
                print(__period)
            else:
                __high = max(__high, __quotes.high())
                __low = min(__low, __quotes.low())
                __close = __quotes.close()
        __weekly_quotes.append(__period, __open, __high, __low, __close)

        return __weekly_quotes