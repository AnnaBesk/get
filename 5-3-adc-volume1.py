import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

comp = 14
troyka = 13

levels = 2 ** 8 - 1
maxVol = 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)


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
    return 255

try:
    while (True):
        val = adc()
        if val == 0:
            GPIO.output(leds, 0)
        elif not type(val):
            GPIO.output(leds, 1)
        else:
            count = int((val / 255) * 8)
            GPIO.output(leds[0:count], 1)
            GPIO.output(leds[count + 1:], 0)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

