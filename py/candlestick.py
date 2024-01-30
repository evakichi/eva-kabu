import quote


class BasicCandleStick:

    CANDLE_STICK_3 = ['-',
                      '陰線',
                      '陽線',
                      '寄引同時線'
                      ]

    CANDLE_STICK_9 = ['-',
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

    CANDLE_STICK_17 = ['-',
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
        return self.CANDLE_STICK_3[self.__state]

    def detect(quote):
        __open = quote.open()
        __high = quote.open()
        __low = quote.open()
        __close = quote.open()

        if __open > __close:
            return BasicCandleStick(1)

        if __open < __close:
            return BasicCandleStick(2)

        if __open == __close:
            return BasicCandleStick(3)
        return BasicCandleStick(0)
