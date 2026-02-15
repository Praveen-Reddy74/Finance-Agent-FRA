#  Testing Layer – Finance Agent

This folder validates all financial computation tools used by the agent.

It ensures:

- ✔ Correct mathematical outputs
- ✔ Proper input validation
- ✔ Error handling for edge cases
- ✔ Portfolio constraints are respected

Finance without testing is risk.  
This folder reduces it.

---

##  Structure

```
tests/
└── test_all_tools.py
```

---

##  What Is Tested

The script verifies:

- **CAPM** – expected return + beta validation  
- **Sharpe Ratio** – risk-adjusted return + volatility checks  
- **VaR** – confidence level boundaries  
- **Black-Scholes** – option pricing + input validation  
- **Altman Z-Score** – bankruptcy model constraints  
- **Portfolio Optimization** – weights sum to 1, long-only constraint  

It also tests invalid inputs to confirm proper error handling.

---

##  Run Tests

From project root:

```bash
python tests/test_all_tools.py
```

You should see:
- Valid outputs printed
- Errors raised for invalid cases
- Portfolio weights summing to 1

---

##  Why It Matters

- Prevents silent mathematical errors  
- Enforces validation rules  
- Demonstrates production-level discipline  

Reliable finance requires reliable code.

