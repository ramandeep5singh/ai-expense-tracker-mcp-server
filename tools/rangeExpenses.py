from dbConnection import get_connection

async def range_expenses(start_date, end_date):

    pool = await get_connection()

    if pool is None:
        return "Failed to connect to the database."

    try:
        async with pool.acquire() as connection:

            range_expenses_query = """
                SELECT id, date, amount, category, subcategory, note
                FROM expenses
                WHERE date >= $1 AND date <= $2
            """

            expenses = await connection.fetch(
                range_expenses_query,
                start_date,
                end_date
            )

            return [dict(row) for row in expenses]

    except Exception as e:
        print("Error while fetching expenses in range:", e)
        return "Failed to fetch expenses in range: " + str(e)