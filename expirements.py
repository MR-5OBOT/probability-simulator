import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import logging
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# custom module
from resources.custom_func.expirements_funcs import Simulation


# Function to run the simulation and display results
def run_simulation():
    try:
        # Get user input values
        initial_balance = float(balanceEntry.get())
        winrate = float(winrateEntry.get())
        risk_percent = float(riskEntry.get())
        rr_ratio = float(rrEntry.get())
        consecutive_l_treshold = consecutive_LossesEntry.get().strip() # for risk reducer
        num_trades = int(nTrades_entry.get())

        # Create Simulation instance
        sim = Simulation(
            initial_balance,
            winrate,
            risk_percent,
            rr_ratio,
            consecutive_l_treshold,
            num_trades,
        )

        # Run simulation
        sim.simulate_trade()

        # Display results
        result_string = sim.display_results()
        result_label.config(text=result_string)  # Update the label with results

        # Plot the results
        plotter = Plotting(sim.balance_history)
        plotter.plot_to_canvas()
        # plotter.save_plot()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")



 # ------------ plotting -------------#
class Plotting:
    def __init__(self, balance_history):
        self.balance_history = balance_history

    def creat_plot(self):
        plt.style.use("dark_background")
        fig = Figure(figsize=(9, 6))
        ax = fig.add_subplot()
        ax.plot(self.balance_history, label="balance_history")

        ax.set_title("Simulation Results", color='grey', fontsize=20, loc='center', pad=15)
        ax.grid(color='#161616', linestyle='--', linewidth=0.5, axis="both")

        # ax.set_xlabel("Trade Number", color='grey', fontsize=12)
        # ax.set_ylabel("Balance", color='grey', fontsize=12)

        # Remove right and top spines
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # Change x and y ticks style
        ax.tick_params(axis='x', direction='inout', length=6, width=2)
        ax.tick_params(axis='y', direction='inout', length=6, width=2)

        # Change x and y label line width and color
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['left'].set_linewidth(2)
        ax.spines['bottom'].set_color('grey')
        ax.spines['left'].set_color('grey')

        # Change x and y ticks color
        ax.tick_params(axis='x', colors='grey')
        ax.tick_params(axis='y', colors='grey')

        # Add a watermark
        ax.text(
            0.5, 0.5,               # X and Y position (relative, in axes coordinates)
            "@MR_5OBOT",             # Watermark text
            fontsize=30,            # Font size
            color='gray',           # Text color
            alpha=0.12,             # Transparency (0.0 to 1.0)
            ha='center',            # Horizontal alignment
            va='center',            # Vertical alignment
            rotation=10,            # Rotate text
            transform=ax.transAxes  # Transform relative to the axes (0 to 1 range)
        )
        # debuging
        logging.info("Ending the program.")

        return fig


    def clear_plot(self):
        # Clear the previous plot
        for widget in plotFrame.winfo_children():
            widget.destroy()

    def plot_to_canvas(self):
        # Add canvas to the plotFrame
        self.clear_plot()
        fig = self.creat_plot()
        canvas = FigureCanvasTkAgg(fig, master=plotFrame)  # A tk.DrawingArea.
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()
        logging.info("Plotting the graph to the canvas")

    # a func to save the plot
    def save_plot(self):
        fig = self.creat_plot()
        fig.savefig("simulation_results.png")
        logging.info("Saving the plot to a file")
        messagebox.showinfo("Save", "Plot saved as 'simulation_results.png'")

    # the function that will be triggered when the checkbox is toggled
    def risk_reducer_func(self):
        if check_var.get() == 1:
            consecutive_LossesEntry.config(state='normal')
        else:
            consecutive_LossesEntry.delete(0)
            consecutive_LossesEntry.config(state='disabled')



#------- GUI ------#
app = tk.Tk()
style = ttk.Style(app) # Create a style object
app.tk.call('source', './resources/Forest-ttk-theme/forest-dark.tcl') # Load custom theme
style.theme_use('forest-dark') # Set custom theme

app.title("Probability Simulator")
app.geometry("1200x650") # Set window size dynamically

app_frame = ttk.Frame(app, padding=(5, 5))
app_frame.pack(fill="both", expand=True)

#----- Tab1 input frame -----#
inputsLabel = ttk.LabelFrame(app_frame, text="Simulation inputs", padding=(15, 15))
inputsLabel.pack(side="left", padx=5)

balanceEntry = ttk.Spinbox(inputsLabel, from_=1000, to=1000000, increment=100)
balanceEntry.insert(0, 'balance')
balanceEntry.bind("<FocusIn>", lambda _: balanceEntry.delete('0', 'end')) # Clear the entry when clicked
balanceEntry.grid(column=0, row=0, sticky="ew", pady=5)

winrateEntry = ttk.Spinbox(inputsLabel, from_=0, to=1, increment=0.1)
winrateEntry.insert(0, "winrate (decimal)")
winrateEntry.bind("<FocusIn>", lambda _: winrateEntry.delete('0', 'end')) # Clear the entry when clicked
winrateEntry.grid(column=0, row=1, sticky="ew", pady=5)

riskEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.1)
riskEntry.insert(0, 'risk percentage')
riskEntry.bind("<FocusIn>", lambda _: riskEntry.delete('0', 'end'))
riskEntry.grid(column=0, row=2, sticky="ew", pady=5)

rrEntry = ttk.Spinbox(inputsLabel, from_=0, to=5, increment=0.5)
rrEntry.insert(0, 'risk reward')
rrEntry.bind("<FocusIn>", lambda _: rrEntry.delete('0', 'end'))
rrEntry.grid(column=0, row=3, sticky="ew", pady=5)

nTrades_entry = ttk.Spinbox(inputsLabel, from_=0, to=1000, increment=1)
nTrades_entry.insert(0, 'total trades')
nTrades_entry.bind("<FocusIn>", lambda _: nTrades_entry.delete('0', 'end'))
nTrades_entry.grid(column=0, row=4, sticky="ew", pady=5)

consecutive_LossesEntry = ttk.Spinbox(inputsLabel, from_=0, to=1000, increment=1)
consecutive_LossesEntry.insert(0, 'losses treshold')
consecutive_LossesEntry.bind("<FocusIn>", lambda _: consecutive_LossesEntry.delete('0', 'end'))
consecutive_LossesEntry.grid(column=0, row=5, sticky="ew", pady=5)
consecutive_LossesEntry.config(state="disabled")

# separator = ttk.Separator(inputsLabel, orient="horizontal")
# separator.grid(column=0, row=6, sticky="nsew", pady=10)

# Variable for Checkbutton state
check_var = tk.IntVar()
# Create Checkbutton and place it inside the LabelFrame
risk_reducerbutton = ttk.Checkbutton(inputsLabel, text="Risk Reducer", variable=check_var, command=Plotting([]).risk_reducer_func)
risk_reducerbutton.grid(column=0, row=7, pady=5)

calculateButton = ttk.Button(inputsLabel, text="Run Simulation", command=run_simulation)
calculateButton.grid(column=0, row=8, sticky="ew", pady=5)

separator = ttk.Separator(inputsLabel, orient="horizontal")
separator.grid(column=0, row=9, sticky="nsew", pady=5)

result_frame = ttk.LabelFrame(inputsLabel, text="Results")
result_frame.grid(column=0, row=10, sticky="nsew")
result_label = ttk.Label(result_frame, text="", anchor="center")
result_label.pack(expand=True, fill="both", padx=5, pady=5)

save_pic = ttk.Button(inputsLabel, text="Save Results", command=Plotting([]).save_plot)
save_pic.grid(column=0, row=11, pady=5, padx=5)

#----- tab1 plot frame -----#
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
