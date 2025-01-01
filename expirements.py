import tkinter as tk
from formulas.min_winrate import min_winrate_calculator

app = tk.Tk()
app.title("Risk Reward Ratio Calculator")
app.geometry("400x200")


def calculate_min_winrate():
    try:
        risk_reward_ratio = float(rr_entry.get())

        result = min_winrate_calculator(risk_reward_ratio)
        result_label.config(text=result)

    except ValueError:
        result_label.config(text="Please enter a valid number.")
    

tk.Label(app, text="Risk Reward Ratio:").pack()

rr_entry = tk.Entry(app)
rr_entry.pack()

rr_button = tk.Button(app, text="Calculate", command=calculate_min_winrate)
rr_button.pack()

result_label = tk.Label(app)
result_label.pack()


app.mainloop()

