import mysql.connector
from mysql.connector import Error

# Database credentials
HOST = ""
USER = "admin"
PASSWORD = ""
DATABASE = "interface"


def db_write(CODE, BRIGHTNESS, DISTANCE, ON):
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        if connection.is_connected():
            print("Connected to the database")

        # Insert data
        check_cursor = connection.cursor()
        check_cursor.execute(f"SELECT EXISTS (SELECT 1 FROM middldeman WHERE code = {CODE});")
        check_value = check_cursor.fetchall()[0][0]
        print(check_value)
        if check_value != 1:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO middldeman (Code, Brightness, Distance, Toggle)
            VALUES (%s, %s, %s, %s)
            """
            values = (CODE, BRIGHTNESS, DISTANCE, ON)
            cursor.execute(insert_query, values)
            cursor.close()
            connection.commit()
            print(f"{cursor.rowcount} row(s) inserted.")

        else:
            update_cursor = connection.cursor()
            update_cursor.execute(f"UPDATE middldeman SET Brightness = {BRIGHTNESS}, Distance = {DISTANCE}, Toggle = '{ON}' WHERE code = {CODE}")
            connection.commit()
            update_cursor.close()
    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Connection closed.")

