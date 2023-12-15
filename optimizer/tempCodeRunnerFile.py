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
        
        self.color_legend={}
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.algorithm_comboBox.currentIndexChanged.connect(self.toggle_layer)
        self.algorithm_comboBox_2.currentIndexChanged.connect(self.toggle_layer)
        self.Run_button.clicked.connect(self.button_clicked)
        self.sol=solution()
        self.algorithm_comboBox_type=0
    def toggle_layer(self):
        
        
            self.stackedWidget.setCurrentIndex(self.algorithm_comboBox.currentIndex())
            self.stackedWidget_2.setCurrentIndex(self.algorithm_comboBox_2.currentIndex())
            
    def button_clicked(self):
        
            if self.algorithm_comboBox.currentText()=="PSO":
                    selected_index = self.algorithm_comboBox.currentIndex()
                    dim=30
                    pop_size=int(self.pso_pop_size.text())
                    num_gen=int(self.pso_num_gen.text())
                    obj_func=self.fuction_select()
                    lower_bound = bounds[selected_index][0]
                    upper_bound = bounds[selected_index][1]
                    self.sol=PSO(obj_func,lower_bound,upper_bound,dim,pop_size,num_gen)
                    self.algorithm_comboBox_type=1
                    self.update_graph()
                    
            if  self.algorithm_comboBox_2.currentText()=="SA":
                    selected_index = self.func_comboBox.currentIndex()
                    print(selected_index)
                    dim=30
                    temp=int(self.sa_temp_2.text())
                    type=self.sa_type_combobox_2.currentText()
                    obj_func=self.fuction_select()
                    lower_bounds= [None for _ in range(dim)]
                    upper_bounds= [None for _ in range(dim)]
                    for idx in range(dim):
                        lower_bounds[idx]=bounds[selected_index][0]
                        upper_bounds[idx]=bounds[selected_index][1]
                        
                    if type=="Linear":
                        self.sol=SA_linear( dim=dim,min_values = lower_bounds, max_values = upper_bounds, mu = 0, sigma = 1, initial_temperature = temp, temperature_iterations = 5000,
                        final_temperature = 0.0001, alpha = 0.9, target_function = obj_func, verbose = True)
                    else:
                        self.sol = SA_linear( dim=dim,min_values = lower_bounds, max_values = upper_bounds, mu = 0, sigma = 1, initial_temperature = temp, temperature_iterations = 5000,
                        final_temperature = 0.0001, alpha = 0.9, target_function = obj_func, verbose = True)
                        
                        
                  
                    self.algorithm_comboBox_type=2
                    self.update_graph()
    
            
    def fuction_select(self):
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

    


    def update_graph(self):
           
            line=sns.lineplot(x=self.sol.x, y=self.sol.y, ax=self.matplotlibWidget.axes)
           
           
            self.matplotlibWidget.axes.set_xlabel('Iteration count')
            self.matplotlibWidget.axes.set_ylabel('Fitness value')
            existing_legend = self.matplotlibWidget.axes.get_legend()


            if self.algorithm_comboBox_type == 1:
                line.lines[0].set_color("red")
                legend_color = mpatches.Patch(color="red", label=f"{self.algorithm_comboBox.currentText()}")
                self.matplotlibWidget.axes.legend(handles=[legend_color], loc=(1, 0.9))

            elif self.algorithm_comboBox_type == 2:
                line.lines[0].set_color("blue")
                legend_color = mpatches.Patch(color="blue", label=f"{self.algorithm_comboBox_2.currentText()}")
                if existing_legend:
                    self.matplotlibWidget.axes.legend(handles=existing_legend.legendHandles + [legend_color], loc=(1, 0.7))
                else:
                    self.matplotlibWidget.axes.legend(handles=[legend_color], loc=(1, 0.7))

            self.matplotlibWidget.draw()
                        

            
          

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()