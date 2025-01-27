import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import logging

# custom module
from resources.custom_func.expirements_funcs import Simulation

class Calculaions:
    def __init__(self):
        self.point_value = 2
    
    def risk_calculation(self):
        self.balance = 5000
        self.stoploss = 20
        self.risk = 1
        # formula
        self.amount_risk = (self.balance * self.risk) /100

    def position_size(self):
        self.position_size_formula = (self.amount_risk / (self.stoploss * self.point_value))

        



# Main (GUI)
class App_Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUI APP WITH CLASS")
        self.root.geometry("800x500")
        self.style = ttk.Style()
        self.style.theme_use("classic")

    def widgets(self):
        self.fram_root = ttk.Frame(self.root)
        self.fram_root.pack()
        self.label1 = ttk.Label(self.fram_root, text="HEllO WORLD")
        self.label1.pack()
        self.entry1 = ttk.Entry(self.fram_root)
        self.entry1.pack()
        self.button1 = ttk.Button(self.fram_root)
        self.button1.pack()


# run the app
if __name__ == "__main__":
    app = App_Gui()
    app.widgets()
    app.root.mainloop()
        
