import sys
import time
from threading import Thread
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
        self.first_time = True
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
        painter = QtGui.QPainter(self.picture)
        self.w = (self.data[1][0] - self.data[0][0]) / 3
        painter.setPen(pg.mkPen('black'))
        num = self.data[-1][0]
        op = self.data[-1][2]
        if (self.w and self.x) is not None:
            try:
                for n, open, close, low, high in self.data:
                    painter.drawLine(QtCore.QPointF(n, low), QtCore.QPointF(n, high))
                    if close < open:
                        painter.setBrush(pg.mkBrush(color=(0, 0, 0)))
                    else:
                        painter.setBrush(pg.mkBrush('w'))

                    painter.drawRect(QtCore.QRectF(n - self.w, open, self.w * 2, close - open))

                painter.drawLine(QtCore.QPointF(num+1, self.lowest), QtCore.QPointF(num+1, self.highest))
                if self.x > op:
                    painter.setBrush(pg.mkBrush('w'))
                else:
                   painter.setBrush(pg.mkBrush(color=(0, 0, 0)))
                painter.drawRect(QtCore.QRectF(num+1 - self.w, op, self.w * 2, self.x - op))
                painter.end()
            except:
                self.parent.close()

    def paint(self, painter, option, widget=None):
        painter.drawPicture(0, 0, self.picture)
        self.getViewBox().setLimits(xMin = 0)
        left, right = [int(i) for i in self.getViewBox().state['viewRange'][0]]
        self.getViewBox().setYRange(min(self.parent.q[left:right], key=lambda x: x[3])[3], max(self.parent.q[left:right], key=lambda x: x[4])[4])

    def convert_painting_2_array(self, width, height):
        exporter = ImageExporter(self.getViewBox())
        exporter.parameters()['width'] = width
        exporter.parameters()['height'] = height
        data = exporter.export(toBytes=True)
        img = data.convertToFormat(QtGui.QImage.Format_RGBA8888)
        ptr = img.constBits()
        ptr.setsize(img.byteCount())
        width = img.width()
        height = img.height()
        arr = np.array(ptr).reshape(height, width, 4)
        return arr

    def handle_sig_dragged(self,obj):
        self.parent.setCursor(self.cursor)
        self.hline2.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label.setText(text=p)

    def handle_sig_dragged2(self,obj):
        self.parent.setCursor(self.cursor)
        self.hline3.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label2.setText(text=p)

    def handle_sig_dragged3(self,obj):
        self.parent.setCursor(self.cursor)
        self.hline4.setCursor(self.cursor)
        p = '%.2f' % obj.pos().y()
        self.line_label3.setText(text=p)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

    def move(self, x, highest, lowest):
        self.highest = highest
        self.lowest = lowest
        self.x = x
        self.pline.setPos(x)
        self.line_label4.setText(text=str(x))
        self.prepareGeometryChange()
        self.generate_picture()
        self.update()

    def move2(self, x):
        self.data = x
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

    def showlines(self, p):
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
    mouse_moved = QtCore.pyqtSignal(float, float, float)
    mouse_moved2 = QtCore.pyqtSignal(list)
    mouse_moved3 = QtCore.pyqtSignal(QPointF)
    key_pressed = QtCore.pyqtSignal(float)
    trigger = QtCore.pyqtSignal(int, int)

    def __init__(self, intval):
        super().__init__()
        self.c = Spot(key='',
                      secret='')
        price = self.c.klines(symbol='BTCBUSD',interval='1m',limit=1000)
        self.p = 0
        self.lastone = []
        self.num = 0
        self.cishu = 1
        self.q = [(index, float(i[1]), float(i[4]), float(i[3]), float(i[2])) for index, i in enumerate(price)]
        self.hl = self.q.pop()
        self.l = self.hl[3]
        self.h = self.hl[4]
        self.timer = self.dingshiqi(intval)
        self.setCursor(Qt.CrossCursor)
        Thread(target=self.keepupdate).start()
        self.chufa2(intval)

    def chufa2(self, intval):
        thread = Thread(target=self.updatedata, args=(intval,))
        thread.start()

    def keepupdate(self):
        try:
            while 1:
                p = self.c.ticker_price(symbol='BTCBUSD')
                x = self.p = float(p['price'])
                if x > self.h:
                    self.h = x
                if x < self.l:
                    self.l = x
                self.mouse_moved.emit(x, self.h, self.l)
                time.sleep(0.2)
        except:
            Thread(target=self.keepupdate).start()

    def updatedata(self, intval: int):
        try:
            while 1:
                print(self.timer)
                time.sleep(self.timer)
                self.timer = self.dingshiqi(intval)
                if self.timer > 0:
                    num = self.q[-1][0]
                    p = self.c.ticker_price(symbol='BTCBUSD')
                    p1 = float(p['price'])
                    tup = (num + 1, self.q[-1][2], p1, self.l, self.h)
                    self.l = p1
                    self.h = p1
                    self.q.append(tup)
                    self.cishu = 2
                    self.mouse_moved2.emit(self.q)
        except:
            self.chufa2(intval)

    def dingshiqi(self, intval: int):
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
            self.key_pressed.emit(self.p)

    def mouseReleaseEvent(self, event):
        super(PlotWidget, self).mouseReleaseEvent(event)
        self.trigger.emit(1280, 1280)

    def wheelEvent(self, event):
        super(PlotWidget, self).wheelEvent(event)
        self.trigger.emit(1280, 1280)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = PlotWidget(1)
    main.setBackground('w')
    data = main.q
    rect = RectItem(data, main)
    main.mouse_moved.connect(rect.move)
    main.mouse_moved2.connect(rect.move2)
    main.mouse_moved3.connect(rect.move3)
    main.key_pressed.connect(rect.showlines)
    main.trigger.connect(rect.convert_painting_2_array)
    main.addItem(rect)
    main.addItem(rect.pline)
    main.addItem(rect.vline)
    main.addItem(rect.hline)
    main.addItem(rect.hline2)
    main.addItem(rect.hline3)
    main.addItem(rect.hline4)
    pg.SignalProxy(main.scene().sigMouseMoved, rateLimit=60, slot=main.PlotCursor)
    main.plotItem.scene().sigMouseMoved.connect(main.PlotCursor)
    main.show()

    sys.exit(app.exec_())
