from tkinter import messagebox

def get_position_sizing_result_forex(account_balance, risk_dollar, stop_loss_pips, pip_value):
    """
    Calculate the position size for forex trading.
    :param account_balance: float
    :param risk_dollar: float
    :param stop_loss_pips: float
    :param pip_value: float
    :return: float

    note: account_balance is not used in the calculation cuz we are using the risk_dollar
    """
    position_size = float(risk_dollar) / (stop_loss_pips * pip_value) # formula with dollar risk

    # display the lot size
    messagebox.showinfo(title="Position Size", message=(f"Position Size: {position_size} Lot"))
    return f"Position Size: {position_size} Lots"

