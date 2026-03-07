from dbConnection import get_connection

async def delete_expense(expense_id):

    pool = await get_connection()

    if pool is None:
        return "Failed to connect to the database."

    try:
        async with pool.acquire() as connection:

            delete_expense_query = """
                DELETE FROM expenses
                WHERE id = $1
            """

            result = await connection.execute(delete_expense_query, expense_id)

            rows_deleted = int(result.split(" ")[1])

            if rows_deleted == 0:
                return f"No expense found with ID: {expense_id}"

            return f"Expense with ID: {expense_id} deleted successfully."

    except Exception as e:
        print("Error while deleting expense:", e)
        return "Failed to delete expense: " + str(e)