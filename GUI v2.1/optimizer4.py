# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.func_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.func_comboBox.setGeometry(QtCore.QRect(650, 0, 141, 22))
        self.func_comboBox.setEditable(False)
        self.func_comboBox.setObjectName("func_comboBox")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_comboBox.addItem("")
        self.func_label = QtWidgets.QLabel(self.centralwidget)
        self.func_label.setGeometry(QtCore.QRect(530, 0, 111, 20))
        self.func_label.setObjectName("func_label")
        self.algorithm_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.algorithm_comboBox.setGeometry(QtCore.QRect(130, 0, 69, 22))
        self.algorithm_comboBox.setObjectName("algorithm_comboBox")
        self.algorithm_comboBox.addItem("")
        self.algorithm_comboBox.addItem("")
        self.algorithm_comboBox.addItem("")
        self.algorithm_comboBox.addItem("")
        self.algorithm_comboBox.addItem("")
        self.algorithm_label = QtWidgets.QLabel(self.centralwidget)
        self.algorithm_label.setGeometry(QtCore.QRect(10, 0, 111, 20))
        self.algorithm_label.setObjectName("algorithm_label")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 30, 341, 201))
        self.stackedWidget.setObjectName("stackedWidget")
        self.HS = QtWidgets.QWidget()
        self.HS.setObjectName("HS")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.HS)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 2, 321, 191))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_7.addWidget(self.lineEdit_6)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_7.addWidget(self.lineEdit_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_6.addWidget(self.lineEdit_8)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_6.addWidget(self.lineEdit_9)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_6.addWidget(self.lineEdit_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.HS)
        self.SA = QtWidgets.QWidget()
        self.SA.setObjectName("SA")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.SA)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 171, 111))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_8.addWidget(self.lineEdit_11)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_8.addWidget(self.lineEdit_12)
        self.stackedWidget.addWidget(self.SA)
        self.GWO = QtWidgets.QWidget()
        self.GWO.setObjectName("GWO")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.GWO)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 211, 171))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout_9.addWidget(self.lineEdit_13)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_9.addWidget(self.label_16)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout_9.addWidget(self.lineEdit_14)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_9.addWidget(self.label_17)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_9.addWidget(self.lineEdit_15)
        self.stackedWidget.addWidget(self.GWO)
        self.PSO = QtWidgets.QWidget()
        self.PSO.setObjectName("PSO")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.PSO)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 221, 151))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_35 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_16.addWidget(self.label_35)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.verticalLayout_16.addWidget(self.lineEdit_31)
        self.label_36 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_16.addWidget(self.label_36)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.verticalLayout_16.addWidget(self.lineEdit_32)
        self.stackedWidget.addWidget(self.PSO)
        self.GA = QtWidgets.QWidget()
        self.GA.setObjectName("GA")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.GA)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 331, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_5.addWidget(self.comboBox)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_5.addWidget(self.comboBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.GA)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.func_comboBox, self.algorithm_comboBox)
        #############################################################################################
        self.algorithm_comboBox.currentIndexChanged.connect(self.toggle_layer)
    
    def toggle_layer(self):
       
        selected_index = self.algorithm_comboBox.currentIndex()
        self.stackedWidget.setCurrentIndex(selected_index)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.func_comboBox.setItemText(0, _translate("MainWindow", "Ackley"))
        self.func_comboBox.setItemText(1, _translate("MainWindow", "Griewank"))
        self.func_comboBox.setItemText(2, _translate("MainWindow", "Schwefel"))
        self.func_comboBox.setItemText(3, _translate("MainWindow", "Rastrigin"))
        self.func_comboBox.setItemText(4, _translate("MainWindow", "Sphere"))
        self.func_comboBox.setItemText(5, _translate("MainWindow", "Perm"))
        self.func_comboBox.setItemText(6, _translate("MainWindow", "Zakharov"))
        self.func_comboBox.setItemText(7, _translate("MainWindow", "Rosenbrock"))
        self.func_comboBox.setItemText(8, _translate("MainWindow", "Dixon-Price"))
        self.func_label.setText(_translate("MainWindow", "Select a function:"))
        self.algorithm_comboBox.setItemText(0, _translate("MainWindow", "GA"))
        self.algorithm_comboBox.setItemText(1, _translate("MainWindow", "SA"))
        self.algorithm_comboBox.setItemText(2, _translate("MainWindow", "GWO"))
        self.algorithm_comboBox.setItemText(3, _translate("MainWindow", "PSO"))
        self.algorithm_comboBox.setItemText(4, _translate("MainWindow", "HS"))
        self.algorithm_label.setText(_translate("MainWindow", "Select an algorithm"))
        self.label_10.setText(_translate("MainWindow", "PAR"))
        self.label_11.setText(_translate("MainWindow", "Bw"))
        self.label_12.setText(_translate("MainWindow", "Nnew"))
        self.label_8.setText(_translate("MainWindow", "Iteration count"))
        self.label.setText(_translate("MainWindow", "HMS"))
        self.label_9.setText(_translate("MainWindow", "HMCR"))
        self.label_13.setText(_translate("MainWindow", "Temp"))
        self.label_14.setText(_translate("MainWindow", "Type"))
        self.label_15.setText(_translate("MainWindow", "Population size"))
        self.label_16.setText(_translate("MainWindow", "Number of Generations"))
        self.label_17.setText(_translate("MainWindow", "a"))
        self.label_35.setText(_translate("MainWindow", "Population size"))
        self.label_36.setText(_translate("MainWindow", "Number of Generations"))
        self.label_2.setText(_translate("MainWindow", "Dimension"))
        self.label_3.setText(_translate("MainWindow", "Population Size"))
        self.label_4.setText(_translate("MainWindow", "Number of Generations"))
        self.label_5.setText(_translate("MainWindow", "Mutation probability"))
        self.label_6.setText(_translate("MainWindow", "Cross-over Type"))
        self.label_7.setText(_translate("MainWindow", "Selection Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
