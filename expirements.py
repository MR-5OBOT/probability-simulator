import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure

from expirements_funcs import complex_simulator, update_plot


def calculate_and_plot():
    balance_history = complex_simulator(balanceEntry, winrateEntry, riskEntry, rrEntry, consecutive_LossesEntry, nTrades_entry, result_label)
    update_plot(plotFrame, balance_history)

#----- Main App -----#
app = tk.Tk()
style = ttk.Style(app) # Create a style object
style.theme_use("clam")

app.tk.call('source', './resources/Forest-ttk-theme/forest-dark.tcl') # Load custom theme
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
notebook.add(tab2, text="Tab2")

#----- Tab1 input frame -----#
inputsLabel = ttk.LabelFrame(tab1, text="Simulation inputs", padding=(15, 15))
inputsLabel.pack(side="left", padx=10)

balanceEntry = ttk.Spinbox(inputsLabel, from_=1000, to=1000000, increment=100)
balanceEntry.insert(0, 'balance')
balanceEntry.bind("<FocusIn>", lambda _: balanceEntry.delete('0', 'end')) # Clear the entry when clicked
balanceEntry.grid(column=0, row=0, sticky="ew", pady=5)

winrateEntry = ttk.Spinbox(inputsLabel, from_=0, to=1, increment=0.1)
winrateEntry.insert(0, "winrate (decimal)")
winrateEntry.bind("<FocusIn>", lambda _: winrateEntry.delete('0', 'end')) # Clear the entry when clicked
winrateEntry.grid(column=0, row=1, sticky="ew", pady=5)

riskEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.1)
riskEntry.insert(0, 'risk percentage')
riskEntry.bind("<FocusIn>", lambda _: riskEntry.delete('0', 'end'))
riskEntry.grid(column=0, row=2, sticky="ew", pady=5)

rrEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.5)
rrEntry.insert(0, 'risk reward')
rrEntry.bind("<FocusIn>", lambda _: rrEntry.delete('0', 'end'))
rrEntry.grid(column=0, row=3, sticky="ew", pady=5)

nTrades_entry = ttk.Spinbox(inputsLabel, from_=0, to=1000, increment=1)
nTrades_entry.insert(0, 'total trades')
nTrades_entry.bind("<FocusIn>", lambda _: nTrades_entry.delete('0', 'end'))
nTrades_entry.grid(column=0, row=4, sticky="ew", pady=5)

consecutive_LossesEntry = ttk.Spinbox(inputsLabel, from_=0, to=1000, increment=1)
consecutive_LossesEntry.insert(0, 'losses treshold')
consecutive_LossesEntry.bind("<FocusIn>", lambda _: consecutive_LossesEntry.delete('0', 'end'))
consecutive_LossesEntry.grid(column=0, row=5, sticky="ew", pady=5)
consecutive_LossesEntry.config(state="disabled")

# the function that will be triggered when the checkbox is toggled
def risk_reducer_func():
    # Check if the Checkbutton is checked
    if check_var.get() == 1:  # If checked
        consecutive_LossesEntry.config(state='normal')  # Enable entry2
    else:  # If unchecked
        consecutive_LossesEntry.delete(0)
        consecutive_LossesEntry.config(state='disabled')  # Disable entry2


# Variable for Checkbutton state
check_var = tk.IntVar()

# Create Checkbutton and place it inside the LabelFrame
risk_reducerbutton = ttk.Checkbutton(inputsLabel, text="Risk Reducer", variable=check_var, command=risk_reducer_func)
risk_reducerbutton.grid(column=0, row=6, pady=5)

calculateButton = ttk.Button(inputsLabel, text="Calculate", command=calculate_and_plot)
calculateButton.grid(column=0, row=7, sticky="ew", pady=5)

separator = ttk.Separator(inputsLabel, orient="horizontal")
separator.grid(column=0, row=8, sticky="nsew", pady=5)

result_frame = ttk.LabelFrame(inputsLabel, text="Results")
result_frame.grid(column=0, row=9, sticky="nsew")
result_label = ttk.Label(result_frame, text="", anchor="center")
result_label.pack(expand=True, fill="both", padx=5, pady=5)

# save_pic = ttk.Button(inputsLabel, text="Save plot", command="")
# save_pic.grid()


#----- tab1 plot frame -----#
plotFrame = ttk.LabelFrame(tab1, text="Plot Graph", padding=(15, 15))
plotFrame.pack(expand=True, fill="both", side="right")

# Configure grid weights for responsiveness
tab1.grid_rowconfigure(0, weight=1) 
tab1.grid_columnconfigure(1, weight=1)



app.mainloop()
