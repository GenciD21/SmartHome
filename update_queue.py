import mysql.connector
import time
HOST = ""
USER = "admin"
PASSWORD = ""
DATABASE = "interface"
connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            autocommit=True
    )
if connection.is_connected():
    print("Connected to the database")
def wait_for_update(CODE):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM middldeman WHERE code = {CODE}")
    initial_data = cursor.fetchall()[0]
    cursor.close()

    
    while True:
        print("waiting for change...")
        new_cursor = connection.cursor()
        new_cursor.execute(f"SELECT * FROM middldeman WHERE code = {CODE}")
        data = new_cursor.fetchall()[0]
        print(data)
        print(initial_data)
        print("-----")
        if data != initial_data:
            print("changes detected!")
            break
        time.sleep(1)
        new_cursor.close()
    time.sleep(1)
    return wait_for_update(CODE)
    

wait_for_update(233)