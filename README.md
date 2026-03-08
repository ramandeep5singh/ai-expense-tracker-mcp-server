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

# Project Architecture

Claude Desktop
↓
Remote MCP Server (FastMCP Cloud)
↓
Async Python Tools
↓
Neon PostgreSQL Database

---

# Project Structure

expense-tracker-mcp-server

* main.py → MCP server and tool registration
* dbConnection.py → asynchronous database connection logic
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

```
CREATE TABLE expenses (
 id SERIAL PRIMARY KEY,
 date DATE,
 amount NUMERIC,
 category VARCHAR(100),
 subcategory VARCHAR(100),
 note TEXT
);
```

---

# Development Journey

### 1. Initial Local MCP Server

The project began as a **local MCP server** using FastMCP with a PostgreSQL database.

Tools were implemented for:

* Adding expenses
* Retrieving expenses
* Deleting expenses
* Viewing summaries

The database connection was handled using **psycopg2**.

---

### 2. Code Refactoring

A separate module `dbConnection.py` was created to manage database connections so that all tools could reuse the same connection logic.

This improved code maintainability and avoided duplication.

---

### 3. Converting to Asynchronous Server

The original implementation was **synchronous**, which blocked the server during database operations.

To improve performance and scalability:

* `psycopg2` was replaced with **asyncpg**
* All database functions were converted to **async functions**
* A PostgreSQL **connection pool** was implemented

This allows multiple MCP tool requests to run concurrently.

---

### 4. Migrating to Cloud Database

Since the server was later deployed remotely, the local database could not be used.

The project migrated to **Neon PostgreSQL**, a serverless cloud database.

Environment variables were configured in the deployment environment to connect securely.

---

### 5. Remote MCP Server Deployment

The MCP server was deployed using **FastMCP Cloud**.

The GitHub repository was connected to the platform so that:

* Every commit automatically triggers a new deployment
* The MCP endpoint stays updated with the latest code

---

### 6. Connecting Claude Desktop

The deployed MCP server requires authentication.

Claude Desktop was connected using the **`.dxt` integration file**, which automatically configures the MCP server connection.

---

# Setup

## Option 1 — Using a Virtual Environment (Recommended)

Create environment:
python -m venv .venv

Activate (Windows):
.venv\Scripts\activate

Install dependencies:
pip install fastmcp asyncpg

---

## Option 2 — Using Global Python Environment

Install dependencies globally:
pip install fastmcp asyncpg

---

# Running the Server Locally

Start the MCP server:
python main.py

Restart **Claude Desktop** after updating MCP configuration.

---

# Tools Available

* `add_expense` → Add a new expense
* `get_expenses` → Retrieve all expenses
* `total_expenses` → Calculate total spending
* `delete_expense` → Remove an expense
* `range_expenses` → Expenses within a date range
* `summary` → Category-wise spending summary

---

# Tech Stack

* Python
* FastMCP
* asyncpg
* PostgreSQL
* Neon Database
* Claude Desktop
* Model Context Protocol (MCP)

---

# Key Takeaways

* MCP enables AI assistants to interact with real systems using structured tools.
* Asynchronous database access significantly improves MCP server scalability.
* Cloud deployment requires environment variables and a remote database.
* Proper separation of database logic and tool logic improves maintainability.
