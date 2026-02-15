from tools.capm import calculate_capm
from tools.sharpe import calculate_sharpe_ratio
from tools.var import calculate_var
from tools.black_scholes import black_scholes_call
from tools.altman_z import calculate_altman_z
from tools.portfolio import minimize_variance

import numpy as np


print("----- CAPM TESTS -----")
print("Valid:", calculate_capm(1.2, 3, 8))
try:
    print("Invalid Beta:", calculate_capm(10, 3, 8))
except Exception as e:
    print("Error:", e)


print("\n----- SHARPE TESTS -----")
print("Valid:", calculate_sharpe_ratio(12, 3, 15))
try:
    print("Invalid Std Dev:", calculate_sharpe_ratio(12, 3, 0))
except Exception as e:
    print("Error:", e)


print("\n----- VAR TESTS -----")
print("Valid:", calculate_var(5, 10, 0.95))
try:
    print("Invalid Confidence:", calculate_var(5, 10, 1.5))
except Exception as e:
    print("Error:", e)


print("\n----- BLACK-SCHOLES TEST -----")
print("Call Price:", black_scholes_call(S=100, K=100, T=1, r=5, sigma=20))


print("\n----- ALTMAN Z TEST -----")
print("Z Score:",
      calculate_altman_z(
          working_capital=500,
          retained_earnings=1000,
          ebit=300,
          market_value_equity=2000,
          total_assets=5000,
          total_liabilities=3000,
          sales=4000
      )
)


print("\n----- PORTFOLIO TEST -----")
cov_matrix = [[0.1, 0.02],
              [0.02, 0.08]]

weights = minimize_variance(cov_matrix)
print("Optimal Weights:", weights)
print("Sum of weights:", np.sum(weights))

