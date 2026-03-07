from dbConnection import get_connection

def total_expenses():
    connection = get_connection()
    if connection is None:
        return "Failed to connect to the database."

    try:
        cursor = connection.cursor()
        total_expenses_query = "SELECT SUM(amount) FROM expenses"
        cursor.execute(total_expenses_query)
        total = cursor.fetchone()[0]
        if total is None:
            return 0
        return total
    except Exception as e:
        print("Error while calculating total expenses:", e)
        return "Failed to calculate total expenses." + str(e)
    finally:
        if connection:
            cursor.close()
            connection.close()