from dbConnection import get_connection

async def total_expenses():

    pool = await get_connection()

    if pool is None:
        return "Failed to connect to the database."

    try:
        async with pool.acquire() as connection:

            total_expenses_query = "SELECT SUM(amount) FROM expenses"

            total = await connection.fetchval(total_expenses_query)

            if total is None:
                return 0

            return total

    except Exception as e:
        print("Error while calculating total expenses:", e)
        return "Failed to calculate total expenses: " + str(e)