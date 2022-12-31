from wasted.circularprogress import *
import sys
import time

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1000,1000)
        self.container = QFrame()
        self.container.setStyleSheet("background-color:transparent")
        self.layout = QVBoxLayout()
        self.progress = CircularProgress()
        self.progress.progress_width = 10
        self.progress.width = 380
        self.progress.height = 380
        self.progress.Value = 100
        self.progress.max_value = 100
        self.progress.set_value(100)
        self.progress.setMinimumSize(self.progress.width,self.progress.height)
        self.layout.addWidget(self.progress,Qt.AlignCenter,Qt.AlignCenter)
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.show()

    def jindu(self):
        global v
        v = 0
        while v < 100:
            v += 1
            print(v)
            self.progress.Value=v
            time.sleep(0.1)
            if v >= 100:
                v = 1
            continue

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())