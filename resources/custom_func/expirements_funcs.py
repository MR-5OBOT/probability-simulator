# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
from tkinter import messagebox
# import logging
import random


class Simulation:
    def __init__(self, initial_balance, winrate, risk_percent, rr_ratio, consecutive_L_treshold, num_trades):
        # Set user inputs
        self.initial_balance = initial_balance
        self.winrate = winrate
        self.risk_percent = risk_percent
        self.rr_ratio = rr_ratio
        self.consecutive_L_treshold = consecutive_L_treshold
        self.num_trades = num_trades

        # Initialize variables
        self.balance = initial_balance
        self.balance_history = [initial_balance]
        self.consecutive_losses = 0
        self.max_consecutive_losses = 0
        self.wins = 0
        self.losses = 0
        self.avg_win = 0
        self.avg_loss = 0
        self.wins_profits = 0
        self.losses_profits = 0
        self.reduced_risk_active = False  # Track if risk reduction is active

    def simulate_trade(self):
        for trade in range(self.num_trades):
            if self.reduced_risk_active:
                risk_amount = self.balance * (self.risk_percent / 100) / 2
            else:
                risk_amount = self.balance * (self.risk_percent / 100)

            # Simulate trade outcome
            if random.random() <= self.winrate:
                profit = risk_amount * self.rr_ratio
                self.balance += profit
                self.wins += 1
                self.wins_profits += profit
                self.consecutive_losses = 0
                self.reduced_risk_active = False  # Reset risk reduction on a win
            else:
                loss = risk_amount
                self.balance -= loss
                self.losses += 1
                self.losses_profits += loss
                self.consecutive_losses += 1
                self.max_consecutive_losses = max(self.max_consecutive_losses, self.consecutive_losses)

            # Check for consecutive losses threshold
            if self.consecutive_L_treshold:  # Only reduce risk if the input is not empty
                try:
                    threshold = int(self.consecutive_L_treshold)
                    if self.consecutive_losses >= threshold:
                        self.reduced_risk_active = True  # Activate risk reduction
                except ValueError:
                    pass  # If conversion fails, don't adjust risk

            # Append the current balance to history
            self.balance_history.append(self.balance)

        return self.balance_history

    def calculate_metrics(self):
        # Calculate Max Drawdown from Balance History
        max_drawdown = 0
        peak_balance = self.balance_history[0]

        for bal in self.balance_history:
            if bal > peak_balance:
                peak_balance = bal
            drawdown = (peak_balance - bal) / peak_balance
            max_drawdown = max(max_drawdown, drawdown)
        max_drawdown *= 100

        # Calculate total return
        total_return = ((self.balance - self.initial_balance) / self.initial_balance) * 100

        # Expected Value (EV) formula
        actual_winrate = self.wins / self.num_trades if self.wins > 0 else 0

        if self.wins + self.losses == self.num_trades:
            self.avg_win = self.wins_profits / self.wins if self.wins > 0 else 0
            self.avg_loss = self.losses_profits / self.losses if self.losses > 0 else 0

        expected_value = (actual_winrate * self.avg_win) - ((1 - actual_winrate) * self.avg_loss)

        return total_return, max_drawdown, self.max_consecutive_losses, self.avg_win, self.avg_loss, expected_value

    # display results in a messagebox
    def display_results(self):
        total_return, max_drawdown, max_consecutive_losses, avg_win, avg_loss, expected_value = self.calculate_metrics()

        messagebox.showinfo(
            message=(
                f"Final Balance: ${self.balance:.2f}\n"
                f"Total Return: {total_return:.2f}%\n"
                f"Max Drawdown: {max_drawdown:.2f}%\n"
                f"Consecutive Losses: {max_consecutive_losses:.0f}\n"
                f"Average Win: ${avg_win:.2f}\n"
                f"Average Loss: {avg_loss:.2f}\n"
                f"Expected Value: ${expected_value:.2f}"
            )
        )

        # display results in a label
        return (
            f"Final Balance: ${self.balance:.2f}\n"
            f"Total Return: {total_return:.2f}%\n"
            f"Max Drawdown: {max_drawdown:.2f}%\n"
            f"Consecutive Losses: {max_consecutive_losses:.0f}\n"
            f"Average Win: ${avg_win:.2f}\n"
            f"Average Loss: {avg_loss:.2f}\n"
            f"Expected Value: ${expected_value:.2f}"
        )


