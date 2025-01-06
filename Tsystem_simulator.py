import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import random


# Main app window
app = tk.Tk()
app.title("Traders Toolbox")
app.geometry("1200x650")
app.resizable(False, False)
# app.configure(borderwidth=5, relief="raised")

# Apply a custom style for vertical tabs
style = ttk.Style(app)
style.theme_use("clam")

# add tabs
tab_control = ttk.Notebook(app)
tab_control.pack(expand=1, fill="both")

# Create individual tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# Configure grid rows and columns
# tab1.grid_rowconfigure(0, weight=1)  # Add weight to top space
# tab1.grid_rowconfigure(1, weight=1)  # Add weight to bottom space
# tab1.grid_columnconfigure(0, weight=1)  # Add weight to left space
# tab1.grid_columnconfigure(1, weight=1)  # Add weight to right space

# add tabs to the window
tab_control.add(tab1, text="Probability Simulator")
tab_control.add(tab2, text="Monte Carlo Simulator")


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
            sim_label.configure(text="Error: All inputs must be positive numbers.")

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

        for balance in balance_history:
            if balance > peak_balance:
                peak_balance = balance
            drawdown = (peak_balance - balance) / peak_balance
            max_drawdown = max(max_drawdown, drawdown)

        # Convert to percentage
        max_drawdown *= 100
        
        # Calculate results
        win_rate = (wins / num_trades) * 100
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Print results in console
        print(total_return)
        print(max_drawdown)

        # Display results in a messagebox
        messagebox.showinfo(message=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nWin Rate: {win_rate:.2f}%\nMax Drawdown: {max_drawdown:.2f}%")

        # plot the results
        ploting()

    except ValueError:
        sim_label.configure(text="Error: Please enter valid numbers.")
        

# plot function
def ploting():
    # Plot the balance history
    plt.style.use("ggplot")
    # plt.figure(figsize=(10, 6))
    plt.plot(balance_history)
    plt.title("Trading Simulation Results")
    plt.xlabel("Number of Trades")
    plt.ylabel("Balance ($)")
    plt.grid(True)
    # plt.savefig("Simulation.png")
    plt.show()



main_label = ttk.Label(tab1, text="Trading Simulator", font=("Arial", 24))
main_label.pack()

ttk.Label(tab1, text="Initial Balance:").pack()
balance_entry = ttk.Entry(tab1)
balance_entry.pack()

# ttk.Label(tab1, text="Risk Percentage:").grid()
# risk_entry = ttk.Entry(tab1)
# risk_entry.grid()
#
# ttk.Label(tab1, text="Risk-Reward Ratio:").grid()
# rr_entry = ttk.Entry(tab1)
# rr_entry.grid()
#
# ttk.Label(tab1, text="Number of Trades:").grid()
# trades_entry = ttk.Entry(tab1)
# trades_entry.grid()
#
# ttk.Button(tab1, text="Run Simulation", command=probability_simulator).grid()
#
# sim_label = ttk.Label(tab1, text="")
# sim_label.grid()
#


app.mainloop() # Run App
