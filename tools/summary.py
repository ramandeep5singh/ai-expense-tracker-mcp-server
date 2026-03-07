from dbConnection import get_connection

async def summary():

    pool = await get_connection()

    if pool is None:
        return "Failed to connect to the database."

    try:
        async with pool.acquire() as connection:

            summary_query = """
                SELECT category, SUM(amount) as total_amount
                FROM expenses
                GROUP BY category
                ORDER BY total_amount DESC
            """

            summary_data = await connection.fetch(summary_query)

            return [dict(row) for row in summary_data]

    except Exception as e:
        print("Error while fetching summary:", e)
        return "Failed to fetch summary: " + str(e)