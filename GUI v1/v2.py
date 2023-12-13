import string
import functions
from enumFunctions import Functions
from GWO import GWO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk



def start_optimization(frames):
   for frame, plot_container in frames:
        selected_alg = frame.children['!combobox'].get()
        selected_lb = float(frame.children['!combobox2'].get())
        selected_ub = float(frame.children['!combobox3'].get())
        selected_dim = int(frame.children['!combobox4'].get())
        selected_search_agents = int(frame.children['!combobox5'].get())
        selected_max_iter = int(frame.children['!combobox6'].get())

        selected_func = functions.selectFunction(Functions[frame.children['!combobox7'].get()])

        result = GWO(selected_func, selected_lb, selected_ub, selected_dim, selected_search_agents, selected_max_iter)

        for widget in plot_container.winfo_children():
            widget.destroy()
        
        # Plotting
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.plot(result.convergence)
        ax.set_title(selected_alg)
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Alpha Score")
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=plot_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)



def create_optimization_frame(window):


    frame = ttk.Frame(window)
    frame.pack()

    alg_label= ttk.Label(frame, text="Select Algorithm")
    alg_label.grid(row=0, column=0, padx=5)
    alg = ttk.Combobox(frame, values=["GA","SA","GWO","PSO","HS"], state="readonly")
    alg.grid(row=1,column=0, padx=5)


    lb_label = ttk.Label(frame, text="Select Lower Bound:")
    lb_label.grid(row=0, column=1, padx=5)
    lb = ttk.Combobox(frame, values=[-32.768,-600,-500,-5.12,-5.12,-30,-5,-2048,-10], state="readonly")
    lb.grid(row=1, column=1, padx=5)

    ub_label = ttk.Label(frame, text="Select Upper Bound:")
    ub_label.grid(row=0, column=2, padx=5)
    ub = ttk.Combobox(frame, values=[32.768, 600, 500,5.12, 30, 2048, 10], state="readonly")
    ub.grid(row=1, column=2, padx=5)

    dim_label = ttk.Label(frame, text="Select Dimension:")
    dim_label.grid(row=0, column=3, padx=5)
    dim = ttk.Combobox(frame, values=[5, 10, 15, 20,25,30], state="readonly")
    dim.grid(row=1, column=3, padx=5)

    search_agents_label = ttk.Label(frame, text="Select Search Agents:")
    search_agents_label.grid(row=0, column=4, padx=5)
    search_agents = ttk.Combobox(frame, values=[5, 10, 15, 20, 500], state="readonly")
    search_agents.grid(row=1, column=4, padx=5)

    
    max_iter_label = ttk.Label(frame, text="Select Max Iterations:")
    max_iter_label.grid(row=0, column=5, padx=5)
    max_iter = ttk.Combobox(frame, values=[100, 500, 1000, 1500], state="readonly")
    max_iter.grid(row=1, column=5, padx=5)

    
    functions_label = ttk.Label(frame, text="Select Objective Function:")
    functions_label.grid(row=0, column=6, padx=5)
    functions_cb = ttk.Combobox(frame, values=["ackley","griewank", "schwefel","rastrigin","sphere","perm","zakharov", "rosenbrock","dixonprice"], state="readonly")
    functions_cb.grid(row=1, column=6, padx=5)

    plot_frame = ttk.Frame(window)  # Frame for the plot
    plot_frame.pack()

    plot_container = ttk.Frame(plot_frame)
    plot_container.grid(row=3, column=0, padx=5, pady=5)
    return frame, plot_container,
def create_and_pack_frames(window, num_frames):
    frames = []
    for _ in range(num_frames):
        frame, plot_container = create_optimization_frame(window)
        frames.append((frame, plot_container))
        frame.pack()
    return frames

    
window = tk.Tk()
window.geometry("1000x600")
window.title("Grey Wolf Optimizer Parameters")


# Create three optimization frames
num_frames = 1
frames = create_and_pack_frames(window, num_frames)

start_button = ttk.Button(window, text="Start Optimization", command=lambda: start_optimization(frames))
start_button.pack()



window.mainloop()
