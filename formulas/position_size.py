from tkinter import messagebox

def get_position_sizing_result(account_balance, risk_percentage, stop_loss_pips, pip_value):
    try:
        # formula
        risk_amount = account_balance * (risk_percentage / 100)
        position_size = risk_amount / (stop_loss_pips * pip_value)

        # display the lot size
        messagebox.showinfo(title="Position Size", message=(f"Position Size: {position_size} lot"))
        return f"Position Size: {position_size} lot"

    except ValueError:
        return "Invalid Inputs!"
    except ZeroDivisionError:
        return "Stop loss cannot be zero"
    except Exception as e:
        return str(e)



