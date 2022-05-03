import RPI.GPIO as GPIO
import time

button_pin = 27
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)

try:
    while True:
        buttonInput = GPIO.input(button_pin)
        print(buttonInput)

except: KeyboardInterrupt:
    pass

GPIO.cleanup()





