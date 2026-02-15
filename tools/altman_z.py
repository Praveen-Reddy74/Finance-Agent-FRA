ALTMAN_Z_DESCRIPTION = """
Altman Z-Score Model (Original Manufacturing Version)

Purpose:
Estimates the probability of corporate bankruptcy using financial ratios.

Formula:
Z = 1.2*(Working Capital / Total Assets)
  + 1.4*(Retained Earnings / Total Assets)
  + 3.3*(EBIT / Total Assets)
  + 0.6*(Market Value of Equity / Total Liabilities)
  + 1.0*(Sales / Total Assets)

Required Inputs:
All values must be in consistent monetary units (e.g., all in millions or all in rupees).

- working_capital:
    Current Assets − Current Liabilities

- retained_earnings:
    Accumulated retained earnings of the company

- ebit:
    Earnings Before Interest and Taxes

- market_value_equity:
    Market capitalization (share price × shares outstanding)

- total_assets:
    Total assets from balance sheet
    Must be positive

- total_liabilities:
    Total liabilities from balance sheet
    Must be positive

- sales:
    Total revenue of the company

Interpretation:
- Z > 3.0     → Financially safe zone
- 1.8 < Z < 3 → Grey zone (moderate risk)
- Z < 1.8     → Distress zone (high bankruptcy risk)

Output:
- Z-score value indicating financial health.
"""


def calculate_altman_z(
    working_capital,
    retained_earnings,
    ebit,
    market_value_equity,
    total_assets,
    total_liabilities,
    sales
):

    if total_assets <= 0:
        raise ValueError("Total assets must be positive.")

    if total_liabilities <= 0:
        raise ValueError("Total liabilities must be positive.")

    z = (
        1.2 * (working_capital / total_assets) +
        1.4 * (retained_earnings / total_assets) +
        3.3 * (ebit / total_assets) +
        0.6 * (market_value_equity / total_liabilities) +
        1.0 * (sales / total_assets)
    )

    return z
