import random

initial_balance = int(5000)
balance = initial_balance
balance_history = [initial_balance]
rr_ratio = 1
risk_percentage = 1
winrate = 0.5
wins = 0
consecutive_losses = 0
max_consecutive_losses = 0
consecutive_L_treshold = 1

# Loop through the number of trades
for trade in range(10):
    risk_amount = balance * (risk_percentage / 100)

    # Reduce risk after x consecutive losses
    if consecutive_losses >= consecutive_L_treshold:
        risk_amount /= 2  # Reduce risk by 50% (adjust this factor as needed)


    # Determine trade outcome
    if random.random() <= winrate:
        balance += (risk_amount * rr_ratio)
        wins += 1
        consecutive_losses = 0
    else:
        balance -= risk_amount
        consecutive_losses += 1

    # Track maximum consecutive losses
    max_consecutive_losses = max(max_consecutive_losses, consecutive_losses)

    balance_history.append(int(balance))

print("Final Balance History:", balance_history)
print("Maximum Consecutive Losses:", max_consecutive_losses)
