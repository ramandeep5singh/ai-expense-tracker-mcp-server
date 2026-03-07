import random
from fastmcp import FastMCP
from tools.addExpense import add_expense
from tools.getExpenses import get_expenses
from tools.totalExpenses import total_expenses
from tools.deleteExpense import delete_expense
from tools.rangeExpenses import range_expenses
from tools.summary import summary

from dbConnection import init_db

#create a fastmcp server instance
mcp = FastMCP(name="Expense Tracker Server")

@mcp.on_startup
async def startup():
    await init_db()

@mcp.tool()
async def add_expense_tool(
    date: str, 
    amount: float, 
    category: str, 
    subcategory: str, 
    note: str):
    return await add_expense(date, amount, category, subcategory, note)

@mcp.tool()
def get_expenses_tool():
    return get_expenses()

@mcp.tool()
def total_expenses_tool():
    return total_expenses()

@mcp.tool()
def delete_expense_tool(expense_id: int):
    return delete_expense(expense_id)

@mcp.tool()
def range_expenses_tool(start_date: str, end_date: str):
    return range_expenses(start_date, end_date)

@mcp.tool()
def summary_tool():
    return summary()

if __name__ == "__main__":
    mcp.run(port=8000, transport="http", host="0.0.0.0")
