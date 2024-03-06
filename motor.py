#importo libreras
from machine import PWM, Pin

#configuro pines
cont1 = Pin(19,Pin.OUT)
cont2 = Pin(21,Pin.OUT)
pwm = PWM(Pin(18))
pwm.freq(1000)

#inicio motor

cont1.value(0)
cont2.value(0)

#programa principal

while True:
    #configuramos velocidad minima 0 maxima 1023
    pwm.duty(300)
    #configuramos direcion de velocidad
    cont1.value(0)
    cont2.value(1)
