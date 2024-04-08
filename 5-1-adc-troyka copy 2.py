import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

levels = 2 ** 8 - 1
maxVol = 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        signal = decimal2binary(value)
        GPIO.output(dac, signal)
        time.sleep(0.0007)
        voltage = value/ levels * maxVol

        compVal = GPIO.input(comp)
        if compVal == 1:
            print("Value", value, "Signal", signal, "Voltage", voltage)
            return value
            break

try:
    while (True):
        val = adc()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

