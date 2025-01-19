# import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
from tkinter import messagebox
# from tkinter import filedialog


#------- simulation based on risk model --------#
def complex_simulator(balanceEntry, winrateEntry, riskEntry, rrEntry, consecutive_LossesEntry, nTrades_entry, result_label):
    try:
        # Get user inputs
        initial_balance = float(balanceEntry.get())
        winrate = float(winrateEntry.get())
        risk_percent = float(riskEntry.get())
        rr_ratio = float(rrEntry.get())
        consecutive_L_treshold = consecutive_LossesEntry.get().strip()  # .strip() to remove extra spaces
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

        reduced_risk_active = False  # Track if risk reduction is active

        for trade in range(num_trades):
            # Calculate the risk amount
            if reduced_risk_active:
                risk_amount = balance * (risk_percent / 100) / 2  # Reduced risk
            else:
                risk_amount = balance * (risk_percent / 100)  # Normal risk

            # Simulate trade outcome
            if random.random() <= winrate:
                balance += (risk_amount * rr_ratio)
                wins += 1
                consecutive_losses = 0
                reduced_risk_active = False  # Reset risk reduction on a win
            else:
                balance -= risk_amount
                consecutive_losses += 1
                max_consecutive_losses = max(max_consecutive_losses, consecutive_losses)

            # Check for consecutive losses threshold
            if consecutive_L_treshold:  # Only reduce risk if the input is not empty
                try:
                    threshold = int(consecutive_L_treshold)
                    if consecutive_losses >= threshold:
                        reduced_risk_active = True  # Activate risk reduction
                except ValueError:
                    pass  # If conversion fails, don't adjust risk

            # Append the current balance to history
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

        # Calculate total return
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Display results in a messagebox
        messagebox.showinfo(message=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nMax Drawdown: {max_drawdown:.2f}%\nConsecutive Losses: {max_consecutive_losses}")
        result_label.configure(text=f"Final Balance: ${balance:.2f}\nTotal Return: {total_return:.2f}%\nMax Drawdown: {max_drawdown:.2f}%\nConsecutive Losses: {max_consecutive_losses}")

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
    fig = Figure()
    ax = fig.add_subplot()
    ax.plot(balance_history)  # Example data
    ax.set_title("Simulation Results", color='grey', fontsize=20, loc='center', pad=15)
    # ax.set_xlabel("Number of Trades")
    # ax.set_ylabel("Account Balance")
    ax.grid(color='#161616', linestyle='--', linewidth=0.5, axis="both")
    # ax.legend()

    # Add a watermark
    ax.text(
        0.5, 0.5,               # X and Y position (relative, in axes coordinates)
        "@MR5OBOT",             # Watermark text
        fontsize=30,            # Font size
        color='gray',           # Text color
        alpha=0.12,             # Transparency (0.0 to 1.0)
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
    # change x y ticks style
    ax.tick_params(axis='x', direction='inout', length=6, width=2)
    ax.tick_params(axis='y', direction='inout', length=6, width=2)
    # change x y label line width
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)

    # # change x y line color
    ax.spines['bottom'].set_color('grey')
    ax.spines['left'].set_color('grey')
    # # ax.spines['top'].set_color('#4E83A3')
    # # ax.spines['right'].set_color('#4E83A3')
    #
    # # change x y ticks color
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')
    #
    # # change x y label color
    # ax.xaxis.label.set_color('white')
    # ax.yaxis.label.set_color('white')
    #
    # # change x y label line style
    # # ax.spines['bottom'].set_linestyle('--')
    # # ax.spines['left'].set_linestyle('--')
    #
    # control ticks spacing make it dynamic
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    # add canvas to the plotFrame
    canvas = FigureCanvasTkAgg(fig, master=plotFrame)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()


