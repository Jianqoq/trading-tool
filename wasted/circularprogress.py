
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x498BD1
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.color = '#%02x%02x%02x' % (113, 255, 70)
        self.enable_shadow = True
        self.set_value(0)
        self.resize(self.width,self.height)

    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height- self.progress_width
        margin = self.progress_width/2
        value = self.value*360/self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)

        rect = QRect(0,0,self.width,self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        pen = QPen()
        pen.setColor(QColor(self.color))
        pen.setWidth(self.progress_width)

        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        paint.setPen(pen)
        paint.drawArc(int(margin),int(margin),width,height,-90*16,int(-value*16))
        #paint.drawArc(20, 20, 70, 70, 180, 180)

        paint.end()

    def set_value(self,value):
        self.value = value
        self.update()
