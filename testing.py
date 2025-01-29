# import logging
# import random
import tkinter as tk
from tkinter import messagebox, ttk

# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure

# custom module
# from resources.custom_func.expirements_funcs import Simulation

# Main (GUI)
class App_Gui:
    # constructor
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUI APP WITH CLASS")
        self.root.geometry("800x500")
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # initializations
        self.point_value = 2
        self.balance = 0
        self.risk_percent = 0
        self.stop_loss = 0

    def input_validation(self):
        try:
            initial_balance = float(self.balance_entry.get())
            risk_percent = float(self.risk_entry.get())
            stop_loss = float(self.stop_loss_entry.get())
            return initial_balance, risk_percent, stop_loss

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    def calculate_position_size(self, initial_balance, risk_percent, stop_loss):
        # formula for position sizing futures
        position_size = (initial_balance * (risk_percent / 100)) / (self.point_value * stop_loss)

        # Update the label with the result
        self.label2.config(text=f"Position Size: {position_size:.2f}")
        return position_size

    def on_button_click(self):
        initial_balance, risk_percent, stop_loss = self.input_validation()
        self.calculate_position_size(initial_balance, risk_percent, stop_loss)

    # widgets method
    def widgets(self):
        self.fram_root = ttk.Frame(self.root)
        self.fram_root.pack(padx=10, pady=10)

        self.label1 = ttk.Label(self.fram_root, text="Position sizing (The OOP Way)")
        self.label1.pack(padx=10, pady=10)

        self.label_balance = ttk.Label(self.fram_root, text="Balance")
        self.label_balance.pack(padx=10, pady=10)
        self.balance_entry = ttk.Entry(self.fram_root)
        self.balance_entry.pack(padx=10, pady=10)

        self.label_risk = ttk.Label(self.fram_root, text="Risk %")
        self.label_risk.pack(padx=10, pady=10)
        self.risk_entry = ttk.Entry(self.fram_root)
        self.risk_entry.pack(padx=10, pady=10)

        self.label_stop_loss = ttk.Label(self.fram_root, text="Stop Loss")
        self.label_stop_loss.pack(padx=10, pady=10)
        self.stop_loss_entry = ttk.Entry(self.fram_root)
        self.stop_loss_entry.pack(padx=10, pady=10)

        self.button1 = ttk.Button(self.fram_root, command=self.on_button_click, text="CLICK ME")
        self.button1.pack(padx=10, pady=10)

        self.label2 = ttk.Label(self.fram_root, text="")
        self.label2.pack(padx=10, pady=10)


# run the app
if __name__ == "__main__":
    app = App_Gui()
    app.widgets()
    app.root.mainloop()
        
