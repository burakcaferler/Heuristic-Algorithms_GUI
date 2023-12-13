import string
from GA import GA
import functions
from enumFunctions import Functions
from GWO import GWO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("1000x600")
window.title("Grey Wolf Optimizer Parameters")

def GA_frame():
    frame = ttk.Frame(window)
    frame.pack()
    func_label= ttk.Label(frame, text="Select Function")
    func_label.grid(row=0, column=0, padx=5)
    func = ttk.Combobox(frame, values=["ackley","griewank", "schwefel","rastrigin","sphere","perm","zakharov", "rosenbrock","dixonprice"], state="readonly")
    func.grid(row=1,column=0, padx=5)

    lb_labelGA = ttk.Label(frame, text="Select Lower Bound:")
    lb_labelGA.grid(row=0, column=1, padx=5)
    lbGA = ttk.Combobox(frame, values=[-32.768,-600,-500,-5.12,-5.12,-30,-5,-2048,-10], state="readonly")
    lbGA.grid(row=1, column=1, padx=5)

    ub_labelGA = ttk.Label(frame, text="Select Upper Bound:")
    ub_labelGA.grid(row=0, column=2, padx=5)
    ubGA = ttk.Combobox(frame, values=[32.768, 600, 500,5.12, 30, 2048, 10], state="readonly")
    ubGA.grid(row=1, column=2, padx=5)

    dim_labelGA = ttk.Label(frame, text="Select Dimension:")
    dim_labelGA.grid(row=0, column=3, padx=5)
    dimGA = ttk.Combobox(frame, values=[5, 10, 15, 20,25,30], state="readonly")
    dimGA.grid(row=1, column=3, padx=5)

    pop_sizeGA_label = ttk.Label(frame, text="Select Population Size:")
    pop_sizeGA_label.grid(row=0, column=4, padx=5)
    pop_sizeGA_ = ttk.Combobox(frame, values=[5, 10, 15, 20], state="readonly")
    pop_sizeGA_.grid(row=1, column=4, padx=5)

    
    mut_probGA_label = ttk.Label(frame, text="Select Max Iterations:")
    mut_probGA_label.grid(row=0, column=5, padx=5)
    mut_probGA = ttk.Combobox(frame, values=[100, 500, 1000, 1500], state="readonly")
    mut_probGA.grid(row=1, column=5, padx=5)

    
    crossover_type_label = ttk.Label(frame, text="Select Objective Function:")
    crossover_type_label.grid(row=0, column=6, padx=5)
    crossover_type = ttk.Combobox(frame, values=["ackley","griewank", "schwefel","rastrigin","sphere","perm","zakharov", "rosenbrock","dixonprice"], state="readonly")
    crossover_type.grid(row=1, column=6, padx=5)

    selection_type_label = ttk.Label(frame, text="Select Objective Function:")
    selection_type_label.grid(row=0, column=6, padx=5)
    selection_type = ttk.Combobox(frame, values=["ackley","griewank", "schwefel","rastrigin","sphere","perm","zakharov", "rosenbrock","dixonprice"], state="readonly")
    selection_type.grid(row=1, column=6, padx=5)

    

   
    sol = GA.GA(frame.children['!combobox'].get(), float(frame.children['!combobox2'].get()), float(frame.children['!combobox3'].get()), float(frame.children['!combobox4'].get()), float(frame.children['!combobox5'].get()), float(frame.children['!combobox6'].get()),mut_prob,crossover_type,selection_type)



window.mainloop()
