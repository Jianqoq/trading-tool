from UI.FTX import *
import datetime
from wasted import circularprogress
import json
import os
import sys
import time
from threading import *
from PyQt5.QtWidgets import *
from UI.lishidingdanui import *
from PyQt5.QtCore import (QEasingCurve,
                          QPropertyAnimation, QPoint)
from binance.cm_futures import CMFutures


with open('D:\初始资金\初始资金.txt') as chushizijin:
    zijin = chushizijin.read()

class FTXWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.offset = None
        self.timenow = None
        self.progress = None
        self.ui2 = None
        self.ui3 = None
        self.window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.animation()
        self.setFixedSize(2000, 1500)
        self.usd = 0.0
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.shadow()
        self.c = CMFutures(
            key="",
            secret="")
        self.labels5 = []
        self.labels2 = []
        self.labels3 = []
        self.labels4 = []
        self.labels7 = []
        self.labels8 = []
        self.labels9 = []
        self.labels10 = []
        self.label = []
        self.setup_roundprogressbar()
        #self.chufa5()
        #self.chufa3()
        #self.chufa()
        #self.chufa4()
        #self.chufa11()
        self.pair_base()
        self.widgets_binding()


    def setup_roundprogressbar(self):
        self.progress = circularprogress.CircularProgress()
        self.progress.width = 380
        self.progress.height = 380
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(850, 3100)
        self.progress.setParent(self.ui.centralwidget)
        self.anim12 = QPropertyAnimation(self.progress, b"pos")
        self.anim12.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim12.setEndValue(QPoint(850, 430))
        self.anim12.setDuration(2650)
        self.anim12.start()
        self.progress.show()

    def animation(self):
        self.anim = QPropertyAnimation(self.ui.frame_15, b"pos")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.setEndValue(QPoint(760, 210))
        self.anim.setDuration(1650)
        self.anim2 = QPropertyAnimation(self.ui.sousuo, b"pos")
        self.anim2.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim2.setEndValue(QPoint(760, 130))
        self.anim2.setDuration(1650)
        self.anim3 = QPropertyAnimation(self.ui.label_2, b"pos")
        self.anim3.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim3.setEndValue(QPoint(760, 130))
        self.anim3.setDuration(1650)
        self.anim4 = QPropertyAnimation(self.ui.pushButton_11, b"pos")
        self.anim4.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim4.setEndValue(QPoint(1160, 140))
        self.anim4.setDuration(1650)
        self.anim5 = QPropertyAnimation(self.ui.frame_7, b"pos")
        self.anim5.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim5.setEndValue(QPoint(750, 609))
        self.anim5.setDuration(1650)
        self.anim6 = QPropertyAnimation(self.ui.frame_3, b"pos")
        self.anim6.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim6.setEndValue(QPoint(10, 540))
        self.anim6.setDuration(1650)
        self.anim7 = QPropertyAnimation(self.ui.frame_5, b"pos")
        self.anim7.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim7.setEndValue(QPoint(10, 230))
        self.anim7.setDuration(1650)
        self.anim8 = QPropertyAnimation(self.ui.frame_8, b"pos")
        self.anim8.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim8.setEndValue(QPoint(10, 100))
        self.anim8.setDuration(1650)
        self.anim9 = QPropertyAnimation(self.ui.frame_11, b"pos")
        self.anim9.setEndValue(QPoint(1520,100))
        self.anim9.setDuration(1650)
        self.anim10 = QPropertyAnimation(self.ui.tabWidget, b"pos")
        self.anim10.setEndValue(QPoint(1250,130))
        self.anim10.setDuration(1350)
        self.anim11 = QPropertyAnimation(self.ui.frame_4, b"pos")
        self.anim11.setEndValue(QPoint(1250,610))
        self.anim11.setDuration(1300)
        self.anim12 = QPropertyAnimation(self.ui.frame, b'size')
        self.anim12.setStartValue(QtCore.QSize(0, 0))
        self.anim12.setEndValue(QtCore.QSize(0, 0))
        self.anim12.setDuration(1300)

        self.anim.start()
        self.anim2.start()
        self.anim3.start()
        self.anim4.start()
        self.anim5.start()
        self.anim6.start()
        self.anim7.start()
        self.anim8.start()
        self.anim9.start()
        self.anim10.start()
        self.anim11.start()
        self.anim12.start()

    def animation_2(self):
        self.anim = QPropertyAnimation(self.ui.frame, b"pos")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.setEndValue(QPoint(760, 210))
        self.anim.setDuration(2650)

    def shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow2 = QGraphicsDropShadowEffect()
        shadow3 = QGraphicsDropShadowEffect()
        shadow4 = QGraphicsDropShadowEffect()
        shadow5 = QGraphicsDropShadowEffect()
        shadow6 = QGraphicsDropShadowEffect()
        shadow7 = QGraphicsDropShadowEffect()
        shadow8 = QGraphicsDropShadowEffect()
        shadow9 = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow2.setBlurRadius(15)
        shadow3.setBlurRadius(15)
        shadow4.setBlurRadius(15)
        shadow5.setBlurRadius(15)
        shadow6.setBlurRadius(15)
        shadow7.setBlurRadius(15)
        shadow8.setBlurRadius(15)
        shadow9.setBlurRadius(50)
        self.ui.sousuo.setGraphicsEffect(shadow)
        self.ui.frame_9.setGraphicsEffect(shadow2)
        self.ui.frame_8.setGraphicsEffect(shadow3)
        self.ui.frame_5.setGraphicsEffect(shadow4)
        self.ui.frame_3.setGraphicsEffect(shadow5)
        self.ui.tabWidget.setGraphicsEffect(shadow6)
        self.ui.frame_4.setGraphicsEffect(shadow7)
        self.ui.frame_7.setGraphicsEffect(shadow8)
        self.ui.frame.setGraphicsEffect(shadow9)

    def widgets_binding(self):
        self.ui.pushButton_11.clicked.connect(self.chufa10)
        self.ui.xiadan_zuoduo.clicked.connect(self.chufa6)
        self.ui.xiadan_zuokong.clicked.connect(self.chufa7)
        self.ui.pushButton_9.clicked.connect(self.chufa8)
        self.ui.pushButton_10.clicked.connect(self.chufa9)
        self.ui.lishidingdan_2.clicked.connect(self.chufa12)
        self.ui.pushButton_16.clicked.connect(self.chufa13)
        self.ui.lishidingdan.clicked.connect(self.openWindow)
        self.ui.horizontalSlider.valueChanged.connect(self.valuechange)
        self.ui.pushButton_18.clicked.connect(self.toggletop)
        self.ui.pushButton_17.clicked.connect(self.chufa14)
        self.ui.pushButton_3.clicked.connect(self.chufa15)

    def toggletop(self):
        on = bool(self.windowFlags() & QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, not on)
        self.show()

    def pair_base(self):
        pairs_list = []
        allinfo_pairs = self.c.book_ticker()
        for elements in allinfo_pairs:
            x = str(elements["symbol"])
            pairs_list.append(x)
        self.completer = QCompleter(pairs_list)
        self.completer.setCaseSensitivity(0)
        self.ui.sousuo.setCompleter(self.completer)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = lishi_MainWindow()
        self.ui2.setupUi(self.window)
        self.window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        row = 0
        length = len(self.c.get_order_history())
        self.ui2.tableWidget.setRowCount(length)
        for elements in self.c.get_order_history():
            self.ui2.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(elements['market'])))
            self.ui2.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(elements['price'])))
            self.ui2.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(elements['side'])))
            self.ui2.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(elements['size'])))
            self.ui2.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(elements['avgFillPrice'])))
            self.ui2.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(elements['type'])))
            row += 1
        self.window.show()



    def chufa(self):
        thread = Thread(target=self.thread)
        thread.start()

    def chufa3(self):
        thread = Thread(target=self.dangriyingli)
        thread.start()

    def chufa4(self):
        thread = Thread(target=self.jilu)
        thread.start()

    def chufa5(self):
        thread = Thread(target=self.jiage)
        thread.start()

    def chufa6(self):
        thread = Thread(target=self.long_order)
        thread.start()

    def chufa7(self):
        thread = Thread(target=self.short_order)
        thread.start()

    def chufa8(self):
        thread = Thread(target=self.long_order2)
        thread.start()

    def chufa9(self):
        thread = Thread(target=self.short_order2)
        thread.start()

    def chufa10(self):
        thread = Thread(target=self.market_name)
        thread.start()

    def chufa11(self):
        thread = Thread(target=self.check_limit)
        thread.start()

    def chufa12(self):
        thread = Thread(target=self.cancelorders)
        thread.start()

    def chufa13(self):
        thread = Thread(target=self.getprice)
        thread.start()

    def chufa14(self):
        thread = Thread(target=self.quanping)
        thread.start()

    def chufa15(self):
        thread = Thread(target=self.modify)
        thread.start()

    def getprice(self):
        price2 = self.ui.pushButton_16.text()
        self.ui.xianjia.setText(price2)

    def calculate_positionsize(self):
        risk = self.ui.doubleSpinBox.value()
        entry = float(self.ui.xiadan_ruchang.text())
        stop_loss = float(self.ui.xiadan_zhiying.text())
        sl_percent = abs(stop_loss - entry) * 100 / entry
        position_size = risk * self.usd / sl_percent
        position_size1 = position_size / entry
        return position_size1

    def quanping(self):
        number = self.ui.comboBox_2.currentText()
        x = int(number)
        while True:
            try:
                if x <= len(self.label):
                    if self.label[x - 1] == 'sell':
                        side = 'buy'
                    else:
                        side = 'sell'
                    self.c.place_order(market=self.labels7[x - 1], side=side, size=self.labels4[x - 1], type='market',
                                       reduce_only=True, price=None, post_only=False)
                    break
                else:
                    time.sleep(0.2)
                    continue
            except:
                print('quanping')

    def long_order(self):
        market = self.ui.label.text()
        ruchang = float(self.ui.xiadan_ruchang.text())
        zhisun = float(self.ui.xiadan_zhiying.text())
        if self.ui.xiadan_jiancang.isChecked():
            type1 = 'market'
        else:
            type1 = 'limit'
        if self.ui.xiadan_maker.isChecked():
            post_only = True
        else:
            post_only = False
        self.c.place_order(market=market, side='buy', price=ruchang, size=self.calculate_positionsize(),
                           type=type1, reduce_only=False, ioc=False, post_only=post_only)
        if self.ui.xiadan_zhisun_2.text() != '':
            zhiying = float(self.ui.xiadan_zhisun_2.text())
            self.c.place_order(market=market, side='sell', price=zhiying,
                               size=self.calculate_positionsize(), type=type1,
                               reduce_only=False, ioc=False, post_only=post_only)

        self.c.place_conditional_order(market=market, side='sell', size=self.calculate_positionsize(), type='stop',
                                       reduce_only=True, trigger_price=zhisun)

    def short_order(self):
        market = self.ui.label.text()
        ruchang = float(self.ui.xiadan_ruchang.text())
        zhisun = float(self.ui.xiadan_zhiying.text())
        if self.ui.xiadan_jiancang.isChecked() == True:
            type1 = 'market'
        else:
            type1 = 'limit'
        if self.ui.xiadan_maker.isChecked() == True:
            post_only = True
        else:
            post_only = False
        self.c.place_order(market=market, side='sell', price=ruchang, size=self.calculate_positionsize(),
                           type=type1, reduce_only=False, ioc=False, post_only=post_only)
        if self.ui.xiadan_zhisun_2.text() != '':
            zhiying = float(self.ui.xiadan_zhisun_2.text())
            self.c.place_order(market=market, side='buy', price=zhiying,
                               size=self.calculate_positionsize(), type=type1,
                               reduce_only=False, ioc=False, post_only=post_only)

        self.c.place_conditional_order(market=market, side='buy', size=self.calculate_positionsize(), type='stop',
                                       reduce_only=True, trigger_price=zhisun)

    def long_order2(self):
        market = self.ui.label.text()
        cangwei = float(self.ui.cangwei.text())
        if self.ui.comboBox.currentText() == '限价':  # OK
            string1 = self.ui.riyingkuipercent.text()
            float1 = int(float(string1[0:4]) * 100)
            if float1 <= -200:
                self.ui.pushButton_9.setEnabled(False)
            else:
                xianjia = float(self.ui.xianjia.text())
                self.c.place_order(market=market, side='buy', price=xianjia, size=cangwei, type='limit',
                                   reduce_only=False, ioc=False, post_only=True)
        if self.ui.comboBox.currentText() == '限价止损':  # OK
            xianjia = float(self.ui.xianjia.text())
            trigger_price = float(self.ui.chufajia.text())
            self.c.place_conditional_order(market=market, side='buy', size=cangwei, type='stop', limit_price=xianjia,
                                           reduce_only=True, trigger_price=trigger_price)
        if self.ui.comboBox.currentText() == '市价':  # OK
            string1 = self.ui.riyingkuipercent.text()
            float1 = int(float(string1[0:4]) * 100)
            if float1 <= -200:
                self.ui.pushButton_9.setEnabled(False)
            else:
                self.c.place_order(market=market, side='buy', size=cangwei, type='market',
                                   reduce_only=False, price=None, post_only=False)
        if self.ui.comboBox.currentText() == '市价止损':  # OK
            trigger_price = float(self.ui.chufajia.text())
            self.c.place_conditional_order(market=market, side='buy', size=cangwei, type='stop',
                                           reduce_only=True, trigger_price=trigger_price)

    def short_order2(self):
        market = self.ui.label.text()
        cangwei = float(self.ui.cangwei.text())
        if self.ui.comboBox.currentText() == '限价':  # OK
            string1 = self.ui.riyingkuipercent.text()
            float1 = int(float(string1[0:4]) * 100)
            if float1 <= -200:
                self.ui.pushButton_10.setEnabled(False)
            else:
                xianjia = float(self.ui.xianjia.text())
                self.c.place_order(market=market, side='sell', price=xianjia, size=cangwei, type='limit',
                                   reduce_only=False, ioc=False, post_only=True)
        if self.ui.comboBox.currentText() == '限价止损':  # OK
            xianjia = float(self.ui.xianjia.text())
            trigger_price = float(self.ui.chufajia.text())
            self.c.place_conditional_order(market=market, side='sell', size=cangwei, type='stop', limit_price=xianjia,
                                           reduce_only=True, trigger_price=trigger_price)
        if self.ui.comboBox.currentText() == '市价':  # OK
            string1 = self.ui.riyingkuipercent.text()
            float1 = int(float(string1[0:4]) * 100)
            if float1 <= -200:
                self.ui.pushButton_10.setEnabled(False)
            else:
                self.c.place_order(market=market, side='sell', size=cangwei, type='market',
                                   reduce_only=False, price=None, post_only=False)
        if self.ui.comboBox.currentText() == '市价止损':  # OK
            trigger_price = float(self.ui.chufajia.text())
            self.c.place_conditional_order(market=market, side='sell', size=cangwei, type='stop',
                                           reduce_only=True, trigger_price=trigger_price)

    def market_name(self):
        initname = self.ui.sousuo.text()
        pairs = []
        allinfo = self.c.book_ticker()
        for elements in allinfo:
            pairs.append(elements["symbol"])
        f = set(pairs)
        if initname in f:
            self.ui.label.setText(initname)

    def check_limit(self):
        while True:
            try:
                string1 = self.ui.riyingkuipercent.text()
                float1 = int(float(string1[0:4]) * 100)
                if float1 <= -200:
                    self.ui.xiadan_zuoduo.setEnabled(False)
                    self.ui.xiadan_zuokong.setEnabled(False)
                else:
                    self.ui.pushButton_9.setEnabled(True)
                    self.ui.pushButton_10.setEnabled(True)
                    self.ui.xiadan_zuoduo.setEnabled(True)
                    self.ui.xiadan_zuokong.setEnabled(True)
                time.sleep(1)
            except:
                print('check_limit')

    def jiage(self):
        while True:
            try:
                self.usd = self.c.get_total_usd_balance()
                self.timenow = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                self.ui.label_10.setText(self.timenow)
                time.sleep(1)
                if self.ui.label.text() != 'N/A':
                    pair_price = self.c.get_market(market_name=self.ui.label.text())
                    pri = pair_price['price']
                    self.ui.pushButton_16.setText(str(pri))
                else:
                    continue
            except:
                print('jiege')

    def dangriyingli(self):
        try:
            today = datetime.date.today()
            h = str(today)
            milli = datetime.datetime.strptime(h, '%Y-%m-%d').timestamp()
            yesterdaytime = int(milli)
            list1 = []
            compare = []
            with open('D:\初始资金\hisbalance.txt', 'r') as sample:
                for line in sample:
                    line = json.loads(line.strip())
                    list1.append(line)
            for recorded_time in list1:
                if recorded_time['Time'] < yesterdaytime and recorded_time['Balance'] > 0.0:
                    compare.append(recorded_time['Time'])
            while True:
                for element in list1:
                    if element['Time'] == max(compare):
                        calculated_profit = (self.usd - element['Balance']) * 100 / element['Balance']
                        self.daily_profit = '%.2f' % calculated_profit
                        daily_profitper = calculated_profit * 50
                        self.progress.set_value(daily_profitper)
                        hebing = self.daily_profit + ' %'
                        if float(self.daily_profit) > 0:
                            color = '#%02x%02x%02x' % (113, 255, 70)
                        else:
                            color = '#%02x%02x%02x' % (205, 70, 70)
                        self.progress.color = color
                        self.ui.riyingkuipercent.setStyleSheet("font: 24pt \"Segoe UI\";\n"f"color: {color};")
                        self.ui.riyingkuipercent.setText(hebing)
                        time.sleep(3)
        except:
            print('dangriyingli')
            time.sleep(60)
            self.chufa3()

    def modify(self):
        if self.ui.comboBox_3.currentText() == "价格":
            self.c.modify_order(existing_order_id=self.ui.id.text(), price=float(self.ui.lineEdit.text()))
        else:
            self.c.modify_order(existing_order_id=self.ui.id.text(),
                                size=float(self.ui.lineEdit.text()))


    def thread(self):
        while True:
            try:
                self.labels5.clear()
                self.labels7.clear()
                self.labels3.clear()
                self.labels4.clear()
                self.labels2.clear()
                self.labels8.clear()
                self.labels9.clear()
                self.labels10.clear()
                self.label.clear()
                position = self.c.get_positions()
                openposition = list(filter(lambda d: d['netSize'] != 0, position))
                openorders = self.c.get_open_orders()
                for open in openorders:
                    self.labels2.append(open['market'])
                for open in openorders:
                    self.labels8.append(open['size'])
                for open in openorders:
                    self.labels9.append(open['side'])
                for open in openorders:
                    self.labels10.append(open['id'])
                for future in openposition:
                    self.labels7.append(future["future"])
                for name in self.labels7:
                    self.labels5.append(self.c.get_market(market_name=name)['price'])
                for Entryp in openposition:
                    self.labels3.append(Entryp["recentAverageOpenPrice"])
                for opensize in openposition:
                    self.labels4.append(opensize["size"])
                for opensize in openposition:
                    self.label.append(opensize["side"])
                self.labels2 = list(map(str, self.labels2))
                self.labels3 = list(map(str, self.labels3))
                self.labels4 = list(map(str, self.labels4))
                self.labels5 = list(map(str, self.labels5))
                self.labels8 = list(map(str, self.labels8))
                self.labels9 = list(map(str, self.labels9))
                self.label = list(map(str, self.label))
                self.labels10 = list(map(str, self.labels10))
                chen = "\n\n".join(self.labels3)
                cang = "\n\n".join(self.labels4)
                pin = "\n\n".join(self.labels7)
                pin2 = "\n".join(self.labels2)
                xian = "\n\n".join(self.labels5)
                size2 = "\n".join(self.labels8)
                side3 = "\n".join(self.labels9)
                side4 = "\n".join(self.labels10)
                self.ui.chengbenjia.setText(chen)
                self.ui.cangwei_2.setText(cang)
                self.ui.pinzhong.setText(pin)
                self.ui.xianjia_2.setText(xian)
                self.ui.label_25.setText(pin2)
                self.ui.label_26.setText(size2)
                self.ui.label_27.setText(side3)
                self.ui.label_16.setText(side4)
                per = round((self.usd - float(zijin)) * 100 / float(zijin), 2)
                bal = round(self.usd, 2)
                percent = str(per)
                zhzj = str(bal)
                self.ui.zhanghuzijin.setText(zhzj)
                self.ui.yingli.setText(percent)
                time.sleep(3)
            except:
                print('thread')
                self.chufa()

    def jilu(self):
        while True:
            try:
                with open('D:\初始资金\hisbalance.txt', 'a') as hisbalance:
                    time_now = datetime.datetime.now().timestamp()
                    time_convert = int(time_now)
                    result = {'Time': time_convert,
                              'Balance': self.usd
                              }
                    for dic in [result]:
                        hisbalance.write('{}\n'.format(json.dumps(dic)))
                size = os.path.getsize('D:\初始资金\hisbalance.txt') / 1024 ** 2
                time.sleep(60)
                if size > 10:
                    os.remove('D:\初始资金\hisbalance.txt')
            except:
                print('jilu')

    def valuechange(self):
        pric = self.ui.pushButton_16.text()
        value = self.ui.horizontalSlider.value()
        self.ui.label_14.setStyleSheet("#label_14{font: 10pt \"Segoe UI\";\n"
                                       "color: rgb(255, 255, 255);}")
        self.ui.label_14.setText(str(value) + '%')
        if pric != '0.0':
            full = self.usd / float(pric)
            value = self.ui.horizontalSlider.value()
            siz = full * value / 100
            digit = '%.2f' % siz
            self.ui.cangwei.setText(digit)

    def cancelorders(self):
        self.c.cancel_orders()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FTXWindow()
    win.show()
    sys.exit(app.exec_())
