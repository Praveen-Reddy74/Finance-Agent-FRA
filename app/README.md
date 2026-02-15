
#  Finance Agent – Application Layer

This folder contains the **LLM orchestration layer** of the Finance Agent.

It connects:
-  Llama 3 (via Ollama)
-  LangGraph (tool routing engine)
-  Financial computation tools

This is where reasoning meets execution.

---

## 📂 Folder Structure

```
app/
│
├── graph_agent.py     # Main LangGraph-powered agent
├── README.md          # This file
```

---

# 🚀 graph_agent.py

## 🎯 Purpose

`graph_agent.py` is the core orchestration engine of the project.

It:

- Connects to Llama 3 using Ollama
- Binds financial tools to the LLM
- Uses LangGraph to control tool execution
- Enforces structured reasoning rules
- Prevents invalid tool calls

---

## 🏗 Architecture Flow

```
User Input
     ↓
System Prompt (Behavior Rules)
     ↓
Llama 3 (Reasoning Layer)
     ↓
LangGraph Conditional Router
     ↓
Tool Execution (if required)
     ↓
LLM Interpretation
     ↓
User Output
```

This ensures the model:
- Explains models when inputs are missing
- Calls tools only when all required inputs are present
- Returns structured financial reasoning

---

## 🧩 Agent Components

### 1️ LLM Initialization

```python
llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    streaming=False
).bind_tools(tools)
```

Why temperature = 0?

- Deterministic reasoning
- No hallucinated financial calculations
- Safe numeric outputs

---

### 2️ System Prompt (Behavior Guardrails)

The system prompt enforces:

- Explain model if inputs missing
- List required inputs clearly
- Show formula used
- Interpret results
- Never call tools with missing arguments

This makes the agent behave like a **finance tutor**, not just a calculator.

---

### 3️ ToolNode Integration

```python
tool_node = ToolNode(tools)
```

LangGraph automatically:

- Detects tool calls
- Routes execution
- Feeds results back to the LLM

---

### 4️ Conditional Execution Graph

```python
graph.add_conditional_edges(
    "chatbot",
    tools_condition,
    {
        "tools": "tools",
        END: END
    }
)
```

This is the brain switch.

If the LLM decides:
- A tool is needed → execute tool
- No tool needed → respond directly

---

# = How to Run

From project root:

```bash
python app/graph_agent.py
```

Then try:

```
Calculate CAPM with beta 1.2, risk-free rate 3%, market return 8%
```

Or try incomplete input:

```
Calculate Sharpe ratio
```

The agent will explain required inputs before computing.

---

# 🛡 Safety Features

✔ Strict input validation  
✔ No tool execution with missing arguments  
✔ Deterministic outputs  
✔ Structured financial explanation  

---

# 🧠 Why Th
