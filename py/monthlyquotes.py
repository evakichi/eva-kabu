import common
import quote
import candlestick
import openpyxl


class MonthlyQuotes:

    def __init__(self, brand) -> None:
        self.__brand = brand
        self.__monthly_quotes_list = list()

    def append(self, period, open, high, low, close):
        self.__monthly_quotes_list.append(
            quote.Quote(period, open, high, low, close))

    def brand(self):
        return self.__brand

    def list(self):
        return self.__monthly_quotes_list

    def write_xlsx_header(self, worksheet, row):
        worksheet[f'A{row}'] = 'month'
        worksheet[f'B{row}'] = 'open'
        worksheet[f'C{row}'] = 'high'
        worksheet[f'D{row}'] = 'low'
        worksheet[f'E{row}'] = 'close'
        worksheet[f'F{row}'] = 'basic'
        worksheet[f'G{row}'] = 'advanced'
        worksheet[f'H{row}'] = 'detailed'

    def write_xslx(self, workbook, begin_row):
        __worksheet = workbook.create_sheet(title='monthly')
        self.write_xlsx_header(__worksheet, begin_row)
        for __monthly_quotes_index, __monthly_quotes in enumerate(self.__monthly_quotes_list, begin_row + 1):
            __worksheet[f'A{__monthly_quotes_index}'] = __monthly_quotes.period()
            __worksheet[f'B{__monthly_quotes_index}'] = __monthly_quotes.open()
            __worksheet[f'C{__monthly_quotes_index}'] = __monthly_quotes.high()
            __worksheet[f'D{__monthly_quotes_index}'] = __monthly_quotes.low()
            __worksheet[f'E{__monthly_quotes_index}'] = __monthly_quotes.close()

            __worksheet[f'F{__monthly_quotes_index}'] = __monthly_quotes.basic_candle_stick(
            ).to_string()
            __worksheet[f'G{__monthly_quotes_index}'] = __monthly_quotes.advanced_candle_stick(
            ).to_string()
            __worksheet[f'H{__monthly_quotes_index}'] = __monthly_quotes.detailed_candle_stick(
            ).to_string()

        __candle_stick_chart = openpyxl.chart.StockChart()
        __candle_stick_labels = openpyxl.chart.Reference(__worksheet,min_col=1,min_row=2,max_row=__worksheet.max_row)
        __candle_stick_data = openpyxl.chart.Reference(__worksheet,min_col=2,max_col=5,min_row=2,max_row=__worksheet.max_row)
        __candle_stick_chart.add_data(__candle_stick_data,titles_from_data=True)
        for __series in __candle_stick_chart.series:
            __series.graphicalProperties.line.noFill = True
        __candle_stick_chart.hiLowLines = openpyxl.chart.axis.ChartLines()
        __candle_stick_chart.upDownBars = openpyxl.chart.updown_bars.UpDownBars()

        __candle_stick_pts = [openpyxl.chart.data_source.NumVal(idx=i) for i in range(len(__candle_stick_data) - 1)]
        __candle_stick_cache = openpyxl.chart.data_source.NumData(pt=__candle_stick_pts)
        __candle_stick_chart.series[-1].val.numRef.numCache = __candle_stick_cache

        __candle_stick_chart.set_categories(__candle_stick_labels)
        __candle_stick_chart.width = 40
        __candle_stick_chart.height = 23
        __candle_stick_chart.legend = None
        
        __candle_stick_graph = workbook.create_sheet(title='monthly graph')
        __candle_stick_graph.add_chart(__candle_stick_chart,"A1")

    def re_calc(self):
        for __monthly_quotes_index, __monthly_quotes in enumerate(self.__monthly_quotes_list):
            __monthly_quotes.re_set(candlestick.BasicCandleStick.calc(__monthly_quotes),
                                    candlestick.AdvancedCandleStick.calc(
                __monthly_quotes),
                candlestick.DetailedCandleStick.calc(__monthly_quotes))

    def calc(daily_quotes):

        __period = '1900-01'
        __brand = daily_quotes.brand()
        __monthly_quotes = MonthlyQuotes(__brand)
        __last_index = len(daily_quotes.list()) - 1

        for __quotes_index, __quotes in enumerate(daily_quotes.list()):
            __quotes_period = common.year_month(__quotes.period())
            if __quotes_index == 0:
                __period = __quotes_period
                __open = __quotes.open()
                __high = __quotes.high()
                __low = __quotes.low()

            if __period != __quotes_period:
                __monthly_quotes.append(
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
                __monthly_quotes.append(
                    __period, __open, __high, __low, __close)

        return __monthly_quotes
