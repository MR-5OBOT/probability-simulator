from tkinter import messagebox

def get_position_sizing_result_futures(account_balance, risk_dollar, stop_loss_pips, point_value):
    try:
        position_size = float(risk_dollar) / (stop_loss_pips * point_value) # formula with dollar risk

        # display the lot size
        messagebox.showinfo(title="Position Size", message=(f"Position Size: {position_size} contacts"))
        return f"Position Size: {position_size} contacts"

    except ZeroDivisionError:
        return "Inputs cannot be zero."
    except ValueError:
        return "Invalid inputs."
    except Exception as e:
        return f"Error: {str(e)}"
