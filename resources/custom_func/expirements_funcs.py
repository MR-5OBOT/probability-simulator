# import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
from tkinter import messagebox
# from tkinter import filedialog


#------- simulation based on risk model --------#
def probability_simulator(balanceEntry, winrateEntry, riskEntry, rrEntry, consecutive_LossesEntry, nTrades_entry, result_label):
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

        if not (0 <= winrate <= 1):
            result_label.configure(text="Error: Win rate must be between 0 and 1.")
            messagebox.showinfo(message="Error: Win rate must be between 0 and 1.")
            return

        # Initialize variables
        balance = initial_balance
        balance_history = [initial_balance]
        consecutive_losses = 0
        max_consecutive_losses = 0
        wins = 0
        losses = 0
        wins_profits = 0
        losses_profits = 0
        reduced_risk_active = False  # Track if risk reduction is active

        for _ in range(num_trades):
            # Calculate the risk amount
            if reduced_risk_active:
                risk_amount = balance * (risk_percent / 100) / 2  # Reduced risk
            else:
                risk_amount = balance * (risk_percent / 100)  # Normal risk

            # Simulate trade outcome
            if random.random() <= winrate:
                balance += (risk_amount * rr_ratio)
                wins += 1
                wins_profits += (risk_amount * rr_ratio)
                consecutive_losses = 0
                reduced_risk_active = False  # Reset risk reduction on a win
            else:
                balance -= risk_amount
                losses += 1
                losses_profits += risk_amount
                consecutive_losses += 1
                max_consecutive_losses = max(max_consecutive_losses, consecutive_losses)

            # Check for consecutive losses threshold
            if consecutive_L_treshold:  # Only reduce risk if the input is not empty
                try:
                    threshold = int(consecutive_L_treshold)
                    if consecutive_losses >= threshold:
                        reduced_risk_active = True  # Activate risk reduction
                except ValueError:
                    # print("no consecutive losses threshold is active!")
                    pass  # If conversion fails, don't adjust risk

            # Append the current balance to history
            balance = round(balance, 2) # formate balance to 2 dicimal
            balance_history.append(balance)

        # Calculate Max Drawdown from Balance History
        max_drawdown = 0
        peak_balance = balance_history[0]

        for bal in balance_history:
            if bal > peak_balance:
                peak_balance = bal
            drawdown = (peak_balance - bal) / peak_balance
            max_drawdown = max(max_drawdown, drawdown)
        max_drawdown *= 100 # Convert to percentage

        total_return = ((balance - initial_balance) / initial_balance) * 100 # total return formula

        # Expected Value (EV) formula:  EV=(Win Rate×Average Win)−(Loss Rate×Average Loss)
        actual_winrate = wins / num_trades
        avg_win = wins_profits / wins if wins > 0 else 0 # avoid division by zero
        avg_loss = losses_profits / losses if losses > 0 else 0 # avoid division by zero
        expected_value = (actual_winrate * avg_win) - ((1 - actual_winrate) * avg_loss)

        # Display results in a messagebox
        result_label.configure(
                text=f"Final Balance: ${balance:.2f}\n"
                f"Total Return: {total_return:.2f}%\n"
                f"Max Drawdown: {max_drawdown:.2f}%\n"
                f"Consecutive Losses: {max_consecutive_losses}\n"
                f"Expected Value: ${expected_value:.2f}"
        )
        messagebox.showinfo(
                message=f"Final Balance: ${balance:.2f}\n"
                f"Total Return: {total_return:.2f}%\n"
                f"Max Drawdown: {max_drawdown:.2f}%\n"
                f"Consecutive Losses: {max_consecutive_losses}\n"
                f"Expected Value (EV): ${expected_value:.2f}"
        )
        # return balance history fot update plot func()
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
    ax.plot(balance_history, label="Balance History")  # Add a label for the plot

    # Customize the plot
    ax.set_title("Simulation Results", color='grey', fontsize=20, loc='center', pad=15)
    ax.grid(color='#161616', linestyle='--', linewidth=0.5, axis="both")

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

    # Remove right and top lines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Change ticks and spines styling
    ax.tick_params(axis='x', direction='inout', length=6, width=2, colors='grey')
    ax.tick_params(axis='y', direction='inout', length=6, width=2, colors='grey')
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['bottom'].set_color('grey')
    ax.spines['left'].set_linewidth(2)
    ax.spines['left'].set_color('grey')

    # Add canvas to the plotFrame
    canvas = FigureCanvasTkAgg(fig, master=plotFrame)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()

    # Save the plot if needed
    plt.savefig("Simulation")

