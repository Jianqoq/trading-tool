import pandas as pd
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from threading import *
import time
import numpy as np


class Data:
    def __init__(self):
        self.price = self.c.get_historical_prices(market='BTC-PERP', start_time=1559881511,resolution=3600)
        self.last = len(self.price)
        self.current_price = self.price[self.last-1]['close']
        self.price1 = pd.DataFrame(self.price)
        self.data1 = []
        self.data2 = []
        self.data3 = []
        self.data4 = []
        self.data5 = []
        self.data6 = []
        self.data7 = []
        self.data8 = []
        self.data9 = []
        self.data10 = []
        self.num = 0
        self.close = 0
        self.array1 = np.array([])
        for i in self.price:
            self.data1.append(self.num)
            self.data2.append(i['open'])
            self.data3.append(i['close'])
            self.data4.append(i['low'])
            self.data5.append(i['high'])
            self.num += 1
        self.a = np.append(self.array1, [20])
        self.a = np.append(self.array1, [40])
        print(self.a)
        self.q = list(zip(self.data1, self.data2, self.data3, self.data4, self.data5))
        self.y = 0
        self.chufa01()
        #print(self.current_price

    def chufa01(self):
        thread = Thread(target=self.current_price1)
        thread.start()

    def current_price1(self):
        while True:
            x = self.c.get_market(market_name='BTC-PERP')
            self.close=x['price']
            time.sleep(0.5)


class CandlestickItem(pg.GraphicsObject):
    def __init__(self, pl,plotcursor):
        pg.GraphicsObject.__init__(self)
        self.picture = QtGui.QPicture()
        self.q1 = Data()
        close = self.q1.current_price
        self.pictures = []
        self.p = QtGui.QPainter(self.picture)
        self.value2 = 0
        self.p.setPen(pg.mkPen(color=(0, 0, 0)))
        self.setFlag(self.ItemUsesExtendedStyleOption)
        self.pen = pg.mkPen(color=(0, 0, 0), width=1, style=QtCore.Qt.SolidLine)
        self.pen2 = pg.mkPen(color=(0, 208, 0), width=2, style=QtCore.Qt.SolidLine)
        self.pen3 = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.SolidLine)
        self.pen4 = pg.mkPen(color=(255, 170, 0), width=2, style=QtCore.Qt.SolidLine)
        self.vline = pg.InfiniteLine(angle=90, movable=False, pen=self.pen)
        self.vline.setPos(-100)
        self.hline = pg.InfiniteLine(angle=0, movable=False, pen=self.pen)
        self.hline.setPos(-100)
        self.hline2 = pg.InfiniteLine(angle=0, movable=True, pen=self.pen2, hoverPen=self.pen2)
        self.hline3 = pg.InfiniteLine(angle=0, movable=True, pen=self.pen3, hoverPen=self.pen3)
        self.hline4 = pg.InfiniteLine(angle=0, movable=True, pen=self.pen4, hoverPen=self.pen4)
        self.line_label = pg.InfLineLabel(self.hline2,text='0.0',position=0.98)
        self.line_label.setColor(color=(0, 208, 0))
        self.line_label2 = pg.InfLineLabel(self.hline3,text='0.0',position=0.98)
        self.line_label2.setColor(color=(255, 0, 0))
        self.line_label3 = pg.InfLineLabel(self.hline4,text='0.0',position=0.98)
        self.line_label3.setColor(color=(255, 170, 0))
        self.hline2.setPos(close*1.01)
        self.hline3.setPos(close*0.99)
        self.hline4.setPos(close)
        self.cursor = Qt.SizeVerCursor
        self.pl = pl
        self.setFlag(self.ItemUsesExtendedStyleOption)
        self.pl.setCursor(Qt.CrossCursor)
        cursor = Qt.SizeVerCursor
        self.hline2.setCursor(cursor)
        self.hline3.setCursor(cursor)
        self.hline4.setCursor(cursor)
        self.hline2.sigDragged.connect(self.handle_sig_dragged)
        self.hline3.sigDragged.connect(self.handle_sig_dragged2)
        self.hline4.sigDragged.connect(self.handle_sig_dragged3)
        self.move_slot = pg.SignalProxy(self.pl.scene().sigMouseMoved, rateLimit=100, slot=plotcursor)
        self.pl.scene().sigMouseClicked.connect(self.mouse_clicked)
        self.len2 = len(self.q1.data3) -1
        self.close = self.q1.data3[self.len2]
        self.close1 = 1000
        self.value1 = 0
        self.w = 0
        self.value2 = 0
        self.chufa()
        #self.chufa2()

    def set_data(self,data):
        self.close1 = data


    def handle_sig_dragged(self,obj):
        self.hline2.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label.setText(text=p)
        assert obj is self.hline2

    def handle_sig_dragged2(self,obj):
        self.hline3.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label2.setText(text=p)
        assert obj is self.hline3

    def handle_sig_dragged3(self,obj):
        self.hline4.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label3.setText(text=p)
        assert obj is self.hline4

    def generatePicture(self):
        self.w = (self.q1.q[1][0] - self.q1.q[0][0]) / 3
        for (t, open, close, min, max) in self.q1.q:
            self.p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                self.p.setBrush(pg.mkBrush(color=(0, 0, 0)))
            else:
                self.p.setBrush(pg.mkBrush('w'))
            self.p.drawRect(QtCore.QRectF(t - self.w, open, self.w * 2, close - open))
        self.p.end()

    def paint(self,x,*args):
        x.drawPicture(0, 0, self.picture)

    def chufa2(self):
        thread = Thread(target=self.paint,args=(self.p,))
        thread.start()

    def mouse_clicked(self, event):
        price = self.hline3.pos().y()

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

    def chufa(self):
        thread = Thread(target=self.generatePicture)
        thread.start()

    def _update(self):
        self.picture = None
        self.prepareGeometryChange()
        self.update()

"""class CandlestickItem2(pg.GraphicsObject):
    def __init__(self):
        pg.GraphicsObject.__init__(self)
        self.data = [
    (1., 10, 13, 5, 15),
    (2., 13, 17, 9, 20),
    (3., 17, 14, 11, 23),
    (4., 14, 15, 5, 19),
    (5., 15, 9, 8, 22),
    (6., 9, 15, 8, 16),]
        self.generatePicture()

    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly,
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('r'))
            else:
                p.setBrush(pg.mkBrush('g'))
            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())"""


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()