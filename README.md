# Probability Simulator

This application helps traders simulate probability-based outcomes to enhance their trading strategies.

![image](https://github.com/user-attachments/assets/bcf145f6-e379-4ffd-a340-ef53739623fd)

## How the Simulations Work

The app allows users to simulate two types of probability models to help traders assess different strategies based on historical data and user inputs.

### Inputs for Simulations

- **Initial Investment**: The amount of money to start the simulation with.
- **Risk-Reward Ratio (RRR)**: The ratio of the expected reward to the risk taken on each trade.
- **Win Rate**: The probability of a trade being successful.
- **Number of Trades**: The total number of trades to simulate.
- **Risk per Trade**: The percentage of the current balance to risk on each trade.

### What to Expect

- **Realistic Scenarios**: Both simulations aim to present realistic trading scenarios based on your inputs.
- **Performace Graphs**: Visualizations of the performance over time, showing how different factors like win rate and risk-reward ratio can influence the long-term results.
- **Data Export (Coming Soon)**: Future updates will include the ability to save your simulation results to a file for further analysis.

## How to Use

1. Download the executable from the [Releases page](https://github.com/MR-5OBOT/proability-simulator/releases).
2. Run the executable to start the application.

## Features

- **Simulate Probability Models**: Simulate different probability scenarios for trading strategies.
- **Graphs**: View simulation results in graphical formats (charts and graphs).
- **Multiple Simulations**: Two types of simulations are available for various trading strategies.
- **Save Results**: Save the results of your simulations for later use.

### **Todos:**

- [x] Make the UI for the app
- [x] Make 2 tabs for the 2 types of simulations
- [x] Plot the results of the simulations in a graph inside the app
- [x] Fix the position of the widgets in the app
- [ ] Add a feature to save the results of the simulations to a file
- [ ] make a windows .EXE version

## Dependencies

To run this app, you need the following Python packages:

- `Python 3.x`
- `Tkinter` (for GUI)
- `matplotlib` (for graph plotting)
- `numpy` (for mathematical operations)
- `pandas` (for data manipulation)

You can install the necessary packages with the following command:

```bash
pip install -r requirements.txt
```
