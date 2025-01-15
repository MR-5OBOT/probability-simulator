import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure

from custom_func.sim_func import probability_simulator, update_plot, complex_simulator

# finctions to Calculate and lot results
def plot_tab1():
    balance_history = probability_simulator(balanceEntry_tab1, winrateEntry_tab1, riskEntry_tab1, rrEntry_tab1, nTrades_entry_tab1, result_label_tab1)
    update_plot(plotFrame_tab1, balance_history)

def plot_tab2():
    balance_history = complex_simulator(balanceEntry_tab2, winrateEntry_tab2, riskEntry_tab2, rrEntry_tab2, consecutive_LossesEntry_tab2, nTrades_entry_tab2, result_label_tab2)
    update_plot(plotFrame_tab2, balance_history)

#----- Main App -----#
app = tk.Tk()
style = ttk.Style(app) # Create a style object
style.theme_use("clam")

app.tk.call('source', './themes/Forest-ttk-theme/forest-dark.tcl') # Load custom theme
# app.tk.call('source', './themes/Forest-ttk-theme/forest-light.tcl') # Load custom theme
style.theme_use('forest-dark') # Set custom theme

app.title("Traders Toolbox")
app.geometry("1200x650") # Set window size dynamically

notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True)

# Create individual tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Probability Simulator")
notebook.add(tab2, text="Complex Simulator")


#------------------------------- tab1 ---------------------------------------#
#----- Tab1 input frame -----#
inputsLabel_tab1 = ttk.LabelFrame(tab1, text="Simulation inputs", padding=(15, 15))
inputsLabel_tab1.pack(side="left", padx=10)

balanceEntry_tab1 = ttk.Spinbox(inputsLabel_tab1, from_=1000, to=1000000, increment=100)
balanceEntry_tab1.insert(0, 'balance')
balanceEntry_tab1.bind("<FocusIn>", lambda _: balanceEntry_tab1.delete('0', 'end')) # Clear the entry when clicked
balanceEntry_tab1.grid(column=0, row=0, sticky="ew", pady=5)

winrateEntry_tab1 = ttk.Spinbox(inputsLabel_tab1, from_=0, to=1, increment=0.1)
winrateEntry_tab1.insert(0, "winrate (decimal)")
winrateEntry_tab1.bind("<FocusIn>", lambda _: winrateEntry_tab1.delete('0', 'end')) # Clear the entry when clicked
winrateEntry_tab1.grid(column=0, row=1, sticky="ew", pady=5)

riskEntry_tab1 = ttk.Spinbox(inputsLabel_tab1, from_=0, to=5, increment=0.1)
riskEntry_tab1.insert(0, 'risk percentage')
riskEntry_tab1.bind("<FocusIn>", lambda _: riskEntry_tab1.delete('0', 'end'))
riskEntry_tab1.grid(column=0, row=2, sticky="ew", pady=5)

rrEntry_tab1 = ttk.Spinbox(inputsLabel_tab1, from_=0, to=5, increment=0.5)
rrEntry_tab1.insert(0, 'risk reward')
rrEntry_tab1.bind("<FocusIn>", lambda _: rrEntry_tab1.delete('0', 'end'))
rrEntry_tab1.grid(column=0, row=3, sticky="ew", pady=5)

nTrades_entry_tab1 = ttk.Spinbox(inputsLabel_tab1, from_=0, to=1000, increment=1)
nTrades_entry_tab1.insert(0, 'total trades')
nTrades_entry_tab1.bind("<FocusIn>", lambda _: nTrades_entry_tab1.delete('0', 'end'))
nTrades_entry_tab1.grid(column=0, row=4, sticky="ew", pady=5)

calculateButton_tab1 = ttk.Button(inputsLabel_tab1, text="Calculate", command=plot_tab1)
calculateButton_tab1.grid(column=0, row=5, sticky="ew", pady=5)

separator_tab1 = ttk.Separator(inputsLabel_tab1, orient="horizontal")
separator_tab1.grid(column=0, row=6, sticky="nsew", pady=5)

result_frame_tab1 = ttk.LabelFrame(inputsLabel_tab1, text="Results")
result_frame_tab1.grid(column=0, row=7, sticky="nsew")
result_label_tab1 = ttk.Label(result_frame_tab1, text="", anchor="center")
result_label_tab1.pack(expand=True, fill="both", padx=5, pady=5)

#----- tab1 plot frame -----#
plotFrame_tab1 = ttk.LabelFrame(tab1, text="Plot Graph", padding=(15, 15))
plotFrame_tab1.pack(expand=True, fill="both", side="right")

# Configure grid weights for responsiveness
tab1.grid_rowconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

#------------------------------- tab2 ---------------------------------------#
#----- Tab2 input frame -----#
inputsLabel_tab2 = ttk.LabelFrame(tab2, text="Simulation inputs", padding=(15, 15))
inputsLabel_tab2.pack(side="left", padx=10)

balanceEntry_tab2 = ttk.Spinbox(inputsLabel_tab2, from_=1000, to=1000000, increment=100)
balanceEntry_tab2.insert(0, 'balance')
balanceEntry_tab2.bind("<FocusIn>", lambda _: balanceEntry_tab2.delete('0', 'end')) # Clear the entry when clicked
balanceEntry_tab2.grid(column=0, row=0, sticky="ew", pady=5)

winrateEntry_tab2 = ttk.Spinbox(inputsLabel_tab2, from_=0, to=1, increment=0.1)
winrateEntry_tab2.insert(0, "winrate (decimal)")
winrateEntry_tab2.bind("<FocusIn>", lambda _: winrateEntry_tab2.delete('0', 'end')) # Clear the entry when clicked
winrateEntry_tab2.grid(column=0, row=1, sticky="ew", pady=5)

riskEntry_tab2 = ttk.Spinbox(inputsLabel_tab2, from_=0, to=5, increment=0.1)
riskEntry_tab2.insert(0, 'risk percentage')
riskEntry_tab2.bind("<FocusIn>", lambda _: riskEntry_tab2.delete('0', 'end'))
riskEntry_tab2.grid(column=0, row=2, sticky="ew", pady=5)

rrEntry_tab2 = ttk.Spinbox(inputsLabel_tab2, from_=0, to=5, increment=0.5)
rrEntry_tab2.insert(0, 'risk reward')
rrEntry_tab2.bind("<FocusIn>", lambda _: rrEntry_tab2.delete('0', 'end'))
rrEntry_tab2.grid(column=0, row=3, sticky="ew", pady=5)

nTrades_entry_tab2 = ttk.Spinbox(inputsLabel_tab2, from_=0, to=1000, increment=1)
nTrades_entry_tab2.insert(0, 'total trades')
nTrades_entry_tab2.bind("<FocusIn>", lambda _: nTrades_entry_tab2.delete('0', 'end'))
nTrades_entry_tab2.grid(column=0, row=4, sticky="ew", pady=5)

consecutive_LossesEntry_tab2 = ttk.Spinbox(inputsLabel_tab2, from_=0, to=10)
consecutive_LossesEntry_tab2.insert(0, "losses threshold")
consecutive_LossesEntry_tab2.bind("<FocusIn>", lambda _: consecutive_LossesEntry_tab2.delete('0', 'end'))
consecutive_LossesEntry_tab2.grid(column=0, row=5, pady=5)

calculateButton_tab2 = ttk.Button(inputsLabel_tab2, text="Calculate", command=plot_tab2)
calculateButton_tab2.grid(column=0, row=6, sticky="ew", pady=5)

separator_tab2 = ttk.Separator(inputsLabel_tab2, orient="horizontal")
separator_tab2.grid(column=0, row=8, sticky="nsew", pady=5)

result_frame_tab2 = ttk.LabelFrame(inputsLabel_tab2, text="Results")
result_frame_tab2.grid(column=0, row=9, sticky="nsew")
result_label_tab2 = ttk.Label(result_frame_tab2, text="", anchor="center")
result_label_tab2.pack(expand=True, fill="both", padx=5, pady=5)

#----- tab2 plot frame -----#
plotFrame_tab2 = ttk.LabelFrame(tab2, text="Plot Graph", padding=(15, 15))
plotFrame_tab2.pack(expand=True, fill="both", side="right")

# Configure grid weights for responsiveness
tab2.grid_rowconfigure(0, weight=1) 
tab2.grid_columnconfigure(1, weight=1)




# toggle dark and light mode

app.mainloop()

