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
async def get_expenses_tool():
    return await get_expenses()

@mcp.tool()
async def total_expenses_tool():
    return await total_expenses()

@mcp.tool()
async def delete_expense_tool(expense_id: int):
    return await delete_expense(expense_id)

@mcp.tool()
async def range_expenses_tool(start_date: str, end_date: str):
    return await range_expenses(start_date, end_date)

@mcp.tool()
async def summary_tool():
    return await summary()

if __name__ == "__main__":
    mcp.run(port=8000, transport="http", host="0.0.0.0")
