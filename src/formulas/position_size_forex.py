from tkinter import messagebox

def get_position_sizing_result_forex(account_balance, risk_dollar, stop_loss_pips, pip_value):
    try:
        position_size = float(risk_dollar) / (stop_loss_pips * pip_value) # formula with dollar risk

        # display the lot size
        messagebox.showinfo(title="Position Size", message=(f"Position Size: {position_size} Lot"))
        return f"Position Size: {position_size} Lots"

    except ZeroDivisionError:
        return "Inputs cannot be zero."
    except ValueError:
        return "Invalid inputs."
    except Exception as e:
        return f"Error: {str(e)}"
