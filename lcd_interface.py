from RPLCD.i2c import CharLCD
import time
lcd = CharLCD(i2c_expander='PCF8574', address=0x3f, port=1,cols=16,rows=2,dotsize=8)
x_pos = 0
y_pos = 0 

def write_to_lcd(message):
  lcd.clear()
  lcd.write_string(message)
  lcd.cursor_pos = (0,0)

def write_and_shift(char, x_pos, y_pos):
  if x_pos > 15:
      x_pos = 0
      y_pos = y_pos + 1
  if y_pos > 1:
      y_pos = 0
  lcd.cursor_pos = (y_pos, x_pos)
  lcd.write_string(char)
  x_pos = x_pos + 1
  return x_pos, y_pos


def get_x():
    return lcd.cursor_pos[1]

def get_y():
    return lcd.cursor_pos[0]

def lcd_clear():
  lcd.clear()

def shift_y_pos(y_pos):
    lcd.cursor_pos = (y_pos, lcd.cursor_pos[1])




    
