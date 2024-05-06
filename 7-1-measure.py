import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

# устанавливаем настройки входов
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

comp = 14
troyka = 13

levels = 2 ** 8 - 1
maxVol = 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

# функция перевода из 10 в двоичную для отображения на светодиодах
def decimal2binary(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

# поразрядное считывание напряжения
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
    return val

data = [] # массив, в котором будем хранить данные

try:
    begin = time.time() # засекаем время начала
    # в цикле сохраняем значения на конденсаторе
    while (True):
        val = adc()
        print(val)
        if val >= 110:
            break
        elif val == 0:
            GPIO.output(leds, 0)
            data.append(str(val))
        elif not type(val):
            GPIO.output(leds, 1)
        else:
            GPIO.output(leds, decimal2binary(val))
            data.append(str(val))
    
    # достигнув макс значения перестаем подавать напряжение
    GPIO.output(troyka, 0)

    # вычисляем длительность эксперимента
    end = time.time()
    dur = end - begin

    per = dur / len(data) # вычисляем период
    vol = maxVol / levels # вычисляем шаг измерения

    # производим записать данных в файл
    with open("data.txt", "w") as DS:
        DS.write("\n".join(data))

    # записываем параметры эксперимента
    set = [dur, per, (1 / per), vol]
    with open("settings.txt", "w") as set:
        set.write("\n".join([str(1/per), str(vol)])) 

    print(dur, "длительность эксперимента")
    print(per, "период измерения")
    print(1 / per, "средняя частота дискретизации")
    print(vol, "шаг квантования")
    for i in range(len(data)):
        data[i] = int(data[i])
    plt.plot(data)
    plt.show()
    print('Finish')
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
