# import sys
# from PyQt5 import QtWidgets, QtCore
# from user_interface_main import Ui_MainWindow
# import generate
# import json
#
# class mywindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(mywindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         #
#         # From here we defines the actions
#         # Pretty straight foward:
#         # self.ui.<widget_name>.<action>.connnect(<function_name>)
#         #
#         # I think we can define the function as a
#         # function of another file. or a function outside this
#         # class
#         #
#         self.ui.pushButton.clicked.connect(self.GenerateJson)
#
#     def GenerateJson(self):
#         if (self.ui.textEdit.toPlainText()):
#             context_data = json.loads(self.ui.textEdit.toPlainText())
#         else:
#             context_data = {}
#         session_name = self.ui.lineEdit.text()
#         session_venue = self.ui.lineEdit_2.text()
#         session_lecturer = self.ui.lineEdit_3.text()
#
#         if not (session_name or session_venue or session_lecturer):
#             #
#             # please note that you have to use return() where
#             # you'd normally use exit()
#             #
#             return()
#       
#
#         self.ui.textEdit.setText(generate.GenerateJson(context_data, session_name, session_venue, session_lecturer))
#         self.ui.listWidget.addItem(session_name)
#         return()
# #
# # is part is important apparently...
# #
# app = QtWidgets.QApplication([])
# application = mywindow()
# application.show()
# sys.exit(app.exec())

import sys
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,QTime)
from PyQt5.QtGui import QStandardItemModel
from user_interface_main import Ui_MainWindow
import libraries as lib
import json

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #
        # From here we defines the actions
        # Pretty straight foward:
        # self.ui.<widget_name>.<action>.connnect(<function_name>)
        #
        # I think we can define the function as a
        # function of another file. or a function outside this
        # class
        #

        self.ui.LoadJson.clicked.connect(self.LoadData)
        self.ui.button_add_year.clicked.connect(self.add_year)
        self.ui.button_delete_year.clicked.connect(self.delete_year)
        self.ui.list_year.clicked.connect(self.LoadData)
        self.ui.list_programmes.clicked.connect(self.LoadData)
        self.ui.list_intakes.clicked.connect(self.LoadData)
        self.ui.combo_list_select_day.currentTextChanged.connect(self.LoadData)
        self.ui.button_add_programme.clicked.connect(self.add_programme)
        self.ui.button_delete_programme.clicked.connect(self.delete_programm)
        self.ui.button_add_intake.clicked.connect(self.addIntake)
        # self.ui.clone_year_button.clicked.connect(self.testingThing)

        # this is the debug version so I'll hide the status
        # data programmatically here..
        self.ui.status_present.hide()
        global dataloaded
        dataloaded = False
        
    # def testingThing(self):
    #     model = QStandardItemModel(0,3)
    #     model.setHeaderData(0, Qt.Horizontal, "From")
    #     model.setHeaderData(1, Qt.Horizontal, "To")
    #     model.setHeaderData(2, Qt.Horizontal, "LALA")
    #     model.insertRow(0)
    #     model.setData(model.index(0, 0), "mailFrom")
    #     dataView = self.ui.treeView.setModel(model)
    
    def loadJsonData(self):
        #
        # load the data from the json
        # data box in the UI
        #
        jsondata = self.ui.jsonraw.toPlainText()

        #
        # check if the user's json file is valid
        # so that the program wont freak out on the user
        #
        if not lib.is_json(jsondata):
            self.ui.status_present.show()
            self.ui.status_present.setText("*JSON file is invalid")
            return("ERROR")
        
        #
        # load the json file as an actual json
        # file
        #
        # now we clear the listWidgets because just to
        # safe. Im not sure what will happen but I dont
        # wanna find out
        #
        # now we hide the status label
        #
        jsondata = json.loads(jsondata)
        global dataloaded
        dataloaded = True
        self.ui.status_present.hide()
        return(jsondata)


    def LoadData(self):
        #
        # this if the function to load
        # the data from the json data
        #
        jsondata = mywindow.loadJsonData(self)
        if jsondata == "ERROR":
            return()

        #
        # we have to define these to variables
        # so that the system can keep track of what's
        # what
        #
        year_preindex = None
        programme_preindex = None
        intake_preindex = None

        if self.ui.list_year.selectedItems():
            year_preindex = self.ui.list_year.currentRow()
        if self.ui.list_programmes.selectedItems():
            programme_preindex = self.ui.list_programmes.currentRow()
        if self.ui.list_intakes.selectedItems():
            intake_preindex = self.ui.list_intakes.currentRow()

        self.ui.list_year.clear()
        self.ui.clone_from_year.clear()

        self.ui.list_programmes.clear()
        self.ui.clone_from_programmes.clear()

        self.ui.list_intakes.clear()
        self.ui.list_sessions.clear()
        

        #
        # now we are going to add the
        # items in the json file to
        # the ListWidget
        #
        # add all the years from the
        # json file to its list
        #
    
        for x in jsondata:
            self.ui.list_year.addItem(x)
            self.ui.clone_from_year.addItem(x)
        if len(jsondata):
            self.ui.list_year.sortItems()
            #
            # if an year is pre-selected set the
            # cursor to that index
            #
            if year_preindex:
                self.ui.list_year.setCurrentRow(year_preindex)
            else:
                self.ui.list_year.setCurrentRow(0)

        # update the line-edit object
        self.ui.linedit_add_year.setText(self.ui.list_year.currentItem().text())

        # load up the combo box...

        #
        # add all the programmes from the json
        # file to the list
        #
        try:
            for x in jsondata[self.ui.list_year.currentItem().text()]:
                self.ui.clone_from_programmes.addItem(x)
                self.ui.list_programmes.addItem(x)
            if len(jsondata[self.ui.list_year.currentItem().text()]):
                self.ui.list_programmes.sortItems()
                if programme_preindex:
                    self.ui.list_programmes.setCurrentRow(programme_preindex)
                else:
                    self.ui.list_programmes.setCurrentRow(0)

            # update the value of the programme name add upon every update
            self.ui.programme_name_add.setText(self.ui.list_programmes.currentItem().text())

        except:
            print("Programme parsing error")

        if self.ui.list_programmes.count() == 0:
            print("Programmes : No data here")
            # disable the delete programme
            # button because that makse sense
            self.ui.button_delete_programme.setEnabled(False)
        else:
            # or else enable it
            self.ui.button_delete_programme.setEnabled(True)


        try:
        #
        # before we add anything to the intakes
        # we have to check if there are any programmes
        # in that selected year. or else json module
        # will return an invalid index error
        #
            #
            # add all the intake months to the
            # list from the json data
            #
            for x in jsondata[self.ui.list_year.currentItem().text()][self.ui.list_programmes.currentItem().text()]:
                # Note : Dont forget to lower() the value of the items of this list
                self.ui.clone_from_intakes.addItem(x.capitalize())
                self.ui.list_intakes.addItem(x.capitalize())
            if len(jsondata[self.ui.list_year.currentItem().text()][self.ui.list_programmes.currentItem().text()]):
                self.ui.list_intakes.sortItems()
                if intake_preindex:
                    self.ui.list_intakes.setCurrentRow(intake_preindex)
                else:
                    self.ui.list_intakes.setCurrentRow(0)

            self.ui.button_delete_intake.setEnabled(True)
        except:
            print("Intakes : No data here")

        if self.ui.list_intakes.count() < 2:
            self.ui.button_delete_intake.setEnabled(False)
        else:
            self.ui.button_delete_intake.setEnabled(True)



        try:
        #
        # now its time to add the sessions to the programme
        # lets think...
        #
            while (self.ui.table_sessions.rowCount() > 0):
                {
                    self.ui.table_sessions.removeRow(0)
                }
            for x in jsondata[self.ui.list_year.currentItem().text()][self.ui.list_programmes.currentItem().text()][self.ui.list_intakes.currentItem().text().lower()][self.ui.combo_list_select_day.currentText().lower()]["sessions"]:
                self.ui.list_sessions.addItem(x[0]) #+ " (" + x[1] + " to " + x[2] + ")")
                #
                # time to populate
                # the table
                #
                self.ui.table_sessions.insertRow(0)
                self.ui.table_sessions.setItem(0,0, QtWidgets.QTableWidgetItem(x[0]))
                self.ui.table_sessions.setItem(0,1, QtWidgets.QTableWidgetItem(x[4]))
                self.ui.table_sessions.setItem(0,2, QtWidgets.QTableWidgetItem(x[1]))
                self.ui.table_sessions.setItem(0,3, QtWidgets.QTableWidgetItem(x[2]))
                self.ui.table_sessions.setItem(0,4, QtWidgets.QTableWidgetItem(x[5]))
                self.ui.table_sessions.setItem(0,5, QtWidgets.QTableWidgetItem(x[3]))
        except:
            print("Sessions : No data here")


        
        print("Year : " + str(year_preindex))
        print("Programme : " + str(programme_preindex))
        print("Intake : " + str(intake_preindex))
        print("Selected day : " + str(self.ui.combo_list_select_day.currentText()))
        print("***********************************")


    def add_year(self):
        #
        # We are now loading the
        # json data from the box
        # if the data is not well formatted
        # we will exit
        #
        if not dataloaded:
            self.ui.status_present.setText("*There is no valid JSON file loaded")
            self.ui.status_present.show()
            return()

        #
        # now we are loading the year value and checking
        # if the data is valid
        #
        year = self.ui.linedit_add_year.text()
        if not year:
            self.ui.status_present.setText("*Please enter an year")
            self.ui.status_present.show()
            return()
        self.ui.status_present.hide()
        jsonfile = mywindow.loadJsonData(self)
        
        #
        # we are now if the json file valid
        # just to be safe, we know its been
        # checked
        #
        if jsonfile == "ERROR":
            return()
        jsonfile.update({year : {}})
        
        #
        # now we update the json box
        # and update the boxes
        #
        self.ui.jsonraw.setText(json.dumps(jsonfile))
        mywindow.LoadData(self)
    


    def delete_year(self):
        #
        # this is the function to delete a year
        # from the json data
        #
        
        if not dataloaded:
            self.ui.status_present.setText("*There is no valid JSON file loaded")
            self.ui.status_present.show()
            return()

        if self.ui.list_year.count() != 1:
            self.ui.status_present.hide()
            selected_year = self.ui.list_year.currentItem().text()
            jsonfile = mywindow.loadJsonData(self)
            del jsonfile[selected_year]
            self.ui.jsonraw.setText(json.dumps(jsonfile))
            mywindow.LoadData(self)
        else:
            self.ui.status_present.setText("*there is only one year left")
            self.ui.status_present.show()

    def add_programme(self):
        #
        # so this is the function to add a programme
        # to the programme list... pretty basic
        #
        if not dataloaded:
            self.ui.status_present.setText("*There is no valid JSON file loaded")
            self.ui.status_present.show()
            return()
        
        if self.ui.programme_name_add.text():
            #
            # we have to check if there is any valid text
            # in the add programme name field
            #
            self.ui.status_present.hide()
            selected_year = self.ui.list_year.currentItem().text()
            programme_name_add = self.ui.programme_name_add.text()
            jsonfile = mywindow.loadJsonData(self)
            jsonfile[selected_year].update({programme_name_add : {}})
            self.ui.jsonraw.setText(json.dumps(jsonfile))
            mywindow.LoadData(self)
        else:
            #
            # if the data is not valid (aka datatype : None)
            # insult the user
            #
            self.ui.status_present.setText("*you didn't type anything in the programme name, you dumbass")
            self.ui.status_present.show()

    def addIntake(self):
        if not dataloaded:
            self.ui.status_present.setText("*There is no valid JSON file loaded")
            self.ui.status_present.show()
            return()

        year = self.ui.list_year.currentItem().text()
        programme = self.ui.list_programmes.currentItem().text()
        selected_intake_month = self.ui.combo_intake.currentText()
        jsonFile = mywindow.loadJsonData(self)

        if jsonFile == "ERROR":
            return()
        jsonFile[year][programme].update({selected_intake_month : {}})
        self.ui.jsonraw.setText(json.dumps(jsonFile))
        mywindow.LoadData(self)

    def delete_programm(self):
        #
        # This is the function to delete a programme
        # duh...
        #
        if not dataloaded:
            self.ui.status_present.setText("*There is no valid JSON file loaded")
            self.ui.status_present.show()
            return()

        if self.ui.list_programmes.count() != 1:
            selected_year = self.ui.list_year.currentItem().text()
            selected_programm = self.ui.list_programmes.currentItem().text()
            jsonfile = mywindow.loadJsonData(self)
            del jsonfile[selected_year][selected_programm]
            self.ui.jsonraw.setText((json.dumps(jsonfile)))
            mywindow.LoadData(self)
        else:
            self.ui.status_present.setText("*there is only one programme left. Add one to delete another one.")
            self.ui.status_present.show()
  


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())