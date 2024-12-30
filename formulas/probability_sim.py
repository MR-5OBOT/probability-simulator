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


# GUI Setup
app = ctk.CTk()
app.geometry("600x500")
app.title("Trading Simulator")
# app.resizable(False, False)

# Title Label
title_label = ctk.CTkLabel(app, text="Trading Simulator", font=("Arial", 24))
title_label.pack(pady=20)

# Input Fields
balance_label = ctk.CTkLabel(app, text="Initial Balance:")
balance_label.pack()
balance_entry = ctk.CTkEntry(app, placeholder_text="Enter initial balance")
balance_entry.pack(pady=5)

risk_label = ctk.CTkLabel(app, text="Risk Percentage:")
risk_label.pack()
risk_entry = ctk.CTkEntry(app, placeholder_text="Enter risk percentage")
risk_entry.pack(pady=5)

rr_label = ctk.CTkLabel(app, text="Risk-Reward Ratio:")
rr_label.pack()
rr_entry = ctk.CTkEntry(app, placeholder_text="Enter risk-reward ratio")
rr_entry.pack(pady=5)

trades_label = ctk.CTkLabel(app, text="Number of Trades:")
trades_label.pack()
trades_entry = ctk.CTkEntry(app, placeholder_text="Enter number of trades")
trades_entry.pack(pady=5)

# Run Simulation Button
run_button = ctk.CTkButton(app, text="Run Simulation", command=simulate_trading)
run_button.pack(pady=20)

# Result Label
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)
