import logging
import random

import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)  # Set logging level

# User inputs
# max_overall_drawdown = float(input("Enter max overall drawdown (e.g., 0.10 for 10%): "))
# profit_target = float(input("Enter profit target (e.g., 0.10 for 10%): "))
# risk_per_trade = float(input("Enter risk per trade (e.g., 0.01 for 1%): "))
#
# win_rate = float(input("Enter win rate (e.g., 0.60 for 60%): "))
# reward_to_risk = float(input("Enter reward to risk ratio (e.g., 2.0 for 2:1): "))
# trades_to_pass = int(input("Enter number of trades needed to pass: "))

# Inputs
initial_balance = 50000
# max_daily_drawdown = 0.03
max_overall_drawdown = 0.06
profit_target = 0.06
risk_per_trade = 0.01
win_rate = 0.55
reward_to_risk = 2.0  # 2:1 RR
trades_to_pass = 10


# function to control risk dynamiclly
def risk_reducer(virtual_balance, current_risk):
    increase_check = initial_balance * 1.03
    decrease_check = initial_balance * 0.98
    if virtual_balance >= increase_check:
        increase_risk = 0.02
        return increase_risk
    elif virtual_balance <= decrease_check:
        decrease_risk = 0.005
        return decrease_risk
    else:
        return current_risk


def max_dd_sim(simulation_data, initial_balance):
    peak = initial_balance
    sim_drawdown = 0
    for balance in simulation_data["balances"]:
        if balance > peak:
            peak = balance  # Update peak if a new high is reached
        # Calculate the current drawdown based on the highest peak so far
        current_drawdown = (peak - balance) / peak  # Drawdown from peak
        # Track the worst drawdown
        sim_drawdown = max(sim_drawdown, current_drawdown)
    return sim_drawdown


# models simulations
def simulate_trades():
    try:
        num_simulations = 10
        results = []
        for sim in range(num_simulations):
            logging.info(f"Starting simulation {sim + 1}")
            virtual_balance = initial_balance
            current_risk = risk_per_trade
            sim_drawdown = 0
            simulation_data = {
                "balances": [virtual_balance],
                "risks": [current_risk],
                "drawdowns": [0],
            }

            for trade in range(trades_to_pass):
                current_risk = risk_reducer(virtual_balance, current_risk)
                # Calculate absolute risk amount
                risk_amount = current_risk * initial_balance
                # Simulate trade outcome
                if random.random() < win_rate:
                    virtual_balance += reward_to_risk * risk_amount
                else:
                    virtual_balance -= risk_amount

                # Track drawdowns
                sim_drawdown = max_dd_sim(simulation_data, initial_balance)

                # Store simulation data
                simulation_data["balances"].append(virtual_balance)
                logging.info(f"Trade {trade + 1} - Balance: {virtual_balance}")

                # Check for violations
                if sim_drawdown >= max_overall_drawdown * initial_balance:
                    logging.info(f"balance reached max dd at trade: {trade + 1}")
                    # break
                elif virtual_balance >= initial_balance * (1 + profit_target):
                    logging.info(f"balance reached target at trade: {trade +1}")
                    # break

                simulation_data["risks"].append(current_risk)
                simulation_data["drawdowns"].append(sim_drawdown)
                # logging.info(f"Ending trade {trade + 1}")

            results.append(simulation_data)
            logging.info(f"Ending simulation {sim + 1}")

            # worst dd value
            worst_dd_all_sims = max(simulation_data["drawdowns"])

            # loggings
            logging.info(f"[Sim {sim}] final balance: {virtual_balance}")
            logging.info(f"[Sim {sim}] current_risk: {current_risk * 100:.2f}%")
            logging.info(f"[Sim {sim}] max_drawdown: {sim_drawdown * 100:.2f}%")

            # logging.info(f"[sim {sim+1}] drawdowns: {simulation_data['drawdowns']}")
            logging.info(f"[all sims] worst drawdown: {worst_dd_all_sims * 100:.2f}%")

        return results

    except Exception as e:
        logging.error(f"An error occurred: {e}")


logging.basicConfig(level=logging.INFO)  # Set logging level


def plotting(results):
    logging.info("Plotting the graph")
    plt.style.use("dark_background")
    # Create a figure and axis
    plt.figure(figsize=(8, 6))
    ax = plt.gca()  # Get the current axis
    # Set title and labels
    ax.set_title(
        "Risk Model Performance", color="grey", fontsize=20, loc="center", pad=15
    )
    ax.set_xlabel("Trade Number", color="grey", fontsize=12)
    ax.set_ylabel("Balance", color="grey", fontsize=12)

    # plot balances
    overall_max_dd = 0
    for sim, data in enumerate(results):
        # ax.plot(data["balances"], label=f"Sim {sim + 1}")
        ax.plot(data["balances"])
        # Find the worst drawdown for this simulation
        worst_dd_value = max(data["drawdowns"])
        # Update the overall maximum drawdown
        if worst_dd_value > overall_max_dd:
            overall_max_dd = worst_dd_value

    # Add a single legend entry for the overall max drawdown
    # ax.plot(
    #     [], [],  # Empty plot (no data)
    #     color="yellow",
    #     label=f"Overall Max DD: {overall_max_dd * 100:.2f}%",
    # )
    # Add profit target and max drawdown reference lines

    ax.axhline(
        initial_balance * (1 + profit_target),
        color="green",
        linestyle="--",
        label="Profit Target",
    )
    ax.axhline(
        initial_balance * (1 - max_overall_drawdown),
        color="red",
        linestyle="--",
        label="Max Drawdown",
    )
    # Customize spines and ticks
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.tick_params(axis="x", direction="inout", length=6, width=2, colors="grey")
    ax.tick_params(axis="y", direction="inout", length=6, width=2, colors="grey")
    ax.spines["bottom"].set_linewidth(2)
    ax.spines["left"].set_linewidth(2)
    ax.spines["bottom"].set_color("grey")
    ax.spines["left"].set_color("grey")

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
    # Finalize plot
    ax.legend()
    plt.savefig("risk_model_performance.png")  # Save the figure
    plt.show()


results = simulate_trades()
plotting(results)
