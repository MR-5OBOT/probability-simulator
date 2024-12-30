import matplotlib.pyplot as plt

# Create a simple plot
trade_n = ["trade 1", "trade 2", "trade 3", "trade 4", "trade 5"]
trade_pl = [10, 20, 25, 30, 35]

plt.plot(trade_n, trade_pl)
plt.title("Trading Simulation Results")
plt.xlabel("Number of Trades")
plt.ylabel("Balance ($)")


# Save the plot as a PNG image
plt.savefig("Simulation.png")

# Optionally, display the plot
plt.show()
