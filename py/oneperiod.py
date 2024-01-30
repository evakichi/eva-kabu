import candlestick


class OnePeriod:

    def __init__(self) -> None:
        pass

    def check(quotes_list):
        for __quote_index, __quote in enumerate(quotes_list):
            __quote.set_basic_candle_stick(
                candlestick.BasicCandleStick.detect(__quote))
