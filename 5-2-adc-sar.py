import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

levels = 2 ** 8 - 1
maxVol = 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT, initial = 0)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def adc():
    val = 0
    for i in range(7, -1, -1):
        val += 2 ** i
        signal = decimal2binary(val)
        GPIO.output(dac, signal)
        time.sleep(0.007)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            val -= 2 ** i
    
    signal = decimal2binary(val)
    voltage = val/ levels * maxVol
    print("Value", val, "Signal", signal, "Voltage", voltage)

try:
    while (True):
        adc()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

