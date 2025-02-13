import csv
import logging
import random

import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)  # Set logging level

# User inputs
# max_daily_drawdown = float(input("Enter max daily drawdown (e.g., 0.05 for 5%): "))
# max_overall_drawdown = float(input("Enter max overall drawdown (e.g., 0.10 for 10%): "))
# profit_target = float(input("Enter profit target (e.g., 0.10 for 10%): "))
# risk_per_trade = float(input("Enter risk per trade (e.g., 0.01 for 1%): "))
#
# win_rate = float(input("Enter win rate (e.g., 0.60 for 60%): "))
# reward_to_risk = float(input("Enter reward to risk ratio (e.g., 2.0 for 2:1): "))
# trades_to_pass = int(input("Enter number of trades needed to pass: "))

# Inputs
# max_daily_drawdown = 0.03
max_overall_drawdown = 0.06
profit_target = 0.06
risk_per_trade = 0.01

win_rate = 0.55
reward_to_risk = 2.0  # 2:1 RR
trades_to_pass = 20

initial_balance = 50000


# function to control risk dynamiclly
def risk_reducer(virtual_balance, current_risk):
    increase_check = virtual_balance * 1.03
    decrease_check = virtual_balance * 0.98

    if virtual_balance >= increase_check:
        increase_risk = 0.02
        return increase_risk

    elif virtual_balance <= decrease_check:
        decrease_risk = 0.005
        return decrease_risk

    else:
        return current_risk


# models simulations
def simulate_trades():
    try:
        num_simulations = 10
        results = []
        for sim in range(num_simulations):
            virtual_balance = initial_balance
            current_risk = risk_per_trade
            overall_drawdown = 0
            simulation_data = {
                "balances": [virtual_balance],
                "risks": [current_risk],
                "drawdowns": [0],
            }

            for trade in range(trades_to_pass):
                # current_risk = risk_per_trade  # fixed risk at the momment
                current_risk = risk_reducer(virtual_balance, current_risk)

                # Calculate absolute risk amount
                risk_amount = current_risk * virtual_balance

                # Simulate trade outcome
                if random.random() < win_rate:
                    virtual_balance += reward_to_risk * risk_amount
                else:
                    virtual_balance -= risk_amount

                # Track drawdowns
                overall_drawdown = max(
                    overall_drawdown, initial_balance - virtual_balance
                )

                simulation_data["max_dd_all_sims"] = (
                    max(simulation_data["balances"]) - min(simulation_data["balances"])
                ) / max(simulation_data["balances"])

                # Store simulation data
                simulation_data["balances"].append(virtual_balance)
                logging.info(f"Trade {trade + 1} - Balance: {virtual_balance}")

                # Check for violations
                if overall_drawdown >= max_overall_drawdown * initial_balance:
                    logging.info("max dd reached!")
                    # break
                if virtual_balance >= initial_balance * (1 + profit_target):
                    logging.info("target reached!")
                    # break

                simulation_data["risks"].append(current_risk)
                simulation_data["drawdowns"].append(overall_drawdown / initial_balance)

                logging.info(f"Ending trade {trade + 1}")

            results.append(simulation_data)
            logging.info(f"Ending simulation {sim + 1}")

            logging.info(f"[Simulation] Current virtual_balance: {virtual_balance}")
            logging.info(
                f"[Simulation] overall_drawdown: {overall_drawdown / initial_balance * 100:.2f}%"
            )
            logging.info(f"[Simulation] current_risk: {current_risk * 100:.2f}%")

        return results

    except Exception as e:
        logging.error(f"An error occurred: {e}")


# data charts
def plotting(results):
    plt.style.use("dark_background")
    # plt.figure(figsize=(10, 8))

    for sim, data in enumerate(results):
        # Plot Account Balance
        plt.subplot(1, 1, 1)
        # plt.plot(data["balances"], label=f"Sim {sim+1}")
        plt.plot(data["balances"])
        plt.axhline(
            initial_balance * (1 + profit_target),
            color="green",
            linestyle="--",
            label="Profit Target",
        )
        plt.axhline(
            initial_balance * (1 - max_overall_drawdown),
            color="red",
            linestyle="--",
            label="Max Drawdown",
        )

        # Annotate max drawdown point
        max_dd_value = data["max_dd_all_sims"]

        plt.xlabel("Trade")
        plt.ylabel("Account Balance")
        plt.title("Account Balance Over Time")

        # Plot Drawdowns
        # plt.subplot(1, 2, 2)
        # plt.plot(data["drawdowns"], label=f"Sim {sim+1}")
        # plt.xlabel("Trade")
        # plt.ylabel("Drawdown (%)")
        # plt.title("Drawdown Over Time")
        # plt.legend(loc="upper left")

        # Plot Risk Levels
        # plt.subplot(1, 2, 2)
        # plt.plot(data["risks"], label=f"Sim {sim+1}")
        # # plt.scatter(range(len(data["risks"])), data["risks"], label=f"Sim {sim+1}")
        # plt.xlabel("Trade")
        # plt.ylabel("Risk Level")
        # plt.title("Risk Level Over Time")
        # plt.legend(loc="upper left")

    # plt.tight_layout()
    plt.show()


results = simulate_trades()
plotting(results)
