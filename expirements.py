import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from custom_func.sim_func import probability_simulator

# Main GUI setup
app = tk.Tk()
style = ttk.Style(app) # Create a style object
style.theme_use("clam")

app.tk.call('source', 'themes/forest-dark.tcl') # Load custom theme
style.theme_use('forest-dark') # Set custom theme

app.title("Traders Toolbox")
app.geometry("1200x650") # Set window size dynamically

notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Probability Simulator")
notebook.add(tab2, text="Tab2")

inputsLabel = ttk.LabelFrame(tab1, text="Simulation inputs", borderwidth=2, relief="raised", padding=(10, 10))
inputsLabel.grid(column=0, row=0, padx=10, pady=10, sticky="ew")

balanceEntry = ttk.Entry(inputsLabel)
balanceEntry.insert(0, 'balance')
balanceEntry.bind("<FocusIn>", lambda args: balanceEntry.delete('0', 'end')) # Clear the entry when clicked
balanceEntry.grid(column=0, row=0, sticky="ew", pady=5)

riskEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.1)
riskEntry.insert(0, 'risk')
riskEntry.bind("<FocusIn>", lambda args: riskEntry.delete('0', 'end'))
riskEntry.grid(column=0, row=1, sticky="ew", pady=5)

rrEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.1)
rrEntry.insert(0, 'risk reward')
rrEntry.bind("<FocusIn>", lambda args: rrEntry.delete('0', 'end'))
rrEntry.grid(column=0, row=2, sticky="ew", pady=5)

nTrades_entry = ttk.Entry(inputsLabel)
nTrades_entry.insert(0, 'number of trades')
nTrades_entry.bind("<FocusIn>", lambda args: nTrades_entry.delete('0', 'end'))
nTrades_entry.grid(column=0, row=3, sticky="ew", pady=5)

calculateButton = ttk.Button(inputsLabel, text="Calculate", command=lambda: probability_simulator(balanceEntry, riskEntry, rrEntry, nTrades_entry))
calculateButton.grid(column=0, row=4, sticky="ew", pady=5)












app.mainloop()

