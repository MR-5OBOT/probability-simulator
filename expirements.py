import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from custom_func.sim_func import probability_simulator, savePlot

# Main GUI setup
app = tk.Tk()
style = ttk.Style(app) # Create a style object
style.theme_use("clam")

app.tk.call('source', 'themes/forest-dark.tcl') # Load custom theme
style.theme_use('forest-dark') # Set custom theme

app.title("Traders Toolbox")
# app.geometry("1200x650") # Set window size dynamically
app.attributes("-fullscreen", True)

notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True)

# Create individual tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Configure grid layout to make it resizable
tab1.grid_rowconfigure(0, weight=1)
tab1.grid_columnconfigure(0, weight=1)

notebook.add(tab1, text="Probability Simulator")
notebook.add(tab2, text="Tab2")

#----- Tab1 input frame -----#
inputsLabel = ttk.LabelFrame(tab1, text="Simulation inputs", padding=(10, 10))
inputsLabel.grid(padx=5, pady=5, column=0, row=0, sticky="nsew")

# balanceEntry = ttk.Entry(inputsLabel)
# balanceEntry.insert(0, 'balance')
# balanceEntry.bind("<FocusIn>", lambda args: balanceEntry.delete('0', 'end')) # Clear the entry when clicked
# balanceEntry.grid(column=0, row=0, sticky="ew", pady=5)
#
# riskEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.1)
# riskEntry.insert(0, 'risk')
# riskEntry.bind("<FocusIn>", lambda args: riskEntry.delete('0', 'end'))
# riskEntry.grid(column=0, row=1, sticky="ew", pady=5)
#
# rrEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.1)
# rrEntry.insert(0, 'risk reward')
# rrEntry.bind("<FocusIn>", lambda args: rrEntry.delete('0', 'end'))
# rrEntry.grid(column=0, row=2, sticky="ew", pady=5)
#
# nTrades_entry = ttk.Entry(inputsLabel)
# nTrades_entry.insert(0, 'number of trades')
# nTrades_entry.bind("<FocusIn>", lambda args: nTrades_entry.delete('0', 'end'))
# nTrades_entry.grid(column=0, row=3, sticky="ew", pady=5)
#
# calculateButton = ttk.Button(inputsLabel, text="Calculate", command=lambda: probability_simulator(balanceEntry, riskEntry, rrEntry, nTrades_entry))
# calculateButton.grid(column=0, row=4, sticky="ew", pady=5)
# save_button = ttk.Button(inputsLabel, text="Save Results", command=lambda: savePlot())
# save_button.grid(column=0, row=5, sticky="", pady=5)

#----- tab1 plot frame -----#
plotFrame = ttk.LabelFrame(tab1, text="Plot", padding=(10, 10))
plotFrame.grid(pady=5, column=1, row=0, sticky="nsew")











app.mainloop()

