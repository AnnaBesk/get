import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 1, 1, 1, 1, 1, 1, 1]
num = 127
print(bin(num))
GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()