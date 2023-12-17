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
        self.algorithm_label = QtWidgets.QLabel(self.centralwidget)
        self.algorithm_label.setGeometry(QtCore.QRect(10, 0, 111, 20))
        self.algorithm_label.setObjectName("algorithm_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 211, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.PSO_layer = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.PSO_layer.setContentsMargins(0, 0, 0, 0)
        self.PSO_layer.setObjectName("PSO_layer")
        self.pop_size_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pop_size_label.setObjectName("pop_size_label")
        self.PSO_layer.addWidget(self.pop_size_label)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.PSO_layer.addWidget(self.spinBox)
        self.iteration_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.iteration_label.setObjectName("iteration_label")
        self.PSO_layer.addWidget(self.iteration_label)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.PSO_layer.addWidget(self.spinBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.func_comboBox, self.algorithm_comboBox)

        self.algorithm_comboBox.currentIndexChanged.connect(self.toggle_layer)
        

    def toggle_layer(self):
        # ComboBox'tan seçilen öğeye bağlı olarak layer'ların görünürlüğünü ayarlayın
        selected_index = self.algorithm_comboBox.currentIndex()

        # Tüm layer'ları başlangıçta gizleyin
        self.pop_size_label.setVisible(False)
        self.spinBox.setVisible(False)
        self.iteration_label.setVisible(False)
        self.spinBox_2.setVisible(False)
        

        # Seçilen layer'ı görünür yapın
        if selected_index == 0:
            self.pop_size_label.setVisible(True)
            self.spinBox.setVisible(True)
            self.iteration_label.setVisible(True)
            self.spinBox_2.setVisible(True)
        elif selected_index == 1:
            self.pop_size_label.setVisible(False)
            self.spinBox.setVisible(False)
            self.iteration_label.setVisible(False)
            self.spinBox_2.setVisible(False)
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
        self.algorithm_comboBox.setItemText(0, _translate("MainWindow", "PSO"))
        self.algorithm_comboBox.setItemText(1, _translate("MainWindow", "GWO"))
        self.algorithm_label.setText(_translate("MainWindow", "Select an algorithm"))
        self.pop_size_label.setText(_translate("MainWindow", "Pop size:"))
        self.iteration_label.setText(_translate("MainWindow", "Iteration count:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())