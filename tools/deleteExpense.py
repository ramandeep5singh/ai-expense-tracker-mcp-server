from dbConnection import get_connection

def delete_expense(expense_id):
    connection = get_connection()
    if connection is None:
        return "Failed to connect to the database."

    try:
        cursor = connection.cursor()
        delete_expense_query = "DELETE FROM expenses WHERE id = %s"
        cursor.execute(delete_expense_query, (expense_id,))
        connection.commit()
        if cursor.rowcount == 0:
            return f"No expense found with ID: {expense_id}"
        return f"Expense with ID: {expense_id} deleted successfully."
    except Exception as e:
        print("Error while deleting expense:", e)
        return "Failed to delete expense." + str(e)
    finally:
        if connection:
            cursor.close()
            connection.close()