#importo libreras
from machine import PWM, Pin, Timer
import time

#configuro pines
cont1 = Pin(19,Pin.OUT)#control direcion
cont2 = Pin(21,Pin.OUT)#control direccion
pwm = PWM(Pin(18))#velocidad
pwm.freq(1000)#frecuencia
sensor = Pin(13, Pin.IN) #sensor
#inicio motor

cont1.value(0)
cont2.value(0)

#programa principal
contador = 0
vueltas = 0
rps = 0
timer = Timer(0)


def contar(pin):
    global contador
    global vueltas
    contador += 1
    
    if contador == 20:
        vueltas += 1
        contador = 0
    
def rps(timer):
    global vueltas, rps
    rps = vueltas
    vueltas = 0
    print(rps)
    
sensor.irq(handler = contar, trigger = Pin.IRQ_FALLING)
timer.init(period=1000, mode=Timer.PERIODIC, callback=rps)

while True:
    #configuramos velocidad minima 0 maxima 1023
    pwm.duty(300)
    #configuramos direcion de velocidad
    cont1.value(0)
    cont2.value(1)

    



    
    
    
