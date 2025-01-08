import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import random


# Main GUI setup
app = tk.Tk()
style = ttk.Style(app) # Create a style object
style.theme_use("clam")

# app.tk.call('source', 'forest-dark.tcl') # Load custom theme
# style.theme_use('forest-dark') # Set custom theme

app.title("Traders Toolbox")
app.geometry(f"{int(app.winfo_screenwidth() * 0.9)}x{int(app.winfo_screenheight() * 0.9)}") # Set window size dynamically
# app.geometry("1200x650")
app.resizable(False, False)

# create a notebook
notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill="both")


# Create individual tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(tab1, text="Probability Simulator")
notebook.add(tab2, text="tab2")

# ----------------- dynamic frame sizes -----------------
def dynamic_frame1_tab1():
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    # Frame size calculated based on the screen size
    frame_width = int(screen_width * 1)
    frame_height = int(screen_height * 0.08)
    return frame_width, frame_height

def dynamic_frame2_tab1():
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    # Frame size calculated based on the screen size
    frame_width = int(screen_width * 0.3)
    frame_height = int(screen_height * 0.9)
    return frame_width, frame_height

def dynamic_frame3_tab1():
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    # Frame size calculated based on the screen size
    frame_width = int(screen_width * 0.6)
    frame_height = int(screen_height * 0.95)
    return frame_width, frame_height

# ----------------- Tab1 Functions -----------------
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
        

# plot function
def ploting():
    # Plot the balance history
    plt.style.use("ggplot")
    # plt.figure(figsize=(10, 6))
    plt.plot(balance_history)
    plt.title("Trading Simulation Results")
    plt.xlabel("Number of Trades")
    plt.ylabel("Balance ($)")
    plt.grid(True)
    # plt.savefig("Simulation.png")
    plt.show()

# ----------------- Tab1 Widgets -----------------

# # Create a frame for the title
# frame1_tab1 = ttk.Frame(tab1, width=dynamic_frame1_tab1()[0], height=dynamic_frame1_tab1()[1], borderwidth=8, relief="raised")
# frame1_tab1.pack(pady=5, padx=5, side="top", expand=True, fill="both")
# ttk.Label(frame1_tab1, text="Probability Simulator (random 50/50)", font=("Arial", 24)).pack()
#
# # Create a frame for the inputs
# frame2_tab1 = ttk.Frame(tab1, width=dynamic_frame2_tab1()[0], height=dynamic_frame2_tab1()[1], borderwidth=2, relief="raised")
# frame2_tab1.pack(pady=5, padx=5, side="left", expand=True, fill="x")
#
# # Create a unique style for a specific frame (e.g., "Custom.TFrame")
# # style.configure("inputs.TFrame", background="white")
#
# ttk.Label(frame2_tab1, text="Simulation inputs", font=("Arial", 19)).pack(pady=30)
#
# ttk.Label(frame2_tab1, text="Initial Balance:").pack(pady=5)
# balance_entry = ttk.Entry(frame2_tab1)
# balance_entry.pack(pady=5)
#
# ttk.Label(frame2_tab1, text="Risk %:").pack(pady=5)
# risk_entry = ttk.Entry(frame2_tab1)
# risk_entry.pack(pady=5)
#
# ttk.Label(frame2_tab1, text="R/R Ratio:").pack(pady=5)
# rr_entry = ttk.Entry(frame2_tab1)
# rr_entry.pack(pady=5)
#
# ttk.Label(frame2_tab1, text="Number of Trades:").pack(pady=5)
# trades_entry = ttk.Entry(frame2_tab1)
# trades_entry.pack(pady=5)
#
# sim_button = ttk.Button(frame2_tab1, text="Run Simulation", command=probability_simulator)
# sim_button.pack(pady=15)
#
# sim_label = ttk.Label(frame2_tab1, text="", font=("Arial", 10))
# sim_label.pack()
#
# save_button = ttk.Button(frame2_tab1, text="Save Results", command=ploting, default="disabled", padding=5, width=10)
# save_button.pack(pady=15)
#
# # Create a frame for plotting
# frame3_tab1 = ttk.Frame(tab1, width=dynamic_frame3_tab1()[0], height=dynamic_frame3_tab1()[1], borderwidth=2, style="plots.TFrame")
# frame3_tab1.pack(pady=5, padx=5, side="right", expand=True, fill="both")
#
# # Create a unique style for a specific frame (e.g., "Custom.TFrame")
# style.configure("plots.TFrame", background="grey")
#
#




app.mainloop() # Run App
