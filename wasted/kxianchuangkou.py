from UI import graph
import sys
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from still_work import k
from PyQt5.QtCore import Qt
import mainwin


class kxian_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = graph.Ui_MainWindow()
        self.ui.setupUi(self)
        self.graph = self.ui.widget
        self.main = k.PlotWidget(15)
        self.main.setBackground('w')
        self.data = self.main.q
        self.rect = k.RectItem(self.data)
        self.main.mouse_moved.connect(self.rect.move)
        self.main.mouse_moved2.connect(self.rect.move2)
        self.currentp = 0
        self.tp = 0
        self.entry = 0
        self.sl = 0
        self.check = False
        self.win = mainwin.FTXWindow()
        self.graph.setBackground((226, 226, 226))
        self.graph.addItem(self.rect)
        self.graph.addItem(self.rect.hline, ignoreBounds=True)
        self.graph.addItem(self.rect.vline, ignoreBounds=True)
        self.graph.addItem(self.rect.pline, ignoreBounds=True)
        self.graph.installEventFilter(self)
        pg.SignalProxy(self.graph.plotItem.scene().sigMouseMoved, rateLimit=60, slot=self.PlotCursor)
        self.graph.plotItem.scene().sigMouseMoved.connect(self.PlotCursor)
        self.price = self.rect.y
        self.win.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            self.Plot_lines()
            self.check = True
        if e.key() == Qt.Key_Return and self.check == True:
            self.win.ui.xiadan_ruchang.setText(str(self.entry))
            self.win.ui.xiadan_zhisun_2.setText(str(self.tp))
            self.win.ui.xiadan_zhiying.setText(str(self.sl))
            self.check = False

    def Plot_lines(self):
        self.graph.addItem(self.rect.hline2, ignoreBounds=True)
        self.graph.addItem(self.rect.hline3, ignoreBounds=True)
        self.graph.addItem(self.rect.hline4, ignoreBounds=True)
        self.rect.line_label.setText(text=str(self.rect.close*1.01))
        self.rect.line_label2.setText(text=str(self.rect.close*0.99))
        self.rect.line_label3.setText(text=str(self.rect.close))

    def PlotCursor(self,event):
        pos = event
        mousePoint = self.graph.plotItem.vb.mapSceneToView(pos)
        self.tp = self.rect.hline2.pos().y()
        self.entry = self.rect.hline4.pos().y()
        self.sl = self.rect.hline3.pos().y()
        y = '%.0f' % mousePoint.y()
        x = '%.2f' % mousePoint.x()
        self.rect.vline.setPos(mousePoint.x())
        self.rect.hline.setPos(mousePoint.y())
        self.ui.label.move(0,int(pos.y()-self.ui.label.geometry().height()/2))
        self.ui.label_2.move(int(pos.x() - self.ui.label_2.geometry().width()/2),1080)
        self.ui.label.setText(y)
        self.ui.label_2.setText(x)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = kxian_MainWindow()
    w.show()
    app.exec_()