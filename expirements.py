import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# root window
root = tk.Tk()
root.title('Posiion size calculator')
# root.geometry('300x70')
root.resizable(False, False)

style = ttk.Style() # access the style database
style.theme_use('clam') # set the theme

# add a fram_forex
fram_forex = ttk.Frame(root, padding=5)
fram_forex.grid(row=0, column=0, sticky="nsew")


def calculate_position_size_forex():
    try:
        account_balance = float(entry_account_balance_forex.get())
        risk_dollar = entry_amount_risk_forex.get().strip("$")
        stop_loss_pips = float(entry_stop_loss_pips_forex.get())
        pip_value = float(entry_pip_value_forex.get())

        # calculate the position size
        position_size = float(risk_dollar) / (stop_loss_pips * pip_value) # formula with dollar risk
        # display the lot size
        messagebox.showinfo(title="Position Size", message=(f"Position Size: {position_size} Lot"))
        label_result_futures_forex.configure(text=f"Position Size: {position_size} Lots")

    except ValueError:
        label_result_futures_forex.configure(text="Error: Please enter valid numbers.")
        messagebox.showerror(title="Error", message="Please enter valid numbers.")

# add a title
forex_title = ttk.Label(fram_forex, text="Position Size Forex", font=("Arial", 14 , "bold"), padding=5)
forex_title.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

# 1
ttk.Label(fram_forex, text="Acc balance").grid(column=0, row=1, pady=5, padx=10)
entry_account_balance_forex = ttk.Entry(fram_forex)
entry_account_balance_forex.grid(column=1, row=1, sticky="")
# 2
ttk.Label(fram_forex, text="Amount risk").grid(column=0, row=2, pady=5, padx=10)
entry_amount_risk_forex = ttk.Entry(fram_forex)
entry_amount_risk_forex.grid(column=1, row=2, sticky="", pady=5, padx=10)
# 3
ttk.Label(fram_forex, text="Stop loss").grid(column=0, row=3, pady=5, padx=10)
entry_stop_loss_pips_forex = ttk.Entry(fram_forex)
entry_stop_loss_pips_forex.grid(column=1, row=3, sticky="", pady=5, padx=10)
# 4
ttk.Label(fram_forex, text="Pip value").grid(column=0, row=4, pady=5, padx=10)
entry_pip_value_forex = ttk.Entry(fram_forex)
entry_pip_value_forex.grid(column=1, row=4, sticky="", pady=5, padx=10)
# 5
calculat_button_forex = ttk.Button(fram_forex, text="Calculate", command=calculate_position_size_forex)
calculat_button_forex.grid(column=0, row=5, columnspan=2, padx=10, pady=5)
# style.map("TButton", foreground=[('pressed', 'white'), ('active', 'black')], background=[('pressed', '!disabled', '#252525'), ('active', 'white')])

label_result_futures_forex = ttk.Label(fram_forex)
label_result_futures_forex.grid(column=0, row=6, columnspan=2, pady=5, padx=5)


# run the app
root.mainloop()
