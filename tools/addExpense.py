from dbConnection import get_connection

def add_expense(date, amount, catregory, subcategory, note):
    connection = get_connection()
    if connection is None:
        return "Failed to connect to the database."

    try:
        cursor = connection.cursor()
        add_expense_query = """
            INSERT INTO expenses (date, amount, category, subcategory, note)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(add_expense_query, (date, amount, catregory, subcategory, note))   
        connection.commit()
        return "Expense added successfully."
    except Exception as e:
        print("Error while adding expense:", e)
        return "Failed to add expense." + str(e)
    finally:
        if connection:
            cursor.close()
            connection.close()
