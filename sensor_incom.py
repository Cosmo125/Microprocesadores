#importo libreras
from machine import PWM, Pin
import time

#configuro pines
cont1 = Pin(19,Pin.OUT)#control direcion
cont2 = Pin(21,Pin.OUT)#control direccion
pwm = PWM(Pin(18))#velocidad
pwm.freq(1000)#frecuencia
sensor = Pin(5, Pin.IN) #sensor
#inicio motor

cont1.value(0)
cont2.value(0)

#programa principal
contador = 0
vueltas = 0

while True:
    #configuramos velocidad minima 0 maxima 1023
    pwm.duty(300)
    #configuramos direcion de velocidad
    cont1.value(0)
    cont2.value(1)
    if sensor.value() == 1:
        contador += 1
    if contador == 20:
        vueltas += 1
        contador = 0


    print(tiempo_transcurrido)
    
    
    
