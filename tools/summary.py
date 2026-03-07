from dbConnection import get_connection

def summary():
    connection = get_connection()
    if connection is None:
        return "Failed to connect to the database."

    try:
        cursor = connection.cursor()
        summary_query = """
            SELECT category, SUM(amount) as total_amount 
            FROM expenses 
            GROUP BY category
            ORDER BY total_amount DESC
        """
        cursor.execute(summary_query)
        summary_data = cursor.fetchall()
        return summary_data
    except Exception as e:
        print("Error while fetching summary:", e)
        return "Failed to fetch summary." + str(e)
    finally:
        if connection:
            cursor.close()
            connection.close()