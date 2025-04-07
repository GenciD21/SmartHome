import mysql.connector
import time
def wait_for_update(connection, CODE, initial_data):
    new_cursor = connection.cursor(buffered=True)
    new_cursor.execute(f"SELECT * FROM middldeman WHERE code = {CODE}")
    data = new_cursor.fetchall()[0]
    if data != initial_data:
        print(data)
        print("changes detected!")
        new_cursor.close()
        return data
    new_cursor.close()
    return initial_data
    
