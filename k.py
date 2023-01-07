import sys
import time
from threading import *
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg
from pyqtgraph.exporters import ImageExporter
import datetime
from PyQt5.QtCore import Qt, QPointF, QRectF
from binance.spot import futures, Spot


class RectItem(pg.GraphicsObject):
    def __init__(self, data, parent):
        super().__init__()
        self.data = data
        self.w = None
        self.x = None
        self.toggle = False
        self.highest = 0
        self.lowest = 0
        self.parent = parent
        self.rect = QtCore.QRectF(0, 0, 1, 1)
        self.picture = QtGui.QPicture()
        self.pen0 = pg.mkPen(color=(0, 0, 0), width=1, style=QtCore.Qt.DotLine)
        self.pen = pg.mkPen(color=(0, 0, 0), width=1, style=QtCore.Qt.SolidLine)
        self.pen2 = pg.mkPen(color=(0, 208, 0), width=2, style=QtCore.Qt.SolidLine)
        self.pen3 = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.SolidLine)
        self.pen4 = pg.mkPen(color=(255, 170, 0), width=2, style=QtCore.Qt.SolidLine)
        self.pline = pg.InfiniteLine(angle=0, movable=False, pen=self.pen0)
        self.vline = pg.InfiniteLine(angle=90, movable=False, pen=self.pen)
        self.hline = pg.InfiniteLine(angle=0, movable=False, pen=self.pen)
        self.pline.hide()
        self.hline.hide()
        self.vline.hide()
        self.hline2 = pg.InfiniteLine(angle=0, movable=True, pen=self.pen2, hoverPen=self.pen2)
        self.hline3 = pg.InfiniteLine(angle=0, movable=True, pen=self.pen3, hoverPen=self.pen3)
        self.hline4 = pg.InfiniteLine(angle=0, movable=True, pen=self.pen4, hoverPen=self.pen4)
        self.hline2.hide()
        self.hline3.hide()
        self.hline4.hide()
        self.line_label = pg.InfLineLabel(self.hline2,text='0.0',position=0.98)
        self.line_label.setColor(color=(0, 208, 0))
        self.line_label2 = pg.InfLineLabel(self.hline3,text='0.0',position=0.98)
        self.line_label2.setColor(color=(255, 0, 0))
        self.line_label3 = pg.InfLineLabel(self.hline4,text='0.0',position=0.98)
        self.line_label3.setColor(color=(255, 170, 0))
        self.line_label4 = pg.InfLineLabel(self.pline,text='0.0',position=0.98)
        self.line_label4.setColor(color=(0, 0, 0))
        self.cursor = Qt.SizeVerCursor
        self.setFlag(self.ItemUsesExtendedStyleOption)
        cursor = Qt.SizeVerCursor
        self.hline2.setCursor(cursor)
        self.hline3.setCursor(cursor)
        self.hline4.setCursor(cursor)
        self.hline2.sigDragged.connect(self.handle_sig_dragged)
        self.hline3.sigDragged.connect(self.handle_sig_dragged2)
        self.hline4.sigDragged.connect(self.handle_sig_dragged3)
        self.generate_picture()

    def generate_picture(self):
        self.painter = QtGui.QPainter(self.picture)
        self.w = (self.data[1][0] - self.data[0][0]) / 3
        self.painter.setPen(pg.mkPen('black'))
        num = self.data[-1][0]
        op = self.data[-1][2]
        if (self.w and self.x) is not None:
            for n, open, close, low, high in self.data:
                self.painter.drawLine(QtCore.QPointF(n, low), QtCore.QPointF(n, high))
                if close < open:
                    self.painter.setBrush(pg.mkBrush(color=(0, 0, 0)))
                else:
                    self.painter.setBrush(pg.mkBrush('w'))

                self.painter.drawRect(QtCore.QRectF(n - self.w, open, self.w * 2, close - open))

            self.painter.drawLine(QtCore.QPointF(num+1, self.lowest), QtCore.QPointF(num+1, self.highest))
            if self.x > op:
                self.painter.setBrush(pg.mkBrush('w'))
            else:
               self.painter.setBrush(pg.mkBrush(color=(0, 0, 0)))
            self.painter.drawRect(QtCore.QRectF(num+1 - self.w, op, self.w * 2, self.x - op))
            self.painter.end()

    def paint(self, painter, option, widget=None):
        painter.drawPicture(0, 0, self.picture)
        array = self.convert_painting_2_array(self.parent)

    def convert_painting_2_array(self, parent):
        item = parent.getViewBox().allChildren(item=self)
        exporter = ImageExporter(item[0])
        data = exporter.export(toBytes=True)
        img = data.convertToFormat(QtGui.QImage.Format_RGBA8888)
        ptr = img.constBits()
        ptr.setsize(img.byteCount())
        width = img.width()
        height = img.height()
        arr = np.array(ptr).reshape(height, width, 4)
        return arr

    def handle_sig_dragged(self,obj):
        self.hline2.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label.setText(text=p)

    def handle_sig_dragged2(self,obj):
        self.hline3.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label2.setText(text=p)

    def handle_sig_dragged3(self,obj):
        self.hline4.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label3.setText(text=p)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

    def move(self, x, highest, lowest):
        p = float(x)
        self.highest = float(highest[0])
        self.lowest = float(lowest[0])
        self.x = p
        self.pline.setPos(p)
        self.line_label4.setText(text=x)
        self.prepareGeometryChange()
        self.generate_picture()
        self.update()

    def move2(self, x):
        self.data = x
        self.prepareGeometryChange()
        self.generate_picture()
        self.update()

    def move3(self, pos):
        if self.toggle:
            self.hline.setPos(pos.y())
            self.vline.setPos(pos.x())
        else:
            self.hline.setPos(pos.y())
            self.vline.setPos(pos.x())
            self.hline.show()
            self.vline.show()
            self.pline.show()
            self.toggle = True

    def showlines(self, price):

        p = float(price)
        self.hline2.setPos(p)
        low, high = self.getViewBox().viewRange()[1]
        p2 = p + (high - p)*0.01
        p3 = p - (p-low)*0.01
        self.hline3.setPos(p2)
        self.hline4.setPos(p3)
        self.hline2.show()
        self.hline4.show()
        self.hline3.show()


class PlotWidget(pg.PlotWidget):
    mouse_moved = QtCore.pyqtSignal(str, list, list)
    mouse_moved2 = QtCore.pyqtSignal(list)
    mouse_moved3 = QtCore.pyqtSignal(QPointF)
    key_pressed = QtCore.pyqtSignal(str)

    def __init__(self, intval):
        super().__init__()
        self.c = Spot(key='', secret='')
        self.price = self.c.klines(symbol='BTCBUSD',interval='5m',limit=1000)
        self.data1 = []
        self.data2 = []
        self.data3 = []
        self.data4 = []
        self.data5 = []
        self.data6 = []
        self.highest = []
        self.lowest = []
        self.lastone = []
        self.num = 0
        self.cishu = 1
        self.list = []
        self.list2 = []
        for i in self.price:
            self.data1.append(self.num)
            self.data2.append(float(i[1]))
            self.data3.append(float(i[4]))
            self.data4.append(float(i[3]))
            self.data5.append(float(i[2]))
            self.data6.append(i[0])
            self.num += 1
        self.q = list(zip(self.data1, self.data2, self.data3, self.data4, self.data5))
        self.hl = self.q.pop()
        self.l = self.hl[3]
        self.h = self.hl[4]
        self.timer = self.dingshiqi(intval)
        self.chufa()
        self.chufa2(intval)

    def chufa(self):
        thread = Thread(target=self.keepupdate)
        thread.start()

    def chufa2(self, intval):
        thread = Thread(target=self.updatedata, args=(intval,))
        thread.start()

    def keepupdate(self):
        try:
            while True:
                self.p = self.c.ticker_price(symbol='BTCBUSD')
                x = self.p['price']
                if len(self.highest) == 0 and len(self.lowest) == 0:
                    self.highest.append(x)
                    self.lowest.append(x)
                if x > self.highest[0]:
                    self.highest.clear()
                    self.highest.append(x)
                if x < self.lowest[0]:
                    self.lowest.clear()
                    self.lowest.append(x)
                self.mouse_moved.emit(self.p['price'], self.highest, self.lowest)
                time.sleep(0.2)
        except:
            self.chufa()

    def updatedata(self, intval):
        try:
            while True:
                time.sleep(self.timer)
                self.timer = self.dingshiqi(intval)
                if self.timer > 0:
                    print(self.timer)
                    num = self.q[-1][0]
                    p = self.c.ticker_price(symbol='BTCBUSD')
                    p1 = p['price']
                    tup = (num + 1, self.q[-1][2], p['price'], self.lowest[0], self.highest[0])
                    self.highest.clear()
                    self.lowest.clear()
                    self.highest.append(p1)
                    self.lowest.append(p1)
                    self.q.append(tup)
                    self.cishu = 2
                    self.mouse_moved2.emit(self.q)
                else:
                    continue
        except:
            self.chufa2(intval)

    def dingshiqi(self, intval):
            current = datetime.datetime.now().minute
            currentsec = datetime.datetime.now().second
            interval = intval
            list = []
            list2 = []
            for i in range(10000000000000000):
                time = interval * i * 60
                list.append(time)
                if time >= 3600:
                    break
            sec = current * 60 + currentsec
            for i in range(len(list)):
                if sec <= list[i]:
                    list2.append(list[i])
            timer = list2[0] - sec
            return timer

    def PlotCursor(self, event):
        pos = event
        mousePoint = self.plotItem.vb.mapSceneToView(pos)
        self.mouse_moved3.emit(mousePoint)

    def keyPressEvent(self, event):
        super(PlotWidget, self).keyPressEvent(event)
        if event.key() == Qt.Key_Return:
            self.key_pressed.emit(self.p['price'])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = PlotWidget(15)
    main.setBackground('w')
    data = main.q
    rect = RectItem(data, main)
    main.mouse_moved.connect(rect.move)
    main.mouse_moved2.connect(rect.move2)
    main.mouse_moved3.connect(rect.move3)
    main.key_pressed.connect(rect.showlines)
    main.addItem(rect)
    main.addItem(rect.pline)
    main.addItem(rect.vline)
    main.addItem(rect.hline)
    main.addItem(rect.hline2)
    main.addItem(rect.hline3)
    main.addItem(rect.hline4)
    pg.SignalProxy(main.scene().sigMouseMoved, rateLimit=60, slot=main.PlotCursor)
    main.plotItem.scene().sigMouseMoved.connect(main.PlotCursor)
    item = main.getViewBox().allChildren(item=rect)
    main.show()

    sys.exit(app.exec_())
