# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor,QPalette,QPixmap

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from query_request import *
from PyQt5.QtGui import *
import sys
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)    #
        MainWindow.setMinimumSize(QtCore.QSize(800,600)) #
        MainWindow.setMaximumSize(QtCore.QSize(800, 600)) #
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title_img = QtWidgets.QLabel(self.centralwidget)
        self.label_title_img.setGeometry(QtCore.QRect(0, 0, 800, 90)) #
        self.label_title_img.setObjectName("label_title_img")
        self.label_title_img.setAutoFillBackground(True)
        palette1=QPalette()     #
        palette1.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('4.jpg')))    #
        self.label_title_img.setPalette(palette1)    #
        #title_img = QPixmap('1.jpg')
        #self.label_title_img.setPixmap(title_img)
        self.label_train_img = QtWidgets.QLabel(self.centralwidget)
        self.label_train_img.setGeometry(QtCore.QRect(0, 210, 800, 40))
        self.label_train_img.setObjectName("label_train_img")
        train_img = QPixmap('3.png')  # 打开火车信息位图
        self.label_train_img.setPixmap(train_img)  # 设置调色板

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 250, 801, 321))
        self.tableView.setObjectName("tableView")
        self.model = QStandardItemModel()  #创建存储数据的模式
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableView.setFont(font)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 100, 800, 80))
        self.widget.setObjectName("widget")
        self.widget.setAutoFillBackground(True)   #
        #palette = QPalette()  #
        #palette.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('1.jpg')))  #
        #self.widget.setPalette(palette)  #
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(430, 20, 72, 15))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(640, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(80, 10, 101, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setGeometry(QtCore.QRect(280, 10, 101, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setGeometry(QtCore.QRect(500, 10, 101, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 160, 791, 61))
        self.widget_2.setObjectName("widget_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(140, 20, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 20, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_3.setGeometry(QtCore.QRect(380, 20, 91, 19))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_4.setGeometry(QtCore.QRect(490, 20, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_5.setGeometry(QtCore.QRect(610, 20, 91, 19))
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 72, 15))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "查询余票"))
        self.checkBox_4.setText(_translate("MainWindow", "T-特快"))
        self.checkBox_5.setText(_translate("MainWindow", "K-快速"))
        self.checkBox_3.setText(_translate("MainWindow", "Z-直达"))
        self.checkBox_2.setText(_translate("MainWindow", "D-动车"))
        self.checkBox.setText(_translate("MainWindow", "GC-高铁"))
        self.label.setText(_translate("MainWindow", "出发地："))
        self.label_2.setText(_translate("MainWindow", "目的地："))
        self.label_3.setText(_translate("MainWindow", "出发日："))
        self.pushButton.setText(_translate("MainWindow", "查询"))

        self.textEdit_3.setText(get_time())  # 出发日显示当天日期
        self.pushButton.clicked.connect(self.on_click)  # 查询按钮指定单击事件的方法
        self.checkBox.stateChanged.connect(self.change_G)  # 高铁选中与取消事件
        self.checkBox_2.stateChanged.connect(self.change_D)  # 动车选中与取消事件
        self.checkBox_3.stateChanged.connect(self.change_Z)  # 直达车选中与取消事件
        self.checkBox_4.stateChanged.connect(self.change_T)  # 特快车选中与取消事件
        self.checkBox_5.stateChanged.connect(self.change_K)  # 快车选中与取消事件




    def change_G(self, state):
        if state == QtCore.Qt.Checked:
            g_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_g_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def change_D(self, state):
        if state == QtCore.Qt.Checked:
            d_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_d_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def change_Z(self, state):
        if state == QtCore.Qt.Checked:
            z_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_z_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def change_T(self, state):
        if state == QtCore.Qt.Checked:
            t_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_t_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def change_K(self, state):
        if state == QtCore.Qt.Checked:
            k_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_k_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    def checkBox_default(self):
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)


    def messageDialog(self,title,message):
        msg_box = QMessageBox(QMessageBox.Warning,title,message)  #information，question和warning分别表示弹出的窗口标题是感叹号，问号或叉号
        msg_box.exec_()
        #调用show()的作用仅仅是将widget及其上的内容都显示出来，
        # 控制权即刻返回给调用函数。而调用exec()后，调用线程将会被阻塞，锁住程序直到用户关闭该对话框，
        # 期间用户不可以切换同程序下的其它窗口直到Dialog关闭。

    def displayTable(self,train,info,data):
        self.model.clear()
        for row in range(train):
            for column in range(info):
                item = QStandardItem(data[row][column])
                self.model.setItem(row,column,item)
        #self.tableView = QTableView()
        self.tableView.setModel(self.model)

    def on_click(self):
        get_from = self.textEdit.toPlainText()
        get_to = self.textEdit_2.toPlainText()
        get_date = self.textEdit_3.toPlainText()

        if isStations() == True:
            stations = eval(read())  #字符串转字典
            if get_from != "" and get_to !="" and get_date !="" :
                if get_from in stations and get_to in stations and is_valid_date(get_date) :
                    inputYearDay = time.strptime(get_date,'%Y-%m-%d').tm_yday  #天数差
                    yearToday = time.localtime(time.time()).tm_yday
                    timeDifference = inputYearDay - yearToday
                    if timeDifference>= 0 and timeDifference<=28:
                        from_station = stations[get_from]
                        to_station = stations[get_to]
                        data = query(get_date,from_station,to_station)
                        self.checkBox_default()
                        if len(data) != 0:
                            self.displayTable(len(data),16,data)
                        else:
                            self.messageDialog('警告','没有返回的数据！')
                    else:
                        self.messageDialog('警告','超出查询日期范围')
                else:
                    self.messageDialog('警告','输入站名不正确或日期不正确')
            else:
                self.messageDialog('警告','输入不能为空')
        else:
            self.messageDialog('警告','未下载车站查询文件')






def get_time():
    now = int(time.time())
    timeStruct = time.localtime(now)
    strTime = time.strftime('%Y-%m-%d',timeStruct)
    return strTime

def is_valid_date(str):
    try:
        time.strptime(str,'%Y-%m-%d')
        return True
    except:
        return False

def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    if isStations() == False:
        getStation()
        show_MainWindow()
    else:
        show_MainWindow()






