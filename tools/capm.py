from utils.validators import normalize_percentage, validate_range

CAPM_DESCRIPTION = """
Capital Asset Pricing Model (CAPM)

Purpose:
Calculates the expected return of an asset based on its systematic risk.

Formula:
Expected Return = Risk-Free Rate + Beta × (Market Return − Risk-Free Rate)

Required Inputs:
- beta: Sensitivity of asset to market movements.
  Typical range: 0 to 3
  1 = market-level risk
  >1 = more volatile than market
  <1 = defensive asset

- risk_free_rate: Government bond yield.
  Can be given as:
    5   (interpreted as 5%)
    0.05 (interpreted as 5%)
  Typical range: 0% to 10%

- market_return: Expected return of the market.
  Can be given as:
    8   (interpreted as 8%)
    0.08 (interpreted as 8%)
  Typical range: 5% to 15%
  Should be greater than risk-free rate.

Output:
- Expected return of the asset.
"""


def calculate_capm(beta, risk_free_rate, market_return):

    risk_free_rate = normalize_percentage(risk_free_rate)
    market_return = normalize_percentage(market_return)

    validate_range(beta, 0, 5, "Beta")
    validate_range(risk_free_rate, 0, 0.20, "Risk-free rate")

    if market_return <= risk_free_rate:
        raise ValueError("Market return should be greater than risk-free rate.")

    return risk_free_rate + beta * (market_return - risk_free_rate)
