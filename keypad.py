# import required libraries
import RPi.GPIO as GPIO
import time
from lcd_interface import write_and_shift, get_x, get_y, lcd_clear, write_to_lcd
# these GPIO pins are connected to the keypad
# change these according to your connections!

# Initialize the GPIO pins

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)

#GPIO.setup(L1, GPIO.OUT)
#GPIO.setup(L2, GPIO.OUT)
#GPIO.setup(L3, GPIO.OUT)
#GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors

#GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def readLine(line, characters, data, start_y_pos):
    C1 = 12
    C2 = 16
    C3 = 20
    C4 = 21
    x_pos = get_x()
    y_pos = start_y_pos
    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
      if characters[0] == '*':
        print("clear")
        lcd_clear()
        return "",y_pos
      else:
        x_pos, y_pos = write_and_shift(characters[0], x_pos, y_pos)
      data = data + characters[0]
    if(GPIO.input(C2) == 1):
      x_pos, y_pos = write_and_shift(characters[1], x_pos, y_pos)
      data = data + characters[1]
    if(GPIO.input(C3) == 1):
      if characters[2] == '#':
        return data + "STOP", y_pos
      else:
        x_pos, y_pos = write_and_shift(characters[2], x_pos, y_pos)
        data = data + characters[2]
    if(GPIO.input(C4) == 1):
      x_pos, y_pos = write_and_shift(characters[3], x_pos, y_pos)
      data = data + characters[3]  
    GPIO.output(line, GPIO.LOW)
    return data, y_pos

def keypad_input(y_pos):
    L1 = 25
    L2 = 8
    L3 = 7
    L4 = 1
    C1 = 12
    C2 = 16
    C3 = 24
    C4 = 21
    data = ""
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)
    GPIO.setup(L4, GPIO.OUT)
    try:
        while True:
            data,y_pos = readLine(L1, ["1","2","3","A"], data,y_pos)
            data,y_pos = readLine(L2, ["4","5","6","B"], data,y_pos)
            data,y_pos = readLine(L3, ["7","8","9","C"], data,y_pos)
            data,y_pos = readLine(L4, ["*","0","#","D"], data,y_pos)
            if "STOP" in data:
                write_to_lcd("Data Recieved")
                print(data[0:data.index("STOP")])
                return data[0:data.index("STOP")] 
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nApplication stopped!")
