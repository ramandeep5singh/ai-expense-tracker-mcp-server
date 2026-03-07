# AI Expense Tracker MCP Server

A lightweight **AI-powered expense tracking backend** that allows **Claude Desktop** to manage expenses using natural language through the **Model Context Protocol (MCP)**.

Example prompts a user can give Claude:

* “Add an expense of 200 for groceries today.”
* “Show my expenses this week.”
* “How much did I spend on food?”

Claude converts these prompts into **MCP tool calls**, which are handled by this Python server and stored in a PostgreSQL database.

---

# Project Environment

This project was **developed and tested on Windows**.

The MCP server can run using either:

1. **Global Python environment**
2. **Virtual environment (.venv)**

Both approaches are supported depending on your setup.

---

# Project Structure

expense-tracker-mcp-server

* main.py → MCP server and tool registration
* dbConnection.py → database connection logic
* tools/

  * addExpense.py
  * getExpenses.py
  * totalExpenses.py
  * deleteExpense.py
  * rangeExpenses.py
  * summary.py

---

# Database Schema

Table: `expenses`

Columns:

* id (primary key)
* date
* amount
* category
* subcategory
* note

Example:
CREATE TABLE expenses (
 id SERIAL PRIMARY KEY,
 date DATE,
 amount NUMERIC,
 category VARCHAR(100),
 subcategory VARCHAR(100),
 note TEXT
);

---

# Setup

## Option 1 — Using a Virtual Environment (Recommended)

Create environment:
python -m venv .venv


Activate (Windows):
.venv\Scripts\activate

Install dependencies:
pip install psycopg2-binary fastmcp

Claude MCP configuration:
{
  "mcpServers": {
    "expense-tracker": {
      "command": "C:\\expense-tracker-mcp-server\\.venv\\Scripts\\python.exe",
      "args": ["C:\\expense-tracker-mcp-server\\main.py"]
    }
  }
}

---

## Option 2 — Using Global Python Environment

Install dependencies globally:
pip install psycopg2-binary fastmcp

Claude MCP configuration:
{
  "mcpServers": {
    "expense-tracker": {
      "command": "python",
      "args": ["C:\\expense-tracker-mcp-server\\main.py"]
    }
  }
}

---

# Running the Server

Start the MCP server:
python main.py

Restart **Claude Desktop** after updating the MCP configuration.

---

# Tools Available

* `add_expense` → Add a new expense
* `get_expenses` → Retrieve all expenses
* `total_expenses` → Total spending by category
* `delete_expense` → Remove an expense
* `range_expenses` → Expenses within a date range
* `summary` → Monthly spending summary

---

# Key Takeaways

* MCP allows AI assistants to control external systems via structured tools.
* Proper Python environment configuration is essential for MCP servers.
* Separating database logic and tool logic improves maintainability.

---

# Tech Stack

* Python
* FastMCP
* PostgreSQL
* Claude Desktop
* Model Context Protocol (MCP)
