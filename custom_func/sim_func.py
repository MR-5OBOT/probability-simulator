# import tkinter as tk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
import random
from tkinter import messagebox

def probability_simulator(balanceEntry, riskEntry, rrEntry, nTrades_entry):
    try:
        # Get user inputs
        initial_balance = float(balanceEntry.get())
        risk_percent = float(riskEntry.get())
        rr_ratio = float(rrEntry.get())
        num_trades = int(nTrades_entry.get())

        # Validate inputs
        if initial_balance <= 0 or risk_percent <= 0 or rr_ratio <= 0 or num_trades <= 0:
            # sim_label.configure(text="Error: All inputs must be positive numbers.")
            messagebox.showinfo(message="Error: All inputs must be positive numbers.")
            return

        # Simulation logic
        balance = initial_balance
        global balance_history
        balance_history = [initial_balance]
        wins = 0

        # Loop through the number of trades
        for _ in range(num_trades):
            risk_amount = balance * (risk_percent / 100)
            if random.random() > 0.5:
                balance += risk_amount * rr_ratio
                wins += 1
            else:
                balance -= risk_amount

            balance_history.append(balance)

        # Calculate Max Drawdown from Balance History
        max_drawdown = 0
        peak_balance = balance_history[0]

        for bal in balance_history:
            if bal > peak_balance:
                peak_balance = bal
            drawdown = (peak_balance - bal) / peak_balance
            max_drawdown = max(max_drawdown, drawdown)

        # Convert to percentage
        max_drawdown *= 100

        # Calculate results
        win_rate = (wins / num_trades) * 100
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Display results in a messagebox
        messagebox.showinfo(message=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nWin Rate: {win_rate:.2f}%\nMax Drawdown: {max_drawdown:.2f}%")

        # Plot the results
        # plot_graph()

    except ValueError:
        messagebox.showerror(message="Error: Please enter valid numbers.")


def balance_history_var():
    return balance_history

# def plot_graph():
#     # Plot the balance history
#     # plt.style.use("ggplot")
#     plt.style.use("dark_background")
#     plt.plot(balance_history)
#     plt.title("Trading Simulation Results")
#     plt.xlabel("Number of Trades")
#     plt.ylabel("Balance ($)")
#     plt.grid(True)
#     plt.savefig("balance_history.png")
#     plt.show()

# def savePlot():
#     plt.savefig("balance_history.png")
#     messagebox.showinfo(message="Plot saved as 'balance_history.png'")
#

