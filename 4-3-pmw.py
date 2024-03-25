import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

gate = 21
led = 22

GPIO.setup(gate, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

duty_cycle = 0
p = GPIO.PWM(gate, 1000)
p.start(duty_cycle)

p1 = GPIO.PWM(led, 1000)
p1.start(duty_cycle)

try:
    while True:
        duty_cycle = int(input())
        p1.start(duty_cycle)


finally:
    GPIO.output(gate, 0)
    GPIO.output(p, 0)
    GPIO.cleanup()