import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from random import random

# Import the functions
from formulas.position_size import get_position_sizing_result


# Main app window
app = tk.Tk()
app.title("Trading Toolbox")
app.geometry("500x400")

# colors
# style = ttk.Style()
# style.config("TNotebook", background="#161616")
# style.config("TNotebook.Tab", background="#101010", font=("Arial", 10))
# style.config("TFrame", background="grey")

# Create a Notebook
notebook = ttk.Notebook(app, style="Vertical.TNotebook") # Create a Notebook with vertical tabs
notebook.pack(expand=True, fill="both")

# Apply a custom style for vertical tabs
style = ttk.Style(app)
style.configure("Vertical.TNotebook", tabposition='wn')  # west, wn
style.configure("Vertical.TNotebook.Tab", width=20, padding=(10, 10))

# Add Tabs
position_sizing_forex_tab = ttk.Frame(notebook)
position_sizing_futures_tab = ttk.Frame(notebook)
probability_sim_tab = ttk.Frame(notebook)

notebook.add(position_sizing_forex_tab, text="Position Sizing forex")
notebook.add(position_sizing_futures_tab, text="Position Sizing futures")
notebook.add(probability_sim_tab, text="probability simulator")


# ------------------------------------------------------------------
def calculate_position_size():
    account_balance = float(entry_account_balance.get())
    risk_percentage = float(entry_risk_percentage.get())
    stop_loss_pips = float(entry_stop_loss_pips.get())
    pip_value = float(entry_pip_value.get())
    result = get_position_sizing_result(account_balance, risk_percentage, stop_loss_pips, pip_value)
    label_result.config(text=result)

tk.Label(position_sizing_forex_tab, text="Position Sizing (Forex)", font=("Arial", 20)).pack(pady=20)

tk.Label(position_sizing_forex_tab, text="Account Balance:").pack()
entry_account_balance = tk.Entry(position_sizing_forex_tab)
entry_account_balance.pack()

tk.Label(position_sizing_forex_tab, text="Risk Percentage:").pack()
entry_risk_percentage = tk.Entry(position_sizing_forex_tab)
entry_risk_percentage.pack()

tk.Label(position_sizing_forex_tab, text="Stop Loss (pips):").pack()
entry_stop_loss_pips = tk.Entry(position_sizing_forex_tab)
entry_stop_loss_pips.pack()

tk.Label(position_sizing_forex_tab, text="pip value:").pack()
entry_pip_value = tk.Entry(position_sizing_forex_tab)
entry_pip_value.pack()

button_calculate = tk.Button(position_sizing_forex_tab, text="Calculate", command=calculate_position_size)
button_calculate.pack(padx=5, pady=5)

label_result = tk.Label(position_sizing_forex_tab)
label_result.pack()

# probability simulator func
def probability_simulator():
    try:
        # Get user inputs
        initial_balance = float(balance_entry.get())
        risk_percent = float(risk_entry.get())
        rr_ratio = float(rr_entry.get())
        num_trades = int(trades_entry.get())

        # Validate inputs
        if initial_balance <= 0 or risk_percent <= 0 or rr_ratio <= 0 or num_trades <= 0:
            sim_label.config(text="Error: All inputs must be positive numbers.")

        # Simulation logic
        balance = initial_balance
        balance_history = [initial_balance]
        wins = 0
        for _ in range(num_trades):
            risk_amount = balance * (risk_percent / 100)
            if random() > 0.5:
                balance += risk_amount * rr_ratio
                wins += 1
            else:
                balance -= risk_amount
            balance_history.append(balance)

        # Calculate results
        win_rate = (wins / num_trades) * 100
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Display results
        messagebox.showinfo(message=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nWin Rate: {win_rate:.2f}%")

        # Plot the balance history
        plt.style.use("ggplot")
        plt.plot(balance_history)
        plt.title("Trading Simulation Results")
        plt.xlabel("Number of Trades")
        plt.ylabel("Balance ($)")
        plt.grid(True)
        plt.savefig("Simulation.png")
        # plt.show()

    except ValueError:
        sim_label.config(text="Error: Please enter valid numbers.")


# probability_simulator GUI
tk.Label(probability_sim_tab, text="Trading Simulator", font=("Arial", 24)).pack(pady=20)

tk.Label(probability_sim_tab, text="Initial Balance:").pack()
balance_entry = tk.Entry(probability_sim_tab)
balance_entry.pack(pady=5)

tk.Label(probability_sim_tab, text="Risk Percentage:").pack()
risk_entry = tk.Entry(probability_sim_tab)
risk_entry.pack(pady=5)

tk.Label(probability_sim_tab, text="Risk-Reward Ratio:").pack()
rr_entry = tk.Entry(probability_sim_tab)
rr_entry.pack(pady=5)

tk.Label(probability_sim_tab, text="Number of Trades:").pack()
trades_entry = tk.Entry(probability_sim_tab)
trades_entry.pack(pady=5)

tk.Button(probability_sim_tab, text="Run Simulation", command=probability_simulator).pack()

sim_label = tk.Label(probability_sim_tab, text="")
sim_label.pack(pady=10)


# popup after closing
def on_closing(): 
    messagebox.showwarning(title="DON'T FORGET", message="accept the loss before it happens")
    app.destroy()
app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop() # Run App




