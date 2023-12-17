from GWO import GWO
from ui_mainwindow import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from io import BytesIO
from pyqtgraph  import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QGraphicsScene, QGraphicsPixmapItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PSO import PSO
from SA import SA_geometric, SA_linear
import functions
from enumFunctions import Functions
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
bounds=[[-32.768,32768],[-600,600],[-500,500],[-5.12,5.12],[-5.12,5.12],[-30.30],[-5.10],[-2048,2048],[-10,10]]
from solution import solution

class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.axes = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MatplotlibWidget, self).__init__(fig)
        self.setParent(parent)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.matplotlibWidget = MatplotlibWidget(self.graphWidget)
        self.graphLayout.addWidget(self.matplotlibWidget)
        self.lower_bound.setText(f"{bounds[0][0]}")
        self.upper_bound.setText(f"{bounds[0][1]}")
        self.color_legend={}
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.algorithm_comboBox.currentIndexChanged.connect(self.toggle_layer)
        self.algorithm_comboBox_2.currentIndexChanged.connect(self.toggle_layer)
        self.algorithm_comboBox_3.currentIndexChanged.connect(self.toggle_layer)
        self.Run_button.clicked.connect(self.button_clicked)
        self.sol=solution()
        self.algorithm_comboBox_type=0
        self.clearGraphButton.clicked.connect(self.clear_graph)
        self.func_comboBox.currentIndexChanged.connect(self.bounds_select)
    
    def bounds_select(self):
        index=self.func_comboBox.currentIndex()
        default_lower_bound = str(bounds[index][0])
        default_upper_bound = str(bounds[index][1])
        
        self.lower_bound.setText(default_lower_bound)
        self.upper_bound.setText(default_upper_bound)
    def toggle_layer(self):
        
        
            self.stackedWidget.setCurrentIndex(self.algorithm_comboBox.currentIndex())
            self.stackedWidget_2.setCurrentIndex(self.algorithm_comboBox_2.currentIndex())
            self.stackedWidget_3.setCurrentIndex(self.algorithm_comboBox_3.currentIndex())
    def clear_graph(self):
            # Clear the graph in the MatplotlibWidget
            self.matplotlibWidget.axes.clear()
            self.matplotlibWidget.draw()
            
    def button_clicked(self):
        combo_boxes = [self.algorithm_comboBox, self.algorithm_comboBox_2, self.algorithm_comboBox_3]

        for index, combo_box in enumerate(combo_boxes, start=1):
            if combo_box.currentText() == "PSO":
                self.run_algorithm(index, "PSO")

            elif combo_box.currentText() == "SA":
                self.run_algorithm(index, "SA")

            elif combo_box.currentText() == "GWO":
                self.run_algorithm(index, "GWO")

    def run_algorithm(self, algorithm_type, algorithm_name):
        selected_index = self.func_comboBox.currentIndex()
        dim = 30
        obj_func = self.function_select()

        if algorithm_type == 1:  # PSO
            pop_size = int(self.pso_pop_size.text())
            num_gen = int(self.pso_num_gen.text())
            lower_bound = int(self.lower_bound.text())
            upper_bound = int(self.upper_bound.text())
            print(f"{lower_bound}")
            print(f"{upper_bound}")
            self.sol = PSO(obj_func, lower_bound, upper_bound, dim, pop_size, num_gen)
            self.update_graph(algorithm_type)

        elif algorithm_type == 2:  # SA
            temp = int(self.sa_temp_2.text())
            sa_type = self.SA_type_2.currentText()
            lower_bounds = [int(self.lower_bound.text()) for _ in range(dim)]
            upper_bounds = [int(self.upper_bound.text()) for _ in range(dim)]

            if sa_type == "Linear":
                self.sol = SA_linear(dim=dim, min_values=lower_bounds, max_values=upper_bounds,
                                          mu=0, sigma=1, initial_temperature=temp,
                                          temperature_iterations=5000, final_temperature=0.0001,
                                          alpha=0.95, target_function=obj_func, verbose=True)
            else:
                self.sol = SA_geometric(dim=dim, min_values=lower_bounds, max_values=upper_bounds,
                                             mu=0, sigma=1, initial_temperature=temp,
                                             temperature_iterations=5000, final_temperature=0.0001,
                                             alpha=0.98, target_function=obj_func, verbose=True)
            self.update_graph(algorithm_type)

        elif algorithm_type == 3:  # GWO
            pop_size = int(self.pso_pop_size.text())  # GWO gereksinimlerine göre parametreleri ayarlayın
            num_gen = int(self.pso_num_gen.text())
            lower_bound = int(self.lower_bound.text())
            upper_bound = int(self.upper_bound.text())
            search_agents_no = int(self.GWO_SearchAgentsNo_3.text())
            max_iter = int(self.GWO_maxIter_3.text())
            decrease_from = int(self.GWO_decreaseFrom_3.text())

            self.sol = GWO(obj_func, lower_bound, upper_bound, dim, search_agents_no, max_iter, decrease_from)
            self.update_graph(algorithm_type)
        
            
    def function_select(self):
            func=self.func_comboBox.currentIndex()
            if func==0:
                return functions.selectFunction(Functions.ackley)
            elif func==1:
                return functions.selectFunction(Functions.griewank)
            elif func==2:
                return functions.selectFunction(Functions.schwefel)
            elif func==3:
                return functions.selectFunction(Functions.rastrigin)
            elif func==4:
                return functions.selectFunction(Functions.sphere)
            elif func==5:
                return functions.selectFunction(Functions.perm)
            elif func==6:
                return functions.selectFunction(Functions.zakharov)
            elif func==7:
                return functions.selectFunction(Functions.rosenbrock)
            elif func==8:
                return functions.selectFunction(Functions.dixonprice)

    




    def update_graph(self,algorithm_type):
        line = sns.lineplot(x=self.sol.x, y=self.sol.y, ax=self.matplotlibWidget.axes, label=self.get_algorithm_label(algorithm_type))

        self.matplotlibWidget.axes.set_xlabel('Iteration count')
        self.matplotlibWidget.axes.set_ylabel('Fitness value')

        self.matplotlibWidget.axes.legend(loc="upper right")

        self.matplotlibWidget.draw()
        

    def get_algorithm_label(self,algorithm_type):
        if algorithm_type == 1:
            return f"{self.algorithm_comboBox.currentText()}"
        elif algorithm_type == 2:
            return f"{self.algorithm_comboBox_2.currentText()}"
        elif algorithm_type == 3:
            return f"{self.algorithm_comboBox_3.currentText()}"
       
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()