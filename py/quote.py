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
