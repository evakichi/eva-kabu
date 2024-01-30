import quote


class BasicCandleStick:

    BASIC_CANDLE_STICK = ['-',
                          '陰線',
                          '陽線',
                          '寄引同時線'
                          ]

    def __init__(self, state) -> None:
        self.__state = state

    def to_string(self):
        return self.BASIC_CANDLE_STICK[self.__state]

    def get(self):
        return self.__state

    def calc(quote):
        __open = quote.open()
        __high = quote.high()
        __low = quote.low()
        __close = quote.close()

        if __open > __close:
            return BasicCandleStick(1)

        if __open < __close:
            return BasicCandleStick(2)

        if __open == __close:
            return BasicCandleStick(3)
        return BasicCandleStick(0)


class AdvancedCandleStick:

    ADVANCED_CANDLE_STICK = ['-',
                             '大陰線',
                             '大陽線',
                             '小陰線',
                             '小陽線',
                             '上ヒゲ陰線',
                             '上ヒゲ陽線',
                             '下ヒゲ陰線',
                             '下ヒゲ陽線',
                             '寄引同時線'
                             ]

    def __init__(self, state) -> None:
        self.__state = state

    def to_string(self):
        return self.ADVANCED_CANDLE_STICK[self.__state]

    def get(self):
        return self.__state

    def calc(quote):
        __open = quote.open()
        __high = quote.high()
        __low = quote.low()
        __close = quote.close()

        if __open > __close:
            return AdvancedCandleStick(1)

        if __open < __close:
            return AdvancedCandleStick(2)

        if __open == __close:
            return AdvancedCandleStick(3)
        return AdvancedCandleStick(0)


class DetailedCandleStick:

    DETAILED_CANDLE_STICK = ['-',
                             '陰の丸坊主',
                             '陽の丸坊主',
                             '陰の大引坊主',
                             '陰の寄付坊主',
                             '陽の寄付坊主',
                             '陽の大引坊主',
                             'コマ(陰の極線)',
                             'コマ(陽の極線)',
                             'トンボ',
                             'トンボ',
                             'トウバ(石塔)',
                             '足長同時(寄せ場)',
                             '陰のカラカサ(たぐり線)',
                             '陰のトンカチ(たぐり線)',
                             '陽のカラカサ(たぐり線)',
                             '陽のトンカチ(たぐり線)',
                             '四値同時(一本同時)'
                             ]

    def __init__(self, state) -> None:
        self.__state = state

    def to_string(self):
        return self.DETAILED_CANDLE_STICK[self.__state]

    def get(self):
        return self.__state

    def calc(quote):
        __open = quote.open()
        __high = quote.high()
        __low = quote.low()
        __close = quote.close()

        if __open > __close:
            return DetailedCandleStick(1)

        if __open < __close:
            return DetailedCandleStick(2)

        if __open == __close:
            return DetailedCandleStick(3)
        return DetailedCandleStick(0)
