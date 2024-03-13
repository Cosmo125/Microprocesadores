#Insertamso las librerias de trabajo
from machine import Pin
#libreria para el tiempo
import time

# Reemplaza 'pin_number' con el número del pin GPIO que estás usando
pin_number = 4

# Configura el pin como salida
led = Pin(pin_number, Pin.OUT)

#variable de trabajo
var = 0

while True:
    #pregunta sobre estadp
    var = int(input())
    #actua el estado
    if var == 1:
        led.value(1)
    else:
        led.value(0)
