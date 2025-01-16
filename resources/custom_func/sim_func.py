# import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
from tkinter import messagebox
# from tkinter import filedialog


def probability_simulator(balanceEntry, winrateEntry, riskEntry, rrEntry, nTrades_entry, result_label):
    try:
        # Get user inputs
        initial_balance = float(balanceEntry.get())
        winrate = float(winrateEntry.get())
        risk_percent = float(riskEntry.get())
        rr_ratio = float(rrEntry.get())
        num_trades = int(nTrades_entry.get())

        # Validate inputs
        if initial_balance <= 0 or risk_percent <= 0 or rr_ratio <= 0 or num_trades <= 0:
            result_label.configure(text="Error: All inputs must be positive numbers.")
            messagebox.showinfo(message="Error: All inputs must be positive numbers.")
            return

        # Simulation logic
        balance = initial_balance
        balance_history = [initial_balance]
        wins = 0

        # Loop through the number of trades
        for _ in range(num_trades):
            risk_amount = balance * (risk_percent / 100)
            if random.random() <= winrate:
                balance += (risk_amount * rr_ratio)
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
        # win_rate = (wins / num_trades) * 100
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Display results in a messagebox
        messagebox.showinfo(message=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nMax Drawdown: {max_drawdown:.2f}%")
        result_label.configure(text=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nMax Drawdown: {max_drawdown:.2f}%")

        # return balance_history
        return balance_history

    except ValueError:
        messagebox.showerror(message="Error: Please enter valid numbers.")
        result_label.configure(text="Error: Please enter valid numbers.")


#------- simulation based on risk model --------#
def complex_simulator(balanceEntry, winrateEntry, riskEntry, rrEntry, consecutive_LossesEntry, nTrades_entry, result_label):
    try:
        # Get user inputs
        initial_balance = float(balanceEntry.get())
        winrate = float(winrateEntry.get())
        risk_percent = float(riskEntry.get())
        rr_ratio = float(rrEntry.get())
        consecutive_L_treshold = float(consecutive_LossesEntry.get())
        # risk_reducer = float(risk_reducerEntry.get())
        num_trades = int(nTrades_entry.get())

        # Validate inputs
        if initial_balance <= 0 or risk_percent <= 0 or rr_ratio <= 0 or num_trades <= 0:
            result_label.configure(text="Error: All inputs must be positive numbers.")
            messagebox.showinfo(message="Error: All inputs must be positive numbers.")
            return

        # Initialize variables
        balance = initial_balance
        balance_history = [initial_balance]
        wins = 0
        consecutive_losses = 0
        max_consecutive_losses = 0

        # Loop through the number of trades
        for _ in range(num_trades):
            risk_amount = balance * (risk_percent / 100)
            if random.random() <= winrate:
                balance += (risk_amount * rr_ratio)
                wins += 1
                consecutive_losses = 0
            else:
                balance -= risk_amount
                consecutive_losses += 1
                max_consecutive_losses = max(max_consecutive_losses, consecutive_losses)

                # reduce risk after x consecutive_losses
                if consecutive_losses >= consecutive_L_treshold:
                    risk_amount /= 2  # Reduce risk by 50% (adjust this factor as needed)

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
        # win_rate = (wins / num_trades) * 100
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Display results in a messagebox
        messagebox.showinfo(message=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nMax Drawdown: {max_drawdown:.2f}%\nConsecutive Losses: {max_consecutive_losses}")
        result_label.configure(text=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nMax Drawdown: {max_drawdown:.2f}%\nConsecutive Losses: {max_consecutive_losses}")

        # return balance_history
        return balance_history

    except ValueError:
        messagebox.showerror(message="Error: Please enter valid numbers.")
        result_label.configure(text="Error: Please enter valid numbers.")


#------------ ploting -------------#
def update_plot(plotFrame, balance_history):
    # Clear the previous plot
    for widget in plotFrame.winfo_children():
        widget.destroy()

    plt.style.use("dark_background")
    # plt.rcParams["figure.figsize"] = (10, 4)
    fig = Figure()
    ax = fig.add_subplot()
    ax.plot(balance_history)  # Example data
    ax.set_title("Simulation Results", color='grey', fontsize=18, loc='center', pad=20)
    # ax.set_xlabel("Number of Trades")
    # ax.set_ylabel("Account Balance")
    # ax.grid(color='#1E1E1E', linestyle='--', linewidth=1)
    # ax.legend()
    # Add a watermark
    ax.text(
        0.5, 0.5,               # X and Y position (relative, in axes coordinates)
        "MR5OBOT S-SIMULATOR",         # Watermark text
        fontsize=25,            # Font size
        color='gray',           # Text color
        alpha=0.15,              # Transparency (0.0 to 1.0)
        ha='center',            # Horizontal alignment
        va='center',            # Vertical alignment
        rotation=10,            # Rotate text
        transform=ax.transAxes  # Transform relative to the axes (0 to 1 range)
        )

    # remove right line and top line
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    
    #--------- Theming --------------#
    # # change balance_history line color
    # ax.lines[0].set_color("#08134E")
    #
    # # change x y line color
    # ax.spines['bottom'].set_color('#217346')
    # ax.spines['left'].set_color('#217346')
    # # ax.spines['top'].set_color('#4E83A3')
    # # ax.spines['right'].set_color('#4E83A3')
    #
    # # change x y ticks color
    # ax.tick_params(axis='x', colors='grey')
    # ax.tick_params(axis='y', colors='grey')
    #
    # # change x y ticks style
    # ax.tick_params(axis='x', direction='inout', length=6, width=2)
    # ax.tick_params(axis='y', direction='inout', length=6, width=2)
    #
    # # change x y label color
    # ax.xaxis.label.set_color('white')
    # ax.yaxis.label.set_color('white')
    #
       #
    # # change x y label line style
    # # ax.spines['bottom'].set_linestyle('--')
    # # ax.spines['left'].set_linestyle('--')
    #
    # # change x y label line width
    # ax.spines['bottom'].set_linewidth(2)
    # ax.spines['left'].set_linewidth(2)
    #
    # control ticks spacing make it dynamic
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    # add canvas to the plotFrame
    canvas = FigureCanvasTkAgg(fig, master=plotFrame)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()


