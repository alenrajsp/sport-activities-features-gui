from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from widgets.ImportDataWidget import Ui_ImportData
from widgets.GraphsWidget import Ui_Graphs
from models.User import User


class Ui_MainWindow(QMainWindow):
    globalUser: User
    importDataUi: Ui_ImportData
    graphsUi = Ui_Graphs
    transofrmationsUi = [] # placeholder
    calendarUi = [] # placeholder
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName("Sport Activities Features GUI")
        self.setEnabled(True)
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabWidget.setGeometry(QtCore.QRect(0, 0, 811, 551))
        self.mainTabWidget.setObjectName("mainTabWidget")
        # IMPORT DATA
        self.tab_ImportData = QtWidgets.QWidget()
        self.tab_ImportData.setObjectName("tab_ImportData")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_ImportData)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # LAYOUT 1
        self.mainLayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout_1.setContentsMargins(0, 0, 0, 0)
        self.mainLayout_1.setObjectName("mainLayout_1")
        self.mainTabWidget.addTab(self.tab_ImportData, "")
        # GRAPHS
        self.tab_Graphs = QtWidgets.QWidget()
        self.tab_Graphs.setObjectName("tab_Graphs")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_Graphs)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.mainLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.mainLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainLayout_2.setObjectName("mainLayout_2")
        self.mainTabWidget.addTab(self.tab_Graphs, "")
        # CALENDAR
        self.tab_Calender = QtWidgets.QWidget()
        self.tab_Calender.setObjectName("tab_Calender")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_Calender)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.mainLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.mainLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainLayout_4.setObjectName("mainLayout_4")
        self.mainTabWidget.addTab(self.tab_Calender, "")
        # TRANSOFRMATIONS
        self.tab_Transformations = QtWidgets.QWidget()
        self.tab_Transformations.setObjectName("tab_Transformations")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_Transformations)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 801, 521))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.mainLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.mainLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainLayout_3.setObjectName("mainLayout_3")
        self.mainTabWidget.addTab(self.tab_Transformations, "")
        
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionImport_Data = QtWidgets.QAction(self)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionCalender = QtWidgets.QAction(self)
        self.actionCalender.setObjectName("actionCalender")
        self.actionGraphs = QtWidgets.QAction(self)
        self.actionGraphs.setObjectName("actionGraphs")
        self.actionTransformations = QtWidgets.QAction(self)
        self.actionTransformations.setObjectName("actionTransformations")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(self)
        self.mainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.importDataUi = Ui_ImportData()
        self.mainLayout_1.addWidget(self.importDataUi)
        self.graphsUi = Ui_Graphs()
        self.mainLayout_2.addWidget(self.graphsUi)
        
        self.actionExit.triggered.connect(self.close)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_ImportData), _translate("MainWindow", "Import Data"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_Graphs), _translate("MainWindow", "Graphs"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_Transformations), _translate("MainWindow", "Transformations"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_Calender), _translate("MainWindow", "Calendar"))
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionImport_Data.setText(_translate("MainWindow", "Import Data"))
        self.actionGraphs.setText(_translate("MainWindow", "Graphs"))
        self.actionTransformations.setText(_translate("MainWindow", "Transformations"))
        self.actionCalender.setText(_translate("MainWindow", "Calender"))

    # IMPORT GLOBAL USER
    def importGlobalUser(self, user):
        self.globalUser = user
        self.importDataUi.importGlobalUser(user)
        self.graphsUi.importGlobalUser(user)