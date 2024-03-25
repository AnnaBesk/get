import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

try:
    while (True): 
        x = input()
        if x != 'q':
            x = float(x)

            if x.is_integer() is False:
                print('Введено не целое')
                continue
            x = int(x)
            if x < 0:
                print('Отрицательное значение')
                continue
            elif x >= 256:
                print('Невозможно показать число')
                continue
            GPIO.output(dac, decimal2binary(x))

            # расчет напряжения
            U = 3.3
            u_1 = U / (2 ** 8 - 1)
            print(x * u_1)
        else:
            break

except ValueError:
    print('Введено не число')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

