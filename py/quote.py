class Quote:

    __period = None
    __open = 0.0
    __high = 0.0
    __low = 0.0
    __close = 0.0
    __volume = 0.0

    def __init__(self, period, open, high, low, close, volume) -> None:
        self.__period = period
        self.__open = open
        self.__high = high
        self.__low = low
        self.__close = close
        self.__volume = volume

    def print(self):
        print(
            f'{self.__period}:{self.__open}-{self.__high}-{self.__low}-{self.__close}:{self.__volume}')

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

    def volume(self):
        return self.__volume
