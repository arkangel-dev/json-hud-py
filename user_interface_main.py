# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user-interface-main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 589)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 761, 530))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_year = QtWidgets.QWidget()
        self.tab_year.setObjectName("tab_year")
        self.groupBox = QtWidgets.QGroupBox(self.tab_year)
        self.groupBox.setGeometry(QtCore.QRect(250, 10, 490, 150))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 100, 20))
        self.label.setObjectName("label")
        self.linedit_add_year = QtWidgets.QLineEdit(self.groupBox)
        self.linedit_add_year.setGeometry(QtCore.QRect(150, 30, 191, 22))
        self.linedit_add_year.setObjectName("linedit_add_year")
        self.button_add_year = QtWidgets.QPushButton(self.groupBox)
        self.button_add_year.setGeometry(QtCore.QRect(10, 80, 130, 30))
        self.button_add_year.setObjectName("button_add_year")
        self.button_delete_year = QtWidgets.QPushButton(self.groupBox)
        self.button_delete_year.setGeometry(QtCore.QRect(10, 110, 130, 30))
        self.button_delete_year.setObjectName("button_delete_year")
        self.list_year = QtWidgets.QListWidget(self.tab_year)
        self.list_year.setGeometry(QtCore.QRect(20, 20, 221, 460))
        self.list_year.setObjectName("list_year")
        self.tabWidget.addTab(self.tab_year, "")
        self.tab_prog = QtWidgets.QWidget()
        self.tab_prog.setObjectName("tab_prog")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_prog)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 10, 490, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 160, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 30, 190, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.button_year_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_year_2.setGeometry(QtCore.QRect(10, 80, 130, 30))
        self.button_year_2.setObjectName("button_year_2")
        self.button_year_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.button_year_5.setGeometry(QtCore.QRect(10, 110, 130, 30))
        self.button_year_5.setObjectName("button_year_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_prog)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 160, 490, 150))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 160, 20))
        self.label_3.setObjectName("label_3")
        self.button_year_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.button_year_3.setGeometry(QtCore.QRect(10, 80, 130, 30))
        self.button_year_3.setObjectName("button_year_3")
        self.combo_programme_year = QtWidgets.QComboBox(self.groupBox_3)
        self.combo_programme_year.setGeometry(QtCore.QRect(150, 30, 190, 22))
        self.combo_programme_year.setObjectName("combo_programme_year")
        self.button_year_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.button_year_4.setGeometry(QtCore.QRect(10, 110, 130, 30))
        self.button_year_4.setObjectName("button_year_4")
        self.list_programmes = QtWidgets.QListWidget(self.tab_prog)
        self.list_programmes.setGeometry(QtCore.QRect(20, 20, 221, 460))
        self.list_programmes.setObjectName("list_programmes")
        self.tabWidget.addTab(self.tab_prog, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.list_year_2 = QtWidgets.QListWidget(self.tab)
        self.list_year_2.setGeometry(QtCore.QRect(20, 20, 221, 460))
        self.list_year_2.setObjectName("list_year_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(250, 10, 490, 150))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 100, 20))
        self.label_4.setObjectName("label_4")
        self.button_add_year_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.button_add_year_2.setGeometry(QtCore.QRect(10, 80, 130, 30))
        self.button_add_year_2.setObjectName("button_add_year_2")
        self.button_delete_year_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.button_delete_year_2.setGeometry(QtCore.QRect(10, 110, 130, 30))
        self.button_delete_year_2.setObjectName("button_delete_year_2")
        self.combo_programme_year_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.combo_programme_year_2.setGeometry(QtCore.QRect(150, 30, 180, 22))
        self.combo_programme_year_2.setObjectName("combo_programme_year_2")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.combo_programme_year_2.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.jsonraw = QtWidgets.QTextEdit(self.centralwidget)
        self.jsonraw.setGeometry(QtCore.QRect(780, 130, 310, 417))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.jsonraw.setFont(font)
        self.jsonraw.setReadOnly(False)
        self.jsonraw.setAcceptRichText(False)
        self.jsonraw.setObjectName("jsonraw")
        self.LoadJson = QtWidgets.QPushButton(self.centralwidget)
        self.LoadJson.setGeometry(QtCore.QRect(780, 42, 310, 40))
        self.LoadJson.setObjectName("LoadJson")
        self.status_present = QtWidgets.QLabel(self.centralwidget)
        self.status_present.setGeometry(QtCore.QRect(780, 10, 310, 20))
        self.status_present.setStyleSheet("color : rgb(255, 0, 0)")
        self.status_present.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_present.setObjectName("status_present")
        self.LoadJson_2 = QtWidgets.QPushButton(self.centralwidget)
        self.LoadJson_2.setGeometry(QtCore.QRect(780, 82, 310, 40))
        self.LoadJson_2.setObjectName("LoadJson_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 26))
        self.menubar.setObjectName("menubar")
        self.menuHello_World = QtWidgets.QMenu(self.menubar)
        self.menuHello_World.setObjectName("menuHello_World")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionGenerate_JSON = QtWidgets.QAction(MainWindow)
        self.actionGenerate_JSON.setObjectName("actionGenerate_JSON")
        self.actionLoad_JSON = QtWidgets.QAction(MainWindow)
        self.actionLoad_JSON.setObjectName("actionLoad_JSON")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHello_World.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "json-hud"))
        self.groupBox.setTitle(_translate("MainWindow", "Add new year"))
        self.label.setText(_translate("MainWindow", "Enter an year"))
        self.button_add_year.setText(_translate("MainWindow", "Add Year"))
        self.button_delete_year.setText(_translate("MainWindow", "Delete Year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_year), _translate("MainWindow", "Years"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Add new programme"))
        self.label_2.setText(_translate("MainWindow", "Programme name"))
        self.button_year_2.setText(_translate("MainWindow", "Add programme"))
        self.button_year_5.setText(_translate("MainWindow", "Delete programme"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Copy details"))
        self.label_3.setText(_translate("MainWindow", "Year"))
        self.button_year_3.setText(_translate("MainWindow", "Copy details"))
        self.button_year_4.setText(_translate("MainWindow", "Overwite details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prog), _translate("MainWindow", "Programmes"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Add new intake"))
        self.label_4.setText(_translate("MainWindow", "Select an year"))
        self.button_add_year_2.setText(_translate("MainWindow", "Add Intake"))
        self.button_delete_year_2.setText(_translate("MainWindow", "Delete Intake"))
        self.combo_programme_year_2.setItemText(0, _translate("MainWindow", "January"))
        self.combo_programme_year_2.setItemText(1, _translate("MainWindow", "February"))
        self.combo_programme_year_2.setItemText(2, _translate("MainWindow", "March"))
        self.combo_programme_year_2.setItemText(3, _translate("MainWindow", "April"))
        self.combo_programme_year_2.setItemText(4, _translate("MainWindow", "May"))
        self.combo_programme_year_2.setItemText(5, _translate("MainWindow", "June"))
        self.combo_programme_year_2.setItemText(6, _translate("MainWindow", "July"))
        self.combo_programme_year_2.setItemText(7, _translate("MainWindow", "August"))
        self.combo_programme_year_2.setItemText(8, _translate("MainWindow", "September"))
        self.combo_programme_year_2.setItemText(9, _translate("MainWindow", "October"))
        self.combo_programme_year_2.setItemText(10, _translate("MainWindow", "November"))
        self.combo_programme_year_2.setItemText(11, _translate("MainWindow", "December"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Intakes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Session Data"))
        self.LoadJson.setText(_translate("MainWindow", "Load JSON Data"))
        self.status_present.setText(_translate("MainWindow", "This is the sample error message"))
        self.LoadJson_2.setText(_translate("MainWindow", "Copy JSON Data"))
        self.menuHello_World.setTitle(_translate("MainWindow", "JSON"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionGenerate_JSON.setText(_translate("MainWindow", "Generate JSON"))
        self.actionLoad_JSON.setText(_translate("MainWindow", "Load JSON"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
