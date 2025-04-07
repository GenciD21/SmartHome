from gpiozero import DistanceSensor
import time

ultrasonic = DistanceSensor(echo=24, trigger=23)
def get_distance():
    return ultrasonic.distance*100


