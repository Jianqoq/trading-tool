import pandas as pd
import api
from threading import *
import time


class Data:
    def __init__(self):
        self.c = api.FtxClient(
            api_key="",
            api_secret="")
        self.price = self.c.get_historical_prices(market='BTC-PERP', resolution=15)
        self.last = len(self.price)
        self.current_price = self.price[self.last - 1]['close']
        self.price1 = pd.DataFrame(self.price)
        self.data1 = []
        self.data2 = []
        self.data3 = []
        self.data4 = []
        self.data5 = []
        self.data6 = []
        self.num = 0
        # print(self.current_price)
        for i in self.price:
            self.data1.append(self.num)
            self.data2.append(i['open'])
            self.data3.append(i['close'])
            self.data4.append(i['low'])
            self.data5.append(i['high'])
            self.num += 1
        self.q = list(zip(self.data1, self.data2, self.data3, self.data4, self.data5))
        self.chufa01()

    def chufa01(self):
        thread = Thread(target=self.current_price1)
        thread.start()

    def current_price1(self):
        while True:
            self.p = self.c.get_market(market_name='BTC-PERP')
            print(self.p['price'])
            time.sleep(1)

Data()