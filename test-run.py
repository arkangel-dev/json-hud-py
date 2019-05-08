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
from PyQt5 import QtWidgets, QtCore, QtGui
from user_interface_main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
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
        #self.ui.pushButton.clicked.connect(self.GenerateJson)
        self.ui.LoadJson.clicked.connect(self.LoadData)
        self.ui.button_add_year.clicked.connect(self.add_year)
        self.ui.button_delete_year.clicked.connect(self.delete_year)
        self.ui.list_year.clicked.connect(self.LoadData)
        self.ui.list_programmes.clicked.connect(self.LoadData)
        self.ui.list_intakes.clicked.connect(self.LoadData)
        self.ui.combo_list_select_day.currentTextChanged.connect(self.LoadData)

        # this is the debug version so I'll hide the status
        # data programmatically here..
        self.ui.status_present.hide()
        global dataloaded
        dataloaded = False
    
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
        self.ui.list_programmes.clear()
        self.ui.list_intakes.clear()
        self.ui.list_sessions.clear()
        #===============================================================
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
        #
        # add all the programmes from the json
        # file to the list
        #
        try:
            for x in jsondata[self.ui.list_year.currentItem().text()]:
                self.ui.list_programmes.addItem(x)
            if len(jsondata[self.ui.list_year.currentItem().text()]):
                self.ui.list_programmes.sortItems()
                if programme_preindex:
                    self.ui.list_programmes.setCurrentRow(programme_preindex)
                else:
                    self.ui.list_programmes.setCurrentRow(0)
        except:
            print("No data here")

        #
        # before we add anything to the intakes
        # we have to check if there are any programmes
        # in that selected year. or else json module
        # will return an invalid index error
        #
        try:
            #
            # add all the intake months to the
            # list from the json data
            #
            for x in jsondata[self.ui.list_year.currentItem().text()][self.ui.list_programmes.currentItem().text()]:
                # Note : Dont forget to lower() the value of the items of this list
                self.ui.list_intakes.addItem(x.capitalize())
            if len(jsondata[self.ui.list_year.currentItem().text()][self.ui.list_programmes.currentItem().text()]):
                self.ui.list_intakes.sortItems()
                if intake_preindex:
                    self.ui.list_intakes.setCurrentRow(intake_preindex)
                else:
                    self.ui.list_intakes.setCurrentRow(0)
        except:
            print("No data here")

        #
        # now its time to add the sessions to the programme
        # lets think...
        #
        try:
            # dayarray = ["sunday","monday","tuesday","wednesday","thurday","friday","saturday",]
            # for y in dayarray:
                # for x in jsondata[self.ui.list_year.currentItem().text()][self.ui.list_programmes.currentItem().text()][self.ui.list_intakes.currentItem().text().lower()][y]["sessions"]:
            
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
                self.ui.table_sessions.setItem(0,0, QTableWidgetItem(x[0]))
                self.ui.table_sessions.setItem(0,1, QTableWidgetItem(x[4]))
                self.ui.table_sessions.setItem(0,2, QTableWidgetItem(x[1]))
                self.ui.table_sessions.setItem(0,3, QTableWidgetItem(x[2]))
                self.ui.table_sessions.setItem(0,4, QTableWidgetItem(x[5]))
                self.ui.table_sessions.setItem(0,5, QTableWidgetItem(x[3]))
            # if len(jsondata[self.ui.list_year.currentItem().text()][self.ui.list_programmes.currentItem().text()]):
        except:
            print("No data here")


        
        print("Year : " + str(year_preindex))
        print("Programme : " + str(programme_preindex))
        print("Intake : " + str(intake_preindex))
        print("Selected day : " + str(self.ui.combo_list_select_day.currentText()))
        print("***********************************")




        #==============================================================

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

        selected_year = self.ui.list_year.currentItem().text()
        jsonfile = mywindow.loadJsonData(self)
        del jsonfile[selected_year]
        self.ui.jsonraw.setText(json.dumps(jsonfile))
        mywindow.LoadData(self)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())