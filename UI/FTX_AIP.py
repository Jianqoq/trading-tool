from PyQt5 import QtCore, QtGui, QtWidgets


# import t

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        # Remove title bar
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.resize(512, 450)
        MainWindow.setMinimumSize(QtCore.QSize(512, 450))
        MainWindow.setMaximumSize(QtCore.QSize(512, 450))
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
                                 "QToolTip {\n"
                                 "    color: #ffffff;\n"
                                 "    background-color: rgba(227, 29, 35, 160);\n"
                                 "    border: 1px solid rgb(40, 40, 40);\n"
                                 "    border-radius: 2px;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 512, 512))
        self.frame.setStyleSheet("QFrame {\n"
                                 "background-image: url(lena.jpg);\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # Connect frame to mouseMoveEvent
        self.frame.mouseMoveEvent = self.mouseMoveEvent
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


#    def mouseMoveEvent(self, event):
#        if event.buttons() == QtCore.Qt.LeftButton:
#            self.move(self.pos() + event.globalPos() - self.dragPos)
#            self.dragPos = event.globalPos()
#            event.accept()


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()

    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    #    MainWindow = QtWidgets.QMainWindow()
    #    ui = Ui_MainWindow()
    #    ui.setupUi(MainWindow)
    #    MainWindow.show()
    w = MyWin()
    w.show()
    sys.exit(app.exec_())