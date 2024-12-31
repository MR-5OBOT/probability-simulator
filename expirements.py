
import customtkinter as ctk
from tkinter import ttk
import matplotlib.pyplot as plt
from tkinter import messagebox
import random

# Import the functions
from formulas.position_size_forex import get_position_sizing_result_forex
from formulas.position_size_futures import get_position_sizing_result_futures

# set up the GUI appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# GUI Setup
app = ctk.CTk()
app.geometry("600x500")
app.title("Traders Toolbox")
app.resizable(False, False)

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


# position_size_forex
def calculate_position_size_forex():
    account_balance = float(entry_account_balance_forex.get())
    risk_dollar = float(entry_amount_risk_forex.get().strip("$"))
    stop_loss_pips = float(entry_stop_loss_pips_forex.get())
    pip_value = float(entry_pip_value_forex.get())
    result = get_position_sizing_result_forex(account_balance, risk_dollar, stop_loss_pips, pip_value)
    # label_result.configure(text=result)

ctk.CTkLabel(position_sizing_forex_tab, text="Position Sizing (Forex)", font=("Arial", 20)).pack(pady=20)

ctk.CTkLabel(position_sizing_forex_tab, text="Account Balance:").pack(pady=2)
entry_account_balance_forex = ctk.CTkEntry(position_sizing_forex_tab)
entry_account_balance_forex.pack(pady=2)

ctk.CTkLabel(position_sizing_forex_tab, text="Dollar Risk $:").pack(pady=2)
entry_amount_risk_forex = ctk.CTkEntry(position_sizing_forex_tab)
entry_amount_risk_forex.pack(pady=2)

ctk.CTkLabel(position_sizing_forex_tab, text="Stop Loss (pips):").pack(pady=2)
entry_stop_loss_pips_forex = ctk.CTkEntry(position_sizing_forex_tab)
entry_stop_loss_pips_forex.pack(pady=2)

ctk.CTkLabel(position_sizing_forex_tab, text="Pip value: (eurusd=10$)").pack(pady=2)
entry_pip_value_forex = ctk.CTkEntry(position_sizing_forex_tab)
entry_pip_value_forex.pack(pady=2)

button_calculate = ctk.CTkButton(position_sizing_forex_tab, text="Calculate", command=calculate_position_size_forex)
button_calculate.pack(padx=5, pady=5)

# label_result = ctk.CTkLabel(position_sizing_forex_tab, text="")
# label_result.pack(pady=2)


# position_size_futures
def calculate_position_size_futures():
    account_balance = float(entry_account_balance_futures.get())
    risk_dollar = entry_amount_risk_futures.get().strip("$")
    stop_loss_pips = float(entry_stop_loss_points_futures.get())
    point_value = float(entry_point_value_futures.get())
    result = get_position_sizing_result_futures(account_balance, risk_dollar, stop_loss_pips, point_value)
    # label_result.configure(text=result)

ctk.CTkLabel(position_sizing_futures_tab, text="Position Sizing (Futures)", font=("Arial", 20)).pack(pady=20)

ctk.CTkLabel(position_sizing_futures_tab, text="Account Balance:").pack(pady=2)
entry_account_balance_futures = ctk.CTkEntry(position_sizing_futures_tab)
entry_account_balance_futures.pack(pady=2)

ctk.CTkLabel(position_sizing_futures_tab, text="Dollar Risk $:").pack(pady=2)
entry_amount_risk_futures = ctk.CTkEntry(position_sizing_futures_tab)
entry_amount_risk_futures.pack(pady=2)

ctk.CTkLabel(position_sizing_futures_tab, text="Stop Loss (points):").pack(pady=2)
entry_stop_loss_points_futures = ctk.CTkEntry(position_sizing_futures_tab)
entry_stop_loss_points_futures.pack(pady=2)

ctk.CTkLabel(position_sizing_futures_tab, text="P value: MNQ=2$ MES=5$").pack(pady=2)
entry_point_value_futures = ctk.CTkEntry(position_sizing_futures_tab)
entry_point_value_futures.pack(pady=2)

button_calculate = ctk.CTkButton(position_sizing_futures_tab, text="Calculate", command=calculate_position_size_futures)
button_calculate.pack(padx=5, pady=5)

# label_result = ctk.CTkLabel(position_sizing_futures_tab,)
# label_result.pack(pady=2)


# probability simulator func
def simulate_trading():
    """Run the trading simulation based on user inputs."""
    try:
        # Get user inputs from the GUI
        initial_balance = float(balance_entry.get())
        risk_percent = float(risk_entry.get())
        rr_ratio = float(rr_entry.get())
        num_trades = int(trades_entry.get())

        # Validate inputs
        if initial_balance <= 0 or risk_percent <= 0 or rr_ratio <= 0 or num_trades <= 0:
            result_label.configure(text="Error: All inputs must be positive numbers.")
            return

        # Initialize variables
        balance = initial_balance
        balance_history = [initial_balance]
        wins = 0

        # Simulation logic
        for trade in range(num_trades):
            risk_amount = balance * (risk_percent / 100)  # Risk as % of current balance
            if random.random() > 0.5:  # 50% chance to win
                balance += risk_amount * rr_ratio
                wins += 1
            else:
                balance -= risk_amount

            balance_history.append(balance)

        # Calculate results
        win_rate = (wins / num_trades) * 100
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Display results in the GUI
        result_label.configure(
            text=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nWin Rate: {win_rate:.2f}%"
        )

        # Plot the balance history
        plt.style.use("ggplot")
        plt.plot(balance_history)
        plt.title("Trading Simulation Results")
        plt.xlabel("Number of Trades")
        plt.ylabel("Balance ($)")
        plt.grid(True)
        plt.show()

    except ValueError:
        result_label.configure(text="Error: Please enter valid numbers.")

# Title CTkLabel
title_label = ctk.CTkLabel(probability_sim_tab, text="Probability Simulator", font=("Arial", 24))
title_label.pack(pady=20)

# Input Fields
balance_label = ctk.CTkLabel(probability_sim_tab, text="Initial Balance:")
balance_label.pack()
balance_entry = ctk.CTkEntry(probability_sim_tab)
balance_entry.pack(pady=5)

risk_label = ctk.CTkLabel(probability_sim_tab, text="Risk Percentage:")
risk_label.pack()
risk_entry = ctk.CTkEntry(probability_sim_tab)
risk_entry.pack(pady=5)

rr_label = ctk.CTkLabel(probability_sim_tab, text="Risk-Reward Ratio:")
rr_label.pack()
rr_entry = ctk.CTkEntry(probability_sim_tab)
rr_entry.pack(pady=5)

trades_label = ctk.CTkLabel(probability_sim_tab, text="Number of Trades:")
trades_label.pack()
trades_entry = ctk.CTkEntry(probability_sim_tab)
trades_entry.pack(pady=5)

# Run Simulation Button
run_button = ctk.CTkButton(probability_sim_tab, text="Run Simulation", command=simulate_trading)
run_button.pack(pady=20)

# Result CTkLabel
result_label = ctk.CTkLabel(probability_sim_tab, text="")
result_label.pack(pady=10)




# popup after closing
def on_closing(): 
    messagebox.showwarning(title="DON'T FORGET", message="accept the loss before it happens")
    app.destroy()
app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop() # Run App



