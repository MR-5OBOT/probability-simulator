def min_winrate_calculator(risk_reward_ratio):
    """
    Calculate minimum win rate required for profitability.
    
    Parameters:
        risk_reward_ratio (float): Risk-reward ratio.
        
    Returns:
        str: A formatted string with the minimum win rate.
    """
    if risk_reward_ratio <= 0:
        return "Risk-reward ratio must be greater than zero."
    elif risk_reward_ratio >= 1:
        return "please enter a risk-reward ratio in decimal form."

    winrate = 1 / (1 + risk_reward_ratio) * 100
    return f"Minimum Win Rate: {winrate:.0f}%"

