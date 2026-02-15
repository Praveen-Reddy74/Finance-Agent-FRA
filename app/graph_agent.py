from typing import TypedDict, Sequence

from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition

# -----------------------------
# Import Computation Layer
# -----------------------------

from tools.capm import calculate_capm
from tools.sharpe import calculate_sharpe_ratio
from tools.var import calculate_var
from tools.black_scholes import black_scholes_call
from tools.altman_z import calculate_altman_z
from tools.portfolio import minimize_variance


# -----------------------------
# TOOL WRAPPERS
# -----------------------------

@tool
def capm(beta: float, risk_free_rate: float, market_return: float) -> float:
    """
    Calculate expected return using CAPM.
    Required inputs:
    - beta
    - risk_free_rate
    - market_return
    """
    return calculate_capm(beta, risk_free_rate, market_return)


@tool
def sharpe(portfolio_return: float, risk_free_rate: float, std_dev: float) -> float:
    """
    Calculate Sharpe Ratio.
    Required inputs:
    - portfolio_return
    - risk_free_rate
    - std_dev
    """
    return calculate_sharpe_ratio(portfolio_return, risk_free_rate, std_dev)


@tool
def var_tool(mean_return: float, std_dev: float, confidence_level: float) -> float:
    """
    Calculate Value at Risk (VaR).
    Required inputs:
    - mean_return
    - std_dev
    - confidence_level
    """
    return calculate_var(mean_return, std_dev, confidence_level)


@tool
def black_scholes(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calculate Black-Scholes Call Option Price.
    Required inputs:
    - S (stock price)
    - K (strike price)
    - T (time in years)
    - r (risk-free rate)
    - sigma (volatility)
    """
    return black_scholes_call(S, K, T, r, sigma)


@tool
def altman_z(
    working_capital: float,
    retained_earnings: float,
    ebit: float,
    market_value_equity: float,
    total_assets: float,
    total_liabilities: float,
    sales: float
) -> float:
    """
    Calculate Altman Z-Score.
    Required inputs:
    - working_capital
    - retained_earnings
    - ebit
    - market_value_equity
    - total_assets
    - total_liabilities
    - sales
    """
    return calculate_altman_z(
        working_capital,
        retained_earnings,
        ebit,
        market_value_equity,
        total_assets,
        total_liabilities,
        sales
    )


@tool
def portfolio_optimization(cov_matrix: list) -> list:
    """
    Perform minimum variance portfolio optimization.

    Required input:
    - cov_matrix (square covariance matrix)

    Example:
    [[0.1, 0.02],
     [0.02, 0.08]]
    """
    weights = minimize_variance(cov_matrix)
    return weights.tolist()


tools = [
    capm,
    sharpe,
    var_tool,
    black_scholes,
    altman_z,
    portfolio_optimization
]


# -----------------------------
# AGENT STATE
# -----------------------------

class AgentState(TypedDict):
    messages: Sequence[BaseMessage]


# -----------------------------
# SYSTEM PROMPT (BEHAVIOR CONTROL)
# -----------------------------

SYSTEM_PROMPT = """
You are a financial computation assistant.

Behavior Rules:

1. If the user mentions a financial model
   (CAPM, Sharpe Ratio, Value at Risk, Black-Scholes,
   Altman Z-Score, Portfolio Optimization)
   but does NOT provide all required numerical inputs:

   - Briefly explain what the model does.
   - Clearly list ALL required inputs.
   - For each input, show:
       • What it represents
       • Typical value range
       • Example format (e.g., 5 or 0.05 for 5%)
   - Ask the user to provide the values.

2. Only call a tool when ALL required inputs are clearly provided.

3. When returning results:
   - Provide the computed value.
   - Show the formula used.
   - Give a short interpretation of the result.

Never call a tool with missing arguments.
Be precise and structured.
"""



# -----------------------------
# CONNECT LLM + BIND TOOLS
# -----------------------------


llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    streaming=False
).bind_tools(tools)



# -----------------------------
# GRAPH NODES
# -----------------------------


def chatbot(state: AgentState):
    print("\n--- STATE BEFORE LLM ---")
    for m in state["messages"]:
        print(type(m), m)

    response = llm.invoke(state["messages"])
    print("DEBUG TOOL CALLS:", response.tool_calls)

    return {"messages": state["messages"] + [response]}



tool_node = ToolNode(tools)



# -----------------------------
# BUILD LANGGRAPH
# -----------------------------

graph = StateGraph(AgentState)

graph.add_node("chatbot", chatbot)
graph.add_node("tools", tool_node)

graph.set_entry_point("chatbot")

graph.add_conditional_edges(
    "chatbot",
    tools_condition,
    {
        "tools": "tools",
        END: END
    }
)

graph.add_edge("tools", "chatbot")

app = graph.compile()


# -----------------------------
# RUN INTERACTIVE LOOP
# -----------------------------

if __name__ == "__main__":

    print("\n🚀 Finance Agent Ready")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = app.invoke({
            "messages": [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=user_input)
            ]
        })

        print("Agent:", result["messages"][-1].content)
