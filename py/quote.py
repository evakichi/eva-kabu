class Quote:

    __period = None
    __open = 0.0
    __high = 0.0
    __low = 0.0
    __close = 0.0

    def __init__(self, period, open, high, low, close) -> None:
        self.__period = period
        self.__open = open
        self.__high = high
        self.__low = low
        self.__close = close

    def re_set(self, basic_candle_stick, advanced_candle_stick, detailed_candle_stick):
        self.__basic_candle_stick = basic_candle_stick
        self.__advanced_candle_stick = advanced_candle_stick
        self.__detailed_candle_stick = detailed_candle_stick

    def basic_candle_stick(self):
        return self.__basic_candle_stick

    def advanced_candle_stick(self):
        return self.__advanced_candle_stick

    def detailed_candle_stick(self):
        return self.__detailed_candle_stick

    def print(self):
        print(
            f'{self.__period}:{self.__open}-{self.__high}-{self.__low}-{self.__close}')

    def period(self):
        return self.__period

    def open(self):
        return self.__open

    def high(self):
        return self.__high

    def low(self):
        return self.__low

    def close(self):
        return self.__close
