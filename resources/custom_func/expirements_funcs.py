import random
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import logging


def probability_simulator(balanceEntry, winrateEntry, riskEntry, rrEntry, consecutive_LossesEntry, nTrades_entry, result_label):
    # for debuging 
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info("Starting simulation")

    try:
        # Get user inputs
        initial_balance = float(balanceEntry.get())
        winrate = float(winrateEntry.get())
        risk_percent = float(riskEntry.get())
        rr_ratio = float(rrEntry.get())
        consecutive_L_treshold = consecutive_LossesEntry.get().strip()  # .strip() to remove extra spaces
        num_trades = int(nTrades_entry.get())

        # Validate inputs
        if initial_balance <= 0 or risk_percent <= 0 or rr_ratio <= 0 or num_trades <= 0 or winrate <= 0:
            result_label.configure(text="Error: All inputs must be positive numbers.")
            messagebox.showinfo(message="Error: All inputs must be positive numbers.")
            # debuging
            logging.error("Error: All inputs must be positive numbers.")
            return


        # Initialize variables
        balance = initial_balance
        balance_history = [initial_balance]
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

            # logging.info("Calculate risk amount.")

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
                        logging.info("Reducing risk")
                except ValueError:
                    pass  # If conversion fails, don't adjust risk
            # debuging
            logging.info("risk reducer is not active!")

            # Append the current balance to history
            balance_history.append(balance)
            if not balance_history:
                result_label.configure(text="Error: Simulation failed. No balance data to plot.")
                return
            #debuging
            # logging.info("new balance added!")

        # Calculate Max Drawdown from Balance History
        max_drawdown = 0
        peak_balance = balance_history[0]

        for bal in balance_history:
            if bal > peak_balance:
                peak_balance = bal
            drawdown = (peak_balance - bal) / peak_balance
            max_drawdown = max(max_drawdown, drawdown)
        max_drawdown *= 100 # Convert to percentage

        # Calculate total return
        total_return = ((balance - initial_balance) / initial_balance) * 100

        # Expected Value (EV) formula
        actual_winrate = wins / num_trades if wins > 0 else 0

        if wins + losses == num_trades:
            avg_win = wins_profits / wins if wins > 0 else 0
            avg_loss = losses_profits / losses if losses > 0 else 0

        expected_value = (actual_winrate * avg_win) - ((1 - actual_winrate) * avg_loss)

        # Display results in a messagebox
        messagebox.showinfo(
                message=(
                f"Final Balance: ${balance:.2f}\n"
                f"Total Return: {total_return:.2f}%\n"
                f"Max Drawdown: {max_drawdown:.2f}%\n"
                f"Consecutive Losses: {max_consecutive_losses:.0f}\n"
                f"Average Win: ${avg_win:.2f}\n"
                f"Average Loss: {avg_loss:.2f}\n"
                f"Expected Value: ${expected_value:.2f}"
                )
        )
        result_label.configure(
                text=(
                f"Final Balance: ${balance:.2f}\n"
                f"Total Return: {total_return:.2f}%\n"
                f"Max Drawdown: {max_drawdown:.2f}%\n"
                f"Consecutive Losses: {max_consecutive_losses:.0f}\n"
                f"Average Win: ${avg_win:.2f}\n"
                f"Average Loss: {avg_loss:.2f}\n"
                f"Expected Value: ${expected_value:.2f}"
                )
        )

        return balance_history

    except ValueError:
        messagebox.showerror(message="Error: Please enter valid numbers.")
        result_label.configure(text="Error: Please enter valid numbers.")

    #debuging
    logging.info("simulation ended.")



