import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

T = float(input())

try:
    while True:
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(T)
            GPIO.output(dac, 0)


        for i in range(255, -1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(T)
            GPIO.output(dac, 0)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()