from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

def turn_on():
  sleep(0.2)
  led.value = 1


def turn_off():
  sleep(0.2)
  led.value = 0


