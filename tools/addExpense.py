from datetime import datetime

from dbConnection import get_connection

async def add_expense(date, amount, category, subcategory, note):

    pool = await get_connection()

    if pool is None:
        return "Failed to connect to the database."

    try:
        async with pool.acquire() as connection:

            add_expense_query = """
                INSERT INTO expenses (date, amount, category, subcategory, note)
                VALUES ($1, $2, $3, $4, $5)
            """

            date_obj = datetime.strptime(date, "%Y-%m-%d").date()

            await connection.execute(
                add_expense_query,
                date_obj,
                amount,
                category,
                subcategory,
                note
            )

        return "Expense added successfully."

    except Exception as e:
        print("Error while adding expense:", e)
        return "Failed to add expense: " + str(e)