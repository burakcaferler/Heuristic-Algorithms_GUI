import functions
from enumFunctions import Functions
from GWO import GWO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
from tkinter import ttk


def start_optimization():
    selected_lb = float(lb.get())
    selected_ub = float(ub.get())
    selected_dim = int(dim.get())
    selected_search_agents = int(search_agents.get())
    selected_max_iter = int(max_iter.get())

    selected_func = functions.selectFunction(Functions[functions_cb.get()])

    result = GWO(selected_func, selected_lb, selected_ub, selected_dim, selected_search_agents, selected_max_iter)

    for widget in plot_container.winfo_children():
        widget.destroy()
       # Plotting
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(result.convergence)
    ax.set_title("Convergence Curve")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Alpha Score")
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=plot_container)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Use 'result' to draw a plot with Alpha_score here


window = tk.Tk()
window.geometry("600x600")
window.title("Grey Wolf Optimizer Parameters")

lb_label = ttk.Label(window, text="Select Lower Bound:")
lb_label.pack()
lb = ttk.Combobox(window, values=[-32.768, -4, -3, -2, -1, 0], state="readonly")
lb.pack()

ub_label = ttk.Label(window, text="Select Upper Bound:")
ub_label.pack()
ub = ttk.Combobox(window, values=[32.768, 2, 3, 4, 5], state="readonly")
ub.pack()

dim_label = ttk.Label(window, text="Select Dimension:")
dim_label.pack()
dim = ttk.Combobox(window, values=[5, 10, 15, 20], state="readonly")
dim.pack()

search_agents_label = ttk.Label(window, text="Select Search Agents:")
search_agents_label.pack()
search_agents = ttk.Combobox(window, values=[5, 10, 15, 20], state="readonly")
search_agents.pack()

max_iter_label = ttk.Label(window, text="Select Max Iterations:")
max_iter_label.pack()
max_iter = ttk.Combobox(window, values=[100, 500, 1000, 1500], state="readonly")
max_iter.pack()

functions_label = ttk.Label(window, text="Select Objective Function:")
functions_label.pack()
functions_cb = ttk.Combobox(window, values=["griewank", "sphere", "rosenbrock"], state="readonly")
functions_cb.pack()

plot_container = ttk.Frame(window)
plot_container.pack(fill=tk.BOTH, expand=True)


start_button = ttk.Button(window, text="Start Optimization", command=start_optimization)
start_button.pack()

window.mainloop()


def gwo():
    obj_func = functions.selectFunction(Functions.griewank)
    # dim array size, -5 lb +5 lb 
    GWO(obj_func, -5, 5, 10, 1000, 100)

def main():
    gwo()

if __name__ == "__main__":
    main()
    
#def GWO(objf, lb, ub, dim, SearchAgents_no, Max_iter):