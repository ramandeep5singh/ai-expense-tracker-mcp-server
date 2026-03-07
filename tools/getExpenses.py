from dbConnection import get_connection

async def get_expenses():

    pool = await get_connection()

    if pool is None:
        return "Failed to connect to the database."

    try:
        async with pool.acquire() as connection:

            get_expenses_query = """
                SELECT id, date, amount, category, subcategory, note
                FROM expenses
            """

            expenses = await connection.fetch(get_expenses_query)

            return expenses

    except Exception as e:
        print("Error while fetching expenses:", e)
        return "Failed to fetch expenses: " + str(e)