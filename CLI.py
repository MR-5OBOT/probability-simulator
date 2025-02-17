import logging
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def probability_simulator(balanceEntry, winrateEntry, riskEntry, rrEntry, consecutive_LossesEntry, nTrades_entry):
    try:
        logging.info("Starting simulation")
        # Get user inputs
        initial_balance = float(balanceEntry)
        winrate = float(winrateEntry)
        risk_percent = float(riskEntry)
        rr_ratio = float(rrEntry)
        consecutive_L_treshold = consecutive_LossesEntry
        num_trades = int(nTrades_entry)

        # Validate inputs
        if initial_balance <= 0 or risk_percent <= 0 or rr_ratio <= 0 or num_trades <= 0 or winrate <= 0:
            # result_label.configure(text="Error: All inputs must be positive numbers.")
            messagebox.showerror(message="Error: All inputs must be positive numbers.")
            # debuging
            logging.error("Error: All inputs must be positive numbers.")
            return

        # Initialize balance history
        global balance_history
        balance_history = [initial_balance]

        # Initialize variables
        balance = initial_balance
        consecutive_losses = 0
        max_consecutive_losses = 0
        wins = 0
        losses = 0
        avg_win = 0
        avg_loss = 0
        wins_profits = 0
        losses_profits = 0

        reduced_risk_active = False  # Track if risk reduction is active

        for trade in range(num_trades):
            if reduced_risk_active:
                risk_amount = balance * (risk_percent / 100) / 2
            else:
                risk_amount = balance * (risk_percent / 100)

            # Simulate trade outcome
            if random.random() <= winrate:
                profit = risk_amount * rr_ratio
                balance += profit
                wins += 1
                wins_profits += profit
                consecutive_losses = 0
                reduced_risk_active = False  # Reset risk reduction on a win
                # debuging
                # logging.info("wining trade")
            else:
                loss = risk_amount
                balance -= loss
                losses += 1
                losses_profits += loss
                consecutive_losses += 1
                max_consecutive_losses = max(max_consecutive_losses, consecutive_losses)
                # debuging
                # logging.info("lossing trade")

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
            if not balance_history:
                logging.info("Error: Simulation failed. No balance data to plot.")
                return

        # Calculate Max Drawdown from Balance History
        max_drawdown = 0
        peak_balance = balance_history[0]

        for bal in balance_history:
            if bal > peak_balance:
                peak_balance = bal
            drawdown = (peak_balance - bal) / peak_balance
            max_drawdown = max(max_drawdown, drawdown)
        max_drawdown *= 100  # Convert to percentage

        # Calculate total return
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Expected Value (EV) formula
        actual_winrate = wins / num_trades if wins > 0 else 0
        # Calculate average win and loss
        if wins + losses == num_trades:
            avg_win = wins_profits / wins if wins > 0 else 0
            avg_loss = losses_profits / losses if losses > 0 else 0

        expected_value = (actual_winrate * avg_win) - ((1 - actual_winrate) * avg_loss)

        logging.info(
            f"Final Balance: ${balance:.2f}\n"
            f"Total Return: {total_return:.2f}%\n"
            f"Max Drawdown: {max_drawdown:.2f}%\n"
            f"Consecutive Losses: {max_consecutive_losses:.0f}\n"
            f"Average Win: ${avg_win:.2f}\n"
            f"Average Loss: {avg_loss:.2f}\n"
            f"Expected Value: ${expected_value:.2f}"
        )

        return balance_history

    except ValueError:
        messagebox.showerror(message="Error: Please enter valid numbers.")

    # debuging
    logging.info("simulation ended.")



def creat_plot():
    plt.style.use("dark_background")
    fig = Figure(figsize=(9, 6))
    ax = plt.gca()  # Get the current axis
    ax.plot(balance_history, label="balance_history")

    ax.set_title("Simulation Results", color="grey", fontsize=20, loc="center", pad=15)
    ax.grid(color="#161616", linestyle="--", linewidth=0.5, axis="both")
    ax.set_xlabel("Trade Number", color='grey', fontsize=12)
    ax.set_ylabel("Balance", color='grey', fontsize=12)

    # Remove right and top spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    # Change x and y ticks style
    ax.tick_params(axis="x", direction="inout", length=6, width=2)
    ax.tick_params(axis="y", direction="inout", length=6, width=2)

    # Change x and y label line width and color
    ax.spines["bottom"].set_linewidth(2)
    ax.spines["left"].set_linewidth(2)
    ax.spines["bottom"].set_color("grey")
    ax.spines["left"].set_color("grey")
    # Change x and y ticks color
    ax.tick_params(axis="x", colors="grey")
    ax.tick_params(axis="y", colors="grey")
    # Add a watermark
    ax.text(
        0.5,
        0.5,  # X and Y position (relative, in axes coordinates)
        "@MR_5OBOT",  # Watermark text
        fontsize=30,  # Font size
        color="gray",  # Text color
        alpha=0.12,  # Transparency (0.0 to 1.0)
        ha="center",  # Horizontal alignment
        va="center",  # Vertical alignment
        rotation=10,  # Rotate text
        transform=ax.transAxes,  # Transform relative to the axes (0 to 1 range)
    )
    logging.info("plotting the graph")
    plt.savefig("simulation_results.png")
    logging.info("Saving the plot to a file")
    plt.show()

    return fig


if __name__ == "__main__":
    # balanceEntry = input("initial balance: ")
    # winrateEntry = input("winrate: ")
    # riskEntry = input("Risk percentage: ")
    # rrEntry = input("R/R: ")
    # consecutive_LossesEntry = (input("consecutive_Losses treshold: "),)
    # nTrades_entry = input("total trades: ")
    balanceEntry = 50000
    winrateEntry = 0.55
    riskEntry = 0.01
    rrEntry = 2
    consecutive_LossesEntry = 1
    nTrades_entry = 100
    probability_simulator(balanceEntry, winrateEntry, riskEntry, rrEntry, consecutive_LossesEntry, nTrades_entry)
    creat_plot()
