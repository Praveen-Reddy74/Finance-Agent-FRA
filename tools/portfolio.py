import numpy as np
from scipy.optimize import minimize

PORTFOLIO_MIN_VAR_DESCRIPTION = """
Minimum Variance Portfolio Optimization

Purpose:
Finds asset weights that minimize total portfolio risk.

Required Input:
- cov_matrix: Covariance matrix of asset returns.
  Must be:
    - 2D square matrix
    - Symmetric
    - Positive variances on diagonal

Constraints:
- Weights sum to 1
- Long-only (no short selling)

Output:
- Optimal asset weights that minimize variance.
"""


def minimize_variance(cov_matrix):

    cov_matrix = np.array(cov_matrix)

    # --- Validation ---
    if cov_matrix.ndim != 2:
        raise ValueError("Covariance matrix must be 2-dimensional.")

    if cov_matrix.shape[0] != cov_matrix.shape[1]:
        raise ValueError("Covariance matrix must be square.")

    if not np.allclose(cov_matrix, cov_matrix.T):
        raise ValueError("Covariance matrix must be symmetric.")

    if np.any(np.diag(cov_matrix) <= 0):
        raise ValueError("Variances (diagonal elements) must be positive.")

    num_assets = cov_matrix.shape[0]

    # --- Objective function ---
    def portfolio_variance(weights):
        return weights.T @ cov_matrix @ weights

    # --- Constraints ---
    constraints = ({
        'type': 'eq',
        'fun': lambda w: np.sum(w) - 1
    })

    bounds = tuple((0, 1) for _ in range(num_assets))

    initial_guess = np.array([1.0 / num_assets] * num_assets)

    # --- Optimization ---
    result = minimize(
        portfolio_variance,
        initial_guess,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    if not result.success:
        raise ValueError("Optimization failed: " + result.message)

    return result.x
