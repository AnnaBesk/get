import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

if GPIO.input(25) == 1:
    GPIO.output(20, 1)
else:
    GPIO.output(20, 0)
