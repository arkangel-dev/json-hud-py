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
        MainWindow.resize(1099, 583)
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
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_year)
        self.groupBox_8.setGeometry(QtCore.QRect(250, 160, 490, 140))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_8)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 160, 20))
        self.label_9.setObjectName("label_9")
        self.clone_year_button = QtWidgets.QPushButton(self.groupBox_8)
        self.clone_year_button.setGeometry(QtCore.QRect(10, 100, 130, 30))
        self.clone_year_button.setObjectName("clone_year_button")
        self.clone_from_year = QtWidgets.QComboBox(self.groupBox_8)
        self.clone_from_year.setGeometry(QtCore.QRect(150, 30, 190, 22))
        self.clone_from_year.setObjectName("clone_from_year")
        self.linedit_add_year_2 = QtWidgets.QLineEdit(self.groupBox_8)
        self.linedit_add_year_2.setGeometry(QtCore.QRect(150, 60, 191, 22))
        self.linedit_add_year_2.setObjectName("linedit_add_year_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_year, "")
        self.tab_prog = QtWidgets.QWidget()
        self.tab_prog.setObjectName("tab_prog")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_prog)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 10, 490, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 160, 20))
        self.label_2.setObjectName("label_2")
        self.programme_name_add = QtWidgets.QLineEdit(self.groupBox_2)
        self.programme_name_add.setGeometry(QtCore.QRect(150, 30, 190, 22))
        self.programme_name_add.setObjectName("programme_name_add")
        self.button_add_programme = QtWidgets.QPushButton(self.groupBox_2)
        self.button_add_programme.setGeometry(QtCore.QRect(10, 80, 130, 30))
        self.button_add_programme.setObjectName("button_add_programme")
        self.button_delete_programme = QtWidgets.QPushButton(self.groupBox_2)
        self.button_delete_programme.setGeometry(QtCore.QRect(10, 110, 130, 30))
        self.button_delete_programme.setObjectName("button_delete_programme")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_prog)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 160, 490, 140))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 160, 20))
        self.label_3.setObjectName("label_3")
        self.button_year_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.button_year_3.setGeometry(QtCore.QRect(10, 100, 130, 30))
        self.button_year_3.setObjectName("button_year_3")
        self.clone_from_programmes = QtWidgets.QComboBox(self.groupBox_3)
        self.clone_from_programmes.setGeometry(QtCore.QRect(150, 30, 190, 22))
        self.clone_from_programmes.setObjectName("clone_from_programmes")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.label_18.setObjectName("label_18")
        self.linedit_add_year_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.linedit_add_year_3.setGeometry(QtCore.QRect(150, 60, 191, 22))
        self.linedit_add_year_3.setObjectName("linedit_add_year_3")
        self.list_programmes = QtWidgets.QListWidget(self.tab_prog)
        self.list_programmes.setGeometry(QtCore.QRect(20, 20, 221, 460))
        self.list_programmes.setObjectName("list_programmes")
        self.tabWidget.addTab(self.tab_prog, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.list_intakes = QtWidgets.QListWidget(self.tab)
        self.list_intakes.setGeometry(QtCore.QRect(20, 20, 221, 460))
        self.list_intakes.setObjectName("list_intakes")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(250, 10, 490, 150))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 140, 20))
        self.label_4.setObjectName("label_4")
        self.button_add_intake = QtWidgets.QPushButton(self.groupBox_4)
        self.button_add_intake.setGeometry(QtCore.QRect(10, 80, 130, 30))
        self.button_add_intake.setObjectName("button_add_intake")
        self.button_delete_intake = QtWidgets.QPushButton(self.groupBox_4)
        self.button_delete_intake.setGeometry(QtCore.QRect(10, 110, 130, 30))
        self.button_delete_intake.setObjectName("button_delete_intake")
        self.combo_intake = QtWidgets.QComboBox(self.groupBox_4)
        self.combo_intake.setGeometry(QtCore.QRect(170, 30, 180, 22))
        self.combo_intake.setObjectName("combo_intake")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.combo_intake.addItem("")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(250, 160, 490, 140))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 160, 20))
        self.label_5.setObjectName("label_5")
        self.button_year_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.button_year_4.setGeometry(QtCore.QRect(10, 100, 130, 30))
        self.button_year_4.setObjectName("button_year_4")
        self.clone_from_intakes = QtWidgets.QComboBox(self.groupBox_5)
        self.clone_from_intakes.setGeometry(QtCore.QRect(150, 30, 190, 22))
        self.clone_from_intakes.setObjectName("clone_from_intakes")
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.label_19.setObjectName("label_19")
        self.combo_intake_2 = QtWidgets.QComboBox(self.groupBox_5)
        self.combo_intake_2.setGeometry(QtCore.QRect(150, 60, 190, 22))
        self.combo_intake_2.setObjectName("combo_intake_2")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.combo_intake_2.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.list_sessions = QtWidgets.QListWidget(self.tab_2)
        self.list_sessions.setGeometry(QtCore.QRect(20, 40, 221, 440))
        self.list_sessions.setObjectName("list_sessions")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(250, 20, 500, 460))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.table_sessions = QtWidgets.QTableWidget(self.tab_5)
        self.table_sessions.setGeometry(QtCore.QRect(10, 10, 480, 411))
        self.table_sessions.setObjectName("table_sessions")
        self.table_sessions.setColumnCount(6)
        self.table_sessions.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        item.setFont(font)
        self.table_sessions.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_sessions.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_sessions.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_sessions.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_sessions.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_sessions.setHorizontalHeaderItem(5, item)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 470, 350))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 140, 20))
        self.label_7.setObjectName("label_7")
        self.combo_programme_year_5 = QtWidgets.QComboBox(self.groupBox_6)
        self.combo_programme_year_5.setGeometry(QtCore.QRect(170, 30, 210, 22))
        self.combo_programme_year_5.setObjectName("combo_programme_year_5")
        self.combo_programme_year_5.addItem("")
        self.combo_programme_year_5.addItem("")
        self.combo_programme_year_5.addItem("")
        self.combo_programme_year_5.addItem("")
        self.combo_programme_year_5.addItem("")
        self.combo_programme_year_5.addItem("")
        self.combo_programme_year_5.addItem("")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 140, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 210, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 140, 20))
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 90, 210, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(10, 120, 140, 20))
        self.label_12.setObjectName("label_12")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 120, 210, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox.setGeometry(QtCore.QRect(6, 206, 110, 30))
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setObjectName("checkBox")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(10, 150, 140, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(10, 180, 140, 20))
        self.label_14.setObjectName("label_14")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_6)
        self.timeEdit.setGeometry(QtCore.QRect(170, 150, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.groupBox_6)
        self.timeEdit_2.setGeometry(QtCore.QRect(170, 180, 118, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.button_add_year_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.button_add_year_3.setGeometry(QtCore.QRect(10, 250, 130, 30))
        self.button_add_year_3.setObjectName("button_add_year_3")
        self.button_delete_year_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.button_delete_year_3.setGeometry(QtCore.QRect(10, 310, 130, 30))
        self.button_delete_year_3.setObjectName("button_delete_year_3")
        self.button_delete_year_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.button_delete_year_4.setGeometry(QtCore.QRect(10, 280, 130, 30))
        self.button_delete_year_4.setObjectName("button_delete_year_4")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 470, 140))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 160, 20))
        self.label_6.setObjectName("label_6")
        self.button_year_6 = QtWidgets.QPushButton(self.groupBox_7)
        self.button_year_6.setGeometry(QtCore.QRect(10, 100, 130, 30))
        self.button_year_6.setObjectName("button_year_6")
        self.combo_programme_year_4 = QtWidgets.QComboBox(self.groupBox_7)
        self.combo_programme_year_4.setGeometry(QtCore.QRect(150, 30, 190, 22))
        self.combo_programme_year_4.setObjectName("combo_programme_year_4")
        self.label_20 = QtWidgets.QLabel(self.groupBox_7)
        self.label_20.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.label_20.setObjectName("label_20")
        self.linedit_add_year_5 = QtWidgets.QLineEdit(self.groupBox_7)
        self.linedit_add_year_5.setGeometry(QtCore.QRect(150, 60, 191, 22))
        self.linedit_add_year_5.setObjectName("linedit_add_year_5")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.combo_list_select_day = QtWidgets.QComboBox(self.tab_2)
        self.combo_list_select_day.setGeometry(QtCore.QRect(20, 10, 220, 22))
        self.combo_list_select_day.setObjectName("combo_list_select_day")
        self.combo_list_select_day.addItem("")
        self.combo_list_select_day.addItem("")
        self.combo_list_select_day.addItem("")
        self.combo_list_select_day.addItem("")
        self.combo_list_select_day.addItem("")
        self.combo_list_select_day.addItem("")
        self.combo_list_select_day.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        self.jsonraw = QtWidgets.QTextEdit(self.centralwidget)
        self.jsonraw.setGeometry(QtCore.QRect(780, 130, 310, 417))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.jsonraw.setFont(font)
        self.jsonraw.setReadOnly(False)
        self.jsonraw.setAcceptRichText(False)
        self.jsonraw.setObjectName("jsonraw")
        self.LoadJson = QtWidgets.QPushButton(self.centralwidget)
        self.LoadJson.setGeometry(QtCore.QRect(780, 42, 310, 40))
        self.LoadJson.setObjectName("LoadJson")
        self.status_present = QtWidgets.QLabel(self.centralwidget)
        self.status_present.setGeometry(QtCore.QRect(269, 10, 821, 20))
        self.status_present.setStyleSheet("color : rgb(255, 0, 0)")
        self.status_present.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_present.setObjectName("status_present")
        self.LoadJson_2 = QtWidgets.QPushButton(self.centralwidget)
        self.LoadJson_2.setGeometry(QtCore.QRect(780, 82, 310, 40))
        self.LoadJson_2.setObjectName("LoadJson_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionGenerate_JSON = QtWidgets.QAction(MainWindow)
        self.actionGenerate_JSON.setObjectName("actionGenerate_JSON")
        self.actionLoad_JSON = QtWidgets.QAction(MainWindow)
        self.actionLoad_JSON.setObjectName("actionLoad_JSON")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionInfo_2 = QtWidgets.QAction(MainWindow)
        self.actionInfo_2.setObjectName("actionInfo_2")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionInfo_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "json-hud"))
        self.groupBox.setTitle(_translate("MainWindow", "Add new year"))
        self.label.setText(_translate("MainWindow", "Enter an year"))
        self.button_add_year.setText(_translate("MainWindow", "Add Year"))
        self.button_delete_year.setText(_translate("MainWindow", "Delete Year"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Clone Year"))
        self.label_9.setText(_translate("MainWindow", "Clone from"))
        self.clone_year_button.setText(_translate("MainWindow", "Clone"))
        self.label_10.setText(_translate("MainWindow", "Clone to"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_year), _translate("MainWindow", "Years"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Add new programme"))
        self.label_2.setText(_translate("MainWindow", "Programme name"))
        self.button_add_programme.setText(_translate("MainWindow", "Add programme"))
        self.button_delete_programme.setText(_translate("MainWindow", "Delete programme"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Clone Programme"))
        self.label_3.setText(_translate("MainWindow", "Clone from"))
        self.button_year_3.setText(_translate("MainWindow", "Clone"))
        self.label_18.setText(_translate("MainWindow", "Clone to"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prog), _translate("MainWindow", "Programmes"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Add new intake"))
        self.label_4.setText(_translate("MainWindow", "Select an intake month"))
        self.button_add_intake.setText(_translate("MainWindow", "Add Intake"))
        self.button_delete_intake.setText(_translate("MainWindow", "Delete Intake"))
        self.combo_intake.setItemText(0, _translate("MainWindow", "January"))
        self.combo_intake.setItemText(1, _translate("MainWindow", "February"))
        self.combo_intake.setItemText(2, _translate("MainWindow", "March"))
        self.combo_intake.setItemText(3, _translate("MainWindow", "April"))
        self.combo_intake.setItemText(4, _translate("MainWindow", "May"))
        self.combo_intake.setItemText(5, _translate("MainWindow", "June"))
        self.combo_intake.setItemText(6, _translate("MainWindow", "July"))
        self.combo_intake.setItemText(7, _translate("MainWindow", "August"))
        self.combo_intake.setItemText(8, _translate("MainWindow", "September"))
        self.combo_intake.setItemText(9, _translate("MainWindow", "October"))
        self.combo_intake.setItemText(10, _translate("MainWindow", "November"))
        self.combo_intake.setItemText(11, _translate("MainWindow", "December"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Clone Intakes"))
        self.label_5.setText(_translate("MainWindow", "Clone from"))
        self.button_year_4.setText(_translate("MainWindow", "Clone"))
        self.label_19.setText(_translate("MainWindow", "Clone to"))
        self.combo_intake_2.setItemText(0, _translate("MainWindow", "January"))
        self.combo_intake_2.setItemText(1, _translate("MainWindow", "February"))
        self.combo_intake_2.setItemText(2, _translate("MainWindow", "March"))
        self.combo_intake_2.setItemText(3, _translate("MainWindow", "April"))
        self.combo_intake_2.setItemText(4, _translate("MainWindow", "May"))
        self.combo_intake_2.setItemText(5, _translate("MainWindow", "June"))
        self.combo_intake_2.setItemText(6, _translate("MainWindow", "July"))
        self.combo_intake_2.setItemText(7, _translate("MainWindow", "August"))
        self.combo_intake_2.setItemText(8, _translate("MainWindow", "September"))
        self.combo_intake_2.setItemText(9, _translate("MainWindow", "October"))
        self.combo_intake_2.setItemText(10, _translate("MainWindow", "November"))
        self.combo_intake_2.setItemText(11, _translate("MainWindow", "December"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Intakes"))
        item = self.table_sessions.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Session Name"))
        item = self.table_sessions.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lecturer"))
        item = self.table_sessions.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Start Time"))
        item = self.table_sessions.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "End Time"))
        item = self.table_sessions.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Venue"))
        item = self.table_sessions.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Bring Laptop"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Overview"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Add new session"))
        self.label_7.setText(_translate("MainWindow", "Select a day"))
        self.combo_programme_year_5.setItemText(0, _translate("MainWindow", "Sunday"))
        self.combo_programme_year_5.setItemText(1, _translate("MainWindow", "Monday"))
        self.combo_programme_year_5.setItemText(2, _translate("MainWindow", "Tuesday"))
        self.combo_programme_year_5.setItemText(3, _translate("MainWindow", "Wednesday"))
        self.combo_programme_year_5.setItemText(4, _translate("MainWindow", "Thursday"))
        self.combo_programme_year_5.setItemText(5, _translate("MainWindow", "Friday"))
        self.combo_programme_year_5.setItemText(6, _translate("MainWindow", "Saturday"))
        self.label_8.setText(_translate("MainWindow", "Session name"))
        self.label_11.setText(_translate("MainWindow", "Session Venue"))
        self.label_12.setText(_translate("MainWindow", "Session lecuturer"))
        self.checkBox.setText(_translate("MainWindow", "Laptop needed"))
        self.label_13.setText(_translate("MainWindow", "Start time"))
        self.label_14.setText(_translate("MainWindow", "End time"))
        self.button_add_year_3.setText(_translate("MainWindow", "Add Session"))
        self.button_delete_year_3.setText(_translate("MainWindow", "Delete Session"))
        self.button_delete_year_4.setText(_translate("MainWindow", "Save modification"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Add session"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Clone sessions"))
        self.label_6.setText(_translate("MainWindow", "Clone from"))
        self.button_year_6.setText(_translate("MainWindow", "Clone"))
        self.label_20.setText(_translate("MainWindow", "Clone to"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Clone sessions"))
        self.combo_list_select_day.setItemText(0, _translate("MainWindow", "Sunday"))
        self.combo_list_select_day.setItemText(1, _translate("MainWindow", "Monday"))
        self.combo_list_select_day.setItemText(2, _translate("MainWindow", "Tuesday"))
        self.combo_list_select_day.setItemText(3, _translate("MainWindow", "Wednesday"))
        self.combo_list_select_day.setItemText(4, _translate("MainWindow", "Thursday"))
        self.combo_list_select_day.setItemText(5, _translate("MainWindow", "Friday"))
        self.combo_list_select_day.setItemText(6, _translate("MainWindow", "Saturday"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Sessions"))
        self.LoadJson.setText(_translate("MainWindow", "Load JSON Data"))
        self.status_present.setText(_translate("MainWindow", "This is the sample error message"))
        self.LoadJson_2.setText(_translate("MainWindow", "Copy JSON Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionGenerate_JSON.setText(_translate("MainWindow", "Generate JSON"))
        self.actionLoad_JSON.setText(_translate("MainWindow", "Load JSON"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionInfo_2.setText(_translate("MainWindow", "Info"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

