import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="db_expense_tracker",
            user="postgres",
            password="root",
            port=5432
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None
