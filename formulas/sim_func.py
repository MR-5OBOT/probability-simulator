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
 
