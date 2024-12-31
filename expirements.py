import tkinter as tk
from src.formulas import position_size_forex, position_size_futures, probability_sim, min_winrate

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input, please enter numbers.")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Enter Number 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Number 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root)
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
root.mainloop()
