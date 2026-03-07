from dbConnection import get_connection

def range_expenses(start_date, end_date):
    connection = get_connection()
    if connection is None:
        return "Failed to connect to the database."

    try:
        cursor = connection.cursor()
        range_expenses_query = """
            SELECT id, date, amount, category, subcategory, note 
            FROM expenses 
            WHERE date >= %s AND date <= %s
        """
        cursor.execute(range_expenses_query, (start_date, end_date))
        expenses = cursor.fetchall()
        return expenses
    except Exception as e:
        print("Error while fetching expenses in range:", e)
        return "Failed to fetch expenses in range." + str(e)
    finally:
        if connection:
            cursor.close()
            connection.close()