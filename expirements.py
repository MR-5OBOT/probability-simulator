# from tkinter import messagebox
import logging
import tkinter as tk
from tkinter import messagebox, ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# custom module
from resources.custom_func.expirements_funcs import (
    get_balance_history,
    probability_simulator,
)


# ------------ plotting -------------#
def start_simulation():
    probability_simulator(
        balanceEntry, winrateEntry, riskEntry, rrEntry, consecutive_LossesEntry, nTrades_entry, result_label
    )


def creat_plot():
    plt.style.use("dark_background")
    fig = Figure(figsize=(9, 6))
    ax = fig.add_subplot()
    data = get_balance_history()
    ax.plot(data, label="balance_history")

    ax.set_title("Simulation Results", color="grey", fontsize=20, loc="center", pad=15)
    ax.grid(color="#161616", linestyle="--", linewidth=0.5, axis="both")

    # ax.set_xlabel("Trade Number", color='grey', fontsize=12)
    # ax.set_ylabel("Balance", color='grey', fontsize=12)

    # Remove right and top spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Change x and y ticks style
    ax.tick_params(axis="x", direction="inout", length=6, width=2)
    ax.tick_params(axis="y", direction="inout", length=6, width=2)

    # Change x and y label line width and color
    ax.spines["bottom"].set_linewidth(2)
    ax.spines["left"].set_linewidth(2)
    ax.spines["bottom"].set_color("grey")
    ax.spines["left"].set_color("grey")

    # Change x and y ticks color
    ax.tick_params(axis="x", colors="grey")
    ax.tick_params(axis="y", colors="grey")

    # Adding annotations for max drawdown
    # max_dd = get_max_dd()
    # balance_history = get_balance_history()
    # ax.scatter(
    #     max_dd,
    #     balance_history[(max_dd)],
    #     color="red",
    #     label="Max Drawdown Point",
    #     zorder=10,
    # )


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
    logging.info("plotting the graph")

    return fig


def plot_to_canvas():
    # Add canvas to the plotFrame
    clear_plot()
    start_simulation()
    fig = creat_plot()
    canvas = FigureCanvasTkAgg(fig, master=plotFrame)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()
    logging.info("Plotting the graph to the canvas")


def save_plot():
    try:
        fig = creat_plot()
        fig.savefig("simulation_results.png")
        logging.info("Saving the plot to a file")
        messagebox.showinfo("Save", "The plot has been saved as 'simulation_results.png'")
    except Exception:
        messagebox.showerror("Error", "No data to save. Please run the simulation first.")


def clear_plot():
    # Clear the previous plot
    for widget in plotFrame.winfo_children():
        widget.destroy()


# the function that will be triggered when the checkbox is toggled
def risk_reducer_func():
    if check_var.get() == 1:  # If checked
        consecutive_LossesEntry.config(state="normal")  # Enable entry
    else:  # If unchecked
        consecutive_LossesEntry.delete(0)
        consecutive_LossesEntry.config(state="disabled")  # Disable entry


# ------- GUI ------#
app = tk.Tk()
style = ttk.Style(app)  # Create a style object
app.tk.call("source", "./resources/Forest-ttk-theme/forest-dark.tcl")  # Load custom theme
style.theme_use("forest-dark")  # Set custom theme

app.title("Probability Simulator")
app.geometry("1200x650")  # Set window size dynamically

app_frame = ttk.Frame(app, padding=(5, 5))
app_frame.pack(fill="both", expand=True)

# ----- Tab1 input frame -----#
inputsLabel = ttk.LabelFrame(app_frame, text="Simulation inputs", padding=(15, 15))
inputsLabel.pack(side="left", padx=5)

balanceEntry = ttk.Spinbox(inputsLabel, from_=1000, to=1000000, increment=100)
balanceEntry.insert(0, "balance")
balanceEntry.bind("<FocusIn>", lambda _: balanceEntry.delete("0", "end"))  # Clear the entry when clicked
balanceEntry.grid(column=0, row=0, sticky="ew", pady=5)

winrateEntry = ttk.Spinbox(inputsLabel, from_=0, to=1, increment=0.1)
winrateEntry.insert(0, "winrate (decimal)")
winrateEntry.bind("<FocusIn>", lambda _: winrateEntry.delete("0", "end"))  # Clear the entry when clicked
winrateEntry.grid(column=0, row=1, sticky="ew", pady=5)

riskEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.1)
riskEntry.insert(0, "risk percentage")
riskEntry.bind("<FocusIn>", lambda _: riskEntry.delete("0", "end"))
riskEntry.grid(column=0, row=2, sticky="ew", pady=5)

rrEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.5)
rrEntry.insert(0, "risk reward")
rrEntry.bind("<FocusIn>", lambda _: rrEntry.delete("0", "end"))
rrEntry.grid(column=0, row=3, sticky="ew", pady=5)

nTrades_entry = ttk.Spinbox(inputsLabel, from_=0, to=1000, increment=1)
nTrades_entry.insert(0, "total trades")
nTrades_entry.bind("<FocusIn>", lambda _: nTrades_entry.delete("0", "end"))
nTrades_entry.grid(column=0, row=4, sticky="ew", pady=5)

consecutive_LossesEntry = ttk.Spinbox(inputsLabel, from_=0, to=1000, increment=1)
consecutive_LossesEntry.insert(0, "losses treshold")
consecutive_LossesEntry.bind("<FocusIn>", lambda _: consecutive_LossesEntry.delete("0", "end"))
consecutive_LossesEntry.grid(column=0, row=5, sticky="ew", pady=5)
consecutive_LossesEntry.config(state="disabled")

# Variable for Checkbutton state
check_var = tk.IntVar()
# Create Checkbutton and place it inside the LabelFrame
risk_reducerbutton = ttk.Checkbutton(inputsLabel, text="Risk Reducer", variable=check_var, command=risk_reducer_func)
risk_reducerbutton.grid(column=0, row=7, pady=5)

calculateButton = ttk.Button(inputsLabel, text="Run Simulation", command=plot_to_canvas)
calculateButton.grid(column=0, row=8, sticky="ew", pady=5)

separator = ttk.Separator(inputsLabel, orient="horizontal")
separator.grid(column=0, row=9, sticky="nsew", pady=5)

result_frame = ttk.LabelFrame(inputsLabel, text="Results")
result_frame.grid(column=0, row=10, sticky="nsew")
result_label = ttk.Label(result_frame, text="", anchor="center")
result_label.pack(expand=True, fill="both", padx=5, pady=5)

save_pic = ttk.Button(inputsLabel, text="Save Results", command=save_plot)
save_pic.grid(column=0, row=11, pady=5, padx=5)

# ----- tab1 plot frame -----#
plotFrame = ttk.LabelFrame(app_frame, text="Plot Graph", padding=(15, 15))
plotFrame.pack(expand=True, fill="both", side="right", pady=10, padx=10)

# Configure grid weights for responsiveness
app_frame.grid_rowconfigure(0, weight=1)
app_frame.grid_columnconfigure(1, weight=1)


# Ensure that we exit the mainloop when the window is closed
def on_closing():
    app.quit()


# Set up the closing protocol
app.protocol("WM_DELETE_WINDOW", on_closing)

# run the app
app.mainloop()
