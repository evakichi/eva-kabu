import common
import quote
import candlestick


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
        worksheet[f'F{row}'] = 'basic'
        worksheet[f'G{row}'] = 'advanced'
        worksheet[f'H{row}'] = 'detailed'

    def write_xslx(self, workbook, begin_row):
        worksheet = workbook.create_sheet(title="weekly")
        self.write_xlsx_header(worksheet, begin_row)
        for __weekly_quotes_index, __weekly_quotes in enumerate(self.__weekly_quotes_list, begin_row + 1):
            worksheet[f'A{__weekly_quotes_index}'] = __weekly_quotes.period()
            worksheet[f'B{__weekly_quotes_index}'] = __weekly_quotes.open()
            worksheet[f'C{__weekly_quotes_index}'] = __weekly_quotes.high()
            worksheet[f'D{__weekly_quotes_index}'] = __weekly_quotes.low()
            worksheet[f'E{__weekly_quotes_index}'] = __weekly_quotes.close()
            worksheet[f'F{__weekly_quotes_index}'] = __weekly_quotes.basic_candle_stick(
            ).to_string()
            worksheet[f'G{__weekly_quotes_index}'] = __weekly_quotes.advanced_candle_stick(
            ).to_string()
            worksheet[f'H{__weekly_quotes_index}'] = __weekly_quotes.detailed_candle_stick(
            ).to_string()

    def re_calc(self):
        for __weekly_quotes_index, __weekly_quotes in enumerate(self.__weekly_quotes_list):
            __weekly_quotes.re_set(candlestick.BasicCandleStick.calc(__weekly_quotes),
                                   candlestick.AdvancedCandleStick.calc(
                __weekly_quotes),
                candlestick.DetailedCandleStick.calc(__weekly_quotes))

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

            if __period != __quotes_period:
                __weekly_quotes.append(
                    __period, __open, __high, __low, __close)
                __period = __quotes_period                
                __open = __quotes.open()
                __high = __quotes.high()
                __low = __quotes.low()

            if __period == __quotes_period:
                __high = max(__high, __quotes.high())
                __low = min(__low, __quotes.low())
                __close = __quotes.close()

            if __quotes_index == __last_index:               
                __high = max(__high, __quotes.high())
                __low = min(__low, __quotes.low())
                __close = __quotes.close()
                __weekly_quotes.append(
                    __period, __open, __high, __low, __close)

        return __weekly_quotes
