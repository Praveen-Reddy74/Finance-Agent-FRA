import numpy as np
from scipy.stats import norm
from utils.validators import normalize_percentage, validate_positive, validate_range

BLACK_SCHOLES_DESCRIPTION = """
Black-Scholes Call Option Pricing Model

Required Inputs:
- S (Stock Price): Current price of the underlying asset. Must be positive.
  Typical range: Any positive number (e.g., 10 to 1000+).

- K (Strike Price): Option strike price. Must be positive.
  Typical range: Any positive number.

- T (Time to Maturity): Time in years.
  Example: 0.5 = 6 months, 1 = 1 year.
  Must be positive.

- r (Risk-Free Rate): Annual risk-free interest rate.
  Can be given as:
    5   (interpreted as 5%)
    0.05 (interpreted as 5%)
  Typical range: 0% to 10%

- sigma (Volatility): Annual volatility of the asset.
  Can be given as:
    20  (interpreted as 20%)
    0.20 (interpreted as 20%)
  Typical range: 5% to 100%

Output:
- Call option price based on Black-Scholes model.
"""


def black_scholes_call(S, K, T, r, sigma):

    # Normalize percentage inputs
    r = normalize_percentage(r)
    sigma = normalize_percentage(sigma)

    # Validate inputs
    validate_positive(S, "Stock price")
    validate_positive(K, "Strike price")
    validate_positive(T, "Time to maturity")
    validate_positive(sigma, "Volatility")

    validate_range(r, -0.5, 0.5, "Risk-free rate")

    # Black-Scholes formula
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

    return call_price
