import mysql.connector
from multiprocessing import Process
from lcd_interface import write_to_lcd, lcd_clear
import update_queue
import time
from gpiozero import DistanceSensor
import asyncio
from keypad import keypad_input
from ultrasonic import get_distance
from lighting import turn_on, turn_off
write_to_lcd("Code:")

async def get_input(row):
   result = keypad_input(row)
   return result

CODE = asyncio.run(get_input(1))

HOST = "smarthomedb.czsygqkws.com"
USER = "admin"
PASSWORD=""
DATABASE="interface"

connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        autocommit=True
    )


if connection.is_connected():
    print('connected')

new_cursor = connection.cursor(buffered=True)
new_cursor.execute(f'SELECT * FROM middldeman WHERE code = {CODE}')
initial_data = new_cursor.fetchall()[0]
new_cursor.close()

data = [0,0,0,0]
data = update_queue.wait_for_update(connection, CODE, data)
brightness = data[1]
ultrasonic_distance = data[2]
toggle = data[3]
light_toggle = False

print(data)

while True:
    time.sleep(1)
    if brightness > 1 and toggle == 1:
      if ultrasonic_distance > 1 and toggle == 1:
        new_distance = get_distance()
        write_to_lcd(f'Distance:{new_distance:.1f}cm')
        if new_distance <= ultrasonic_distance:
          turn_on()
        else:
          turn_off()
      elif toggle == 1:
        turn_on()
        write_to_lcd("Light On")
    else:
        turn_off()
        write_to_lcd("Turned Off")
    data = update_queue.wait_for_update(connection, CODE, data)
    brightness = data[1]
    ultrasonic_distance = data[2]
    toggle = data[3]


