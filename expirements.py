import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create main application window
root = tk.Tk()
# root.geometry("400x400")  # Set the window size
root.title("Tabbed Application")  # Set the window title
root.state("zoomed")  # Maximize the window

style = ttk.Style()
# style.configure("TNotebook", background="white")
# style.configure("TNotebook.Tab", background="white", padding=[10, 5])
style.theme_use("clam") 





# Run the application
root.mainloop()
