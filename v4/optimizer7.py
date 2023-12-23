import GA
from GWO import GWO
from HS import harmonySearch
from WOA import WOA
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
bounds=[[-32.768,32.768],[-600,600],[-500,500],[-5.12,5.12],[-5.12,5.12],[-30,30],[-5,10],[-2048,2048],[-10,10]]
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
        self.gridLayout_2.parentWidget().setStyleSheet("background-color: peachpuff;")
        self.gridLayout_3.parentWidget().setStyleSheet("background-color: lavender;")
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
            elif combo_box.currentText() == "HS":
                self.run_algorithm(index, "HS")
            elif combo_box.currentText() == "GA":
                self.run_algorithm(index, "GA")

    def run_algorithm(self, algorithm_type, algorithm_name):
        
        
      
        obj_func = self.function_select()
        
        if algorithm_name == "PSO" :  # PSO
            if algorithm_type == 1:
                pop_size = int(self.pso_pop_size.text())
                num_gen = int(self.pso_num_gen.text())
                dim=int(self.pso_dim.text())
                print("PSO 1: ")
                print(pop_size)
                print(num_gen)
                print(dim)
            elif algorithm_type == 2:
                pop_size = int(self.pso_pop_size_2.text())
                num_gen = int(self.pso_num_gen_2.text())
                dim=int(self.pso_dim_2.text())
            else:
                pop_size = int(self.pso_pop_size_3.text())
                num_gen = int(self.pso_num_gen_3.text())
                dim=int(self.pso_dim_3.text())
           
            lower_bound = float(self.lower_bound.text())
            upper_bound = float(self.upper_bound.text())
            self.sol = PSO(obj_func, lower_bound, upper_bound, dim, pop_size, num_gen)
            self.update_graph(algorithm_type)

        elif algorithm_name == "SA":  # SA
            if algorithm_type == 1:
                temp = int(self.sa_temp.text())
                sa_type = self.SA_type_1.currentText()
                dim=int(self.SA_dim_1.text())
            elif algorithm_type == 2:
                temp = int(self.sa_temp_2.text())
                sa_type = self.SA_type_2.currentText()
                dim=int(self.SA_dim_2.text())
            else:
                temp = int(self.sa_temp_3.text())
                sa_type = self.SA_type_3.currentText()
                dim=int(self.SA_dim_3.text())
            
            lower_bounds = [float(self.lower_bound.text()) for _ in range(dim)]
            upper_bounds = [float(self.upper_bound.text()) for _ in range(dim)]

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

        elif algorithm_name == "GWO":  # GWO
            if algorithm_type == 1:
                search_agents_no = int(self.GWO_SearchAgentsNo.text())
                max_iter = int(self.GWO_maxIter.text())
                decrease_from = int(self.GWO_decreaseFrom.text())
                dim=int(self.GWO_dim.text())
            elif algorithm_type == 2:
                search_agents_no = int(self.GWO_SearchAgentsNo_2.text())
                max_iter = int(self.GWO_maxIter_2.text())
                decrease_from = int(self.GWO_decreaseFrom_2.text())
                dim=int(self.GWO_dim_2.text())
            else:
                search_agents_no = int(self.GWO_SearchAgentsNo_3.text())
                max_iter = int(self.GWO_maxIter_3.text())
                decrease_from = int(self.GWO_decreaseFrom_3.text())
                dim=int(self.GWO_dim_3.text())
           
          
            lower_bound = float(self.lower_bound.text())
            upper_bound = float(self.upper_bound.text())
            self.sol = GWO(obj_func, lower_bound, upper_bound, dim, search_agents_no, max_iter, decrease_from)
            self.update_graph(algorithm_type)
        elif algorithm_name == "HS":  # HS
            
            
            if algorithm_type == 1:
                hms = int(self.HS_HWS.text())
                iter = int(self.HS_iterCount.text())
                hmcr = float(self.HS_HMCR.text())
                par = float(self.HS_PAR.text())
                bw=float(self.HS_BW.text())
                nnew=int(self.HS_NNEW.text())
                dim=int(self.hs_dim.text())
            elif algorithm_type == 2:
                hms = int(self.HS_HWS_2.text())
                iter = int(self.HS_iterCount_2.text())
                hmcr = float(self.HS_HMCR_2.text())
                par = float(self.HS_PAR_2.text())
                bw=float(self.HS_BW_2.text())
                nnew=int(self.HS_NNEW_2.text())
                dim=int(self.hs_dim_2.text())
            else:
                hms = int(self.HS_HWS_3.text())
                iter = int(self.HS_iterCount_3.text())
                hmcr = float(self.HS_HMCR_3.text())
                par = float(self.HS_PAR_3.text())
                bw=float(self.HS_BW_3.text())
                nnew=int(self.HS_NNEW_3.text())
                dim=int(self.hs_dim_3.text())
                
            lower_bounds = [float(self.lower_bound.text()) for _ in range(dim)]
            upper_bounds = [float(self.upper_bound.text()) for _ in range(dim)]
            self.sol=harmonySearch(hms, iter, hmcr, par, bw, nnew, lower_bounds, upper_bounds,obj_func)
            self.update_graph(algorithm_type)
        
        elif algorithm_name == "GA": 
            
           
            if algorithm_type == 1:
                pop_size=int(self.GA_popSize.text())
                num_of_gen=int(self.GA_numOfGens.text())
                mut_prob=float(self.GA_mutProb.text())
                crossover_type=int(self.GA_crossType.currentIndex())
                selection_type=int(self.GA_selectType.currentIndex())
                dimension=int(self.GA_dim.text())
            elif algorithm_type == 2:
                pop_size=int(self.GA_popSize_2.text())
                num_of_gen=int(self.GA_numOfGens_2.text())
                mut_prob=float(self.GA_mutProb_2.text())
                crossover_type=int(self.GA_crossType_2.currentIndex())
                selection_type=int(self.GA_selectType_2.currentIndex())
                dimension=int(self.GA_dim_2.text())
            else:
                pop_size=int(self.GA_popSize_3.text())
                num_of_gen=int(self.GA_numOfGens_3.text())
                mut_prob=float(self.GA_mutProb_3.text())
                crossover_type=int(self.GA_crossType_3.currentIndex())
                selection_type=int(self.GA_selectType_3.currentIndex())
                dimension=int(self.GA_dim_3.text())
                
                
            lower_bound = float(self.lower_bound.text())
            upper_bound = float(self.upper_bound.text())
            self.sol = GA.GA(obj_func, lower_bound, upper_bound, dimension, pop_size, num_of_gen,mut_prob,crossover_type,selection_type)
            self.update_graph(algorithm_type)
        elif algorithm_name == "WOA":  # WOA
            if algorithm_type == 1:
                search_agents_no = int(self.WOA_SearchAgentsNo.text())
                max_iter = int(self.WOA_Max_iter.text())
                dim=int(self.WOA_dim.text())
            elif algorithm_type == 2:
                search_agents_no = int(self.WOA_SearchAgentsNo.text())
                max_iter = int(self.WOA_Max_iter_2.text())
                dim=int(self.WOA_dim_2.text())
            else:
                search_agents_no = int(self.WOA_SearchAgentsNo.text())
                max_iter = int(self.WOA_Max_iter_4.text())
                dim=int(self.WOA_dim_4.text())
                
            lower_bound = float(self.lower_bound.text())
            upper_bound = float(self.upper_bound.text())
            self.sol = WOA(obj_func, lower_bound,upper_bound,dim,search_agents_no,max_iter)
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