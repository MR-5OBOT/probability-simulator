import random

# Get user inputs
initial_balance = float(5000)
risk_percent = float(1)
rr_ratio = float(2)
num_trades = int(100)

# initializations
balance = initial_balance
balance_history = [initial_balance]

balance += 1
print(balance)
print(balance_history)

# Calculate Max Drawdown from Balance History
max_drawdown = 0
peak_balance = balance_history[0]
print(peak_balance)

for bal in balance_history:
    if bal > peak_balance:
        peak_balance = bal
    drawdown = (peak_balance - bal) / peak_balance
    max_drawdown = max(max_drawdown, drawdown)

# Convert to percentage
max_drawdown *= 100


