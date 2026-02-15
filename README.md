# Finance-Agent-FRA  
LLM-Powered Financial Reasoning Agent

An intelligent finance assistant designed to help students understand  
what financial models are, why they are used, and how they work — not just compute them.

Built using:

- Llama 3 (via Ollama)
- LangGraph (tool orchestration)
- Modular financial computation layer
- Structured validation system

---

## Problem Statement

Most finance tools:

- Only compute numerical outputs
- Do not explain reasoning
- Fail silently when inputs are invalid

This project implements a tool-augmented LLM agent that:

- Explains financial models when inputs are missing
- Clearly lists required parameters
- Validates all numerical inputs
- Executes tools only when inputs are complete
- Returns structured results with interpretation

It behaves like a finance tutor rather than a calculator.

---

## Architecture Overview

```
User
  ↓
Llama 3 (Reasoning Layer)
  ↓
LangGraph Decision Engine
  ↓
Financial Tool Execution
  ↓
Validated & Interpreted Output
```

The system separates:

- Reasoning Layer → LLM  
- Execution Layer → Financial Models  
- Control Layer → LangGraph  

This modular design ensures safety, clarity, and extensibility.

---

## Implemented Financial Models

- CAPM (Capital Asset Pricing Model)
- Sharpe Ratio
- Value at Risk (VaR)
- Black-Scholes Option Pricing
- Altman Z-Score
- Minimum Variance Portfolio Optimization

Each model includes:

- Input normalization (percentage handling)
- Range validation
- Error handling for invalid cases
- Deterministic outputs

---

## Repository Structure

```
Finance-Agent-FRA/
│
├── app/        # LLM orchestration layer
├── tools/      # Financial computation modules
├── utils/      # Shared validation logic
├── tests/      # Tool validation tests
└── README.md
```

---

## How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the agent:

```
python app/graph_agent.py
```

Example query:

```
Calculate CAPM with beta 1.2, risk-free rate 3%, market return 8%
```

If inputs are missing, the agent will explain the required parameters before executing the model.

---

## Testing

Run all financial tool tests:

```
python tests/test_all_tools.py
```

This verifies:

- Correct mathematical outputs
- Input validation rules
- Portfolio constraints
- Proper error handling

---

## Design Highlights

- Tool-augmented LLM architecture
- Deterministic reasoning (temperature = 0)
- Strict input validation
- Modular financial engine
- Clear separation of reasoning and execution

---

## Future Improvements

- REST API deployment
- Web interface (Streamlit or FastAPI)
- Integration with live market data
- Monte Carlo simulation module
- Continuous Integration workflow

---

This project demonstrates structured LLM engineering combined with validated financial computation, built for clarity, safety, and extensibility.

