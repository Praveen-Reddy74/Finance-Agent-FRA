from utils.validators import normalize_percentage, validate_positive

SHARPE_DESCRIPTION = """
Sharpe Ratio

Purpose:
Measures risk-adjusted return of a portfolio.
It tells us how much excess return we earn per unit of risk.

Formula:
Sharpe Ratio = (Portfolio Return − Risk-Free Rate) / Standard Deviation

Required Inputs:
- portfolio_return: Expected or realized portfolio return.
  Can be given as:
    12   (interpreted as 12%)
    0.12 (interpreted as 12%)
  Typical range: -100% to +100%

- risk_free_rate: Risk-free return (e.g., government bond yield).
  Can be given as:
    5   (interpreted as 5%)
    0.05 (interpreted as 5%)
  Typical range: 0% to 10%

- std_dev: Standard deviation (volatility) of portfolio returns.
  Can be given as:
    15   (interpreted as 15%)
    0.15 (interpreted as 15%)
  Must be positive.
  Typical range: 5% to 50%

Interpretation:
- Sharpe > 1  → Good risk-adjusted return
- Sharpe > 2  → Very strong performance
- Sharpe < 1  → Weak risk-adjusted performance
- Negative    → Underperforming risk-free rate

Output:
- Risk-adjusted return metric (dimensionless number).
"""


def calculate_sharpe_ratio(portfolio_return, risk_free_rate, std_dev):

    portfolio_return = normalize_percentage(portfolio_return)
    risk_free_rate = normalize_percentage(risk_free_rate)
    std_dev = normalize_percentage(std_dev)

    validate_positive(std_dev, "Standard deviation")

    return (portfolio_return - risk_free_rate) / std_dev
