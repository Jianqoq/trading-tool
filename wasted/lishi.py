import sys

from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QTreeView, QVBoxLayout,
                             QWidget)
import api

c = api.FtxClient(
                 api_key="",
                    api_secret="")

class lishi(QWidget):
    Id, pinzhong, fangxiang ,cangwei,zhuangtai,leixing= range(6)

    def __init__(self):
        super().__init__()
        self.title = ''
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 240
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.dataGroupBox = QGroupBox("Inbox")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)

        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)

        model = self.createMailModel(self)
        self.dataView.setModel(model)

        for elements in c.get_order_history():
            self.addMail(model, elements["id"], elements["market"], elements["side"],elements["size"],elements["status"],elements["type"])


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)

        self.show()

    def createMailModel(self, parent):
        model = QStandardItemModel(0, 6, parent)
        model.setHeaderData(self.Id, Qt.Horizontal, "Id")
        model.setHeaderData(self.pinzhong, Qt.Horizontal, "品种")
        model.setHeaderData(self.fangxiang, Qt.Horizontal, "方向")
        model.setHeaderData(self.cangwei, Qt.Horizontal, "仓位")
        model.setHeaderData(self.zhuangtai, Qt.Horizontal, "状态")
        model.setHeaderData(self.leixing, Qt.Horizontal, "类型")

        return model

    def addMail(self, model, Id, pinzhong, fangxiang, cangwei,zhuangtai,leixing):
        model.insertRow(0)
        model.setData(model.index(0, self.Id), Id)
        model.setData(model.index(0, self.pinzhong), pinzhong)
        model.setData(model.index(0, self.fangxiang), fangxiang)
        model.setData(model.index(0, self.cangwei), cangwei)
        model.setData(model.index(0, self.zhuangtai), zhuangtai)
        model.setData(model.index(0, self.leixing), leixing)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = lishi()
    sys.exit(app.exec_())
