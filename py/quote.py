class Quote:

    __period           = None
    __open             = 0.0
    __high             = 0.0
    __low              = 0.0
    __close            = 0.0

    def __init__(self,period,open,high,low,close) -> None:
        self.__period = period
        self.__open   = open
        self.__high   = high
        self.__low    = low
        self.__close  = close

    def print(self):
        print(f'{self.__period}:{self.__open}-{self.__high}-{self.__low}-{self.__close}')