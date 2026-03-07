from dbConnection import get_connection

def get_expenses():
    connection = get_connection()
    if connection is None:
        return "Failed to connect to the database."

    try:
        cursor = connection.cursor()
        get_expenses_query = "SELECT id, date, amount, category, subcategory, note FROM expenses"
        cursor.execute(get_expenses_query)
        expenses = cursor.fetchall()
        return expenses
    except Exception as e:
        print("Error while fetching expenses:", e)
        return "Failed to fetch expenses." + str(e)
    finally:
        if connection:
            cursor.close()
            connection.close()