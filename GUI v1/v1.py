import functions
from enumFunctions import Functions
from GWO import GWO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk



def create_optimization_frame(window, optimization_algorithm):
    def start_optimization():
        nonlocal plot_container
        selected_lb = float(lb.get())
        selected_ub = float(ub.get())
        selected_dim = int(dim.get())
        selected_search_agents = int(search_agents.get())
        selected_max_iter = int(max_iter.get())

        selected_func = functions.selectFunction(Functions[functions_cb.get()])

        result = optimization_algorithm(selected_func, selected_lb, selected_ub, selected_dim, selected_search_agents, selected_max_iter)

        for widget in plot_container.winfo_children():
            widget.destroy()
        
        # Plotting
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.plot(result.convergence)
        ax.set_title("Convergence Curve")
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Alpha Score")
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=plot_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    frame = ttk.Frame(window)
    frame.pack()

    alg_label= ttk.Label(frame, text="Select Algorithm")
    alg_label.grid(row=0, column=0, padx=5)
    alg = ttk.Combobox(frame, values=["GA","SA","GWO","PSO","HS"])
    alg.grid(row=1,column=0, padx=5)


    lb_label = ttk.Label(frame, text="Select Lower Bound:")
    lb_label.grid(row=0, column=1, padx=5)
    lb = ttk.Combobox(frame, values=[-32.768, -4, -3, -2, -1, 0], state="readonly")
    lb.grid(row=1, column=1, padx=5)

    ub_label = ttk.Label(frame, text="Select Upper Bound:")
    ub_label.grid(row=0, column=2, padx=5)
    ub = ttk.Combobox(frame, values=[32.768, 2, 3, 4, 5], state="readonly")
    ub.grid(row=1, column=2, padx=5)

    dim_label = ttk.Label(frame, text="Select Dimension:")
    dim_label.grid(row=0, column=3, padx=5)
    dim = ttk.Combobox(frame, values=[5, 10, 15, 20], state="readonly")
    dim.grid(row=1, column=3, padx=5)

    search_agents_label = ttk.Label(frame, text="Select Search Agents:")
    search_agents_label.grid(row=0, column=4, padx=5)
    search_agents = ttk.Combobox(frame, values=[5, 10, 15, 20], state="readonly")
    search_agents.grid(row=1, column=4, padx=5)

    
    max_iter_label = ttk.Label(frame, text="Select Max Iterations:")
    max_iter_label.grid(row=0, column=5, padx=5)
    max_iter = ttk.Combobox(frame, values=[100, 500, 1000, 1500], state="readonly")
    max_iter.grid(row=1, column=5, padx=5)

    
    functions_label = ttk.Label(frame, text="Select Objective Function:")
    functions_label.grid(row=0, column=6, padx=5)
    functions_cb = ttk.Combobox(frame, values=["griewank", "sphere", "rosenbrock"], state="readonly")
    functions_cb.grid(row=1, column=6, padx=5)

    plot_frame = ttk.Frame(window)  # Frame for the plot
    plot_frame.pack()

    plot_container = ttk.Frame(plot_frame)
    plot_container.pack()

    

    start_button = ttk.Button(frame, text="Start Optimization", command=start_optimization)
    start_button.grid(row=3, column=5)

    return frame
    

    
window = tk.Tk()
window.geometry("1000x600")
window.title("Grey Wolf Optimizer Parameters")

gwo_frame = create_optimization_frame(window, GWO)  # Create frame for Grey Wolf Optimizer
gwo_frame.pack()
gwo_fr = create_optimization_frame(window, GWO)  # Create frame for Grey Wolf Optimizer
gwo_fa=create_optimization_frame(window, GWO)  # Create frame for Grey Wolf Optimizer
gwo_fa.pack()



# You can create frames for other algorithms similarly
# algo2_frame = create_optimization_frame(window, Algorithm2)
# algo2_frame.pack()

window.mainloop()
