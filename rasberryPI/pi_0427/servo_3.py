import RPI.GPIO as GPIO
import time

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)

for t_high in range(30,125):    #부드러운 모션을 위해 10을 곱했다.
    pwm.ChangeDutyCycle(t_high / 10.0)   #30 = 0도 .... 125 = 180도
    time.sleep(0.02)
    pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()
