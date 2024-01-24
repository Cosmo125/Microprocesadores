#Insertamso las librerias de trabajo
from machine import Pin
#libreria para el tiempo
import time

# Reemplaza 'pin_number' con el número del pin GPIO que estás usando
red = 2
blue = 0
green = 4

# Configura el pin como salida
led1 = Pin(red, Pin.OUT)
led2 = Pin(blue, Pin.OUT)
led3 = Pin(green, Pin.OUT)


# Enciende el LED rojo
led1.value(1)
# Espera 2 segundo
time.sleep(2)
# Enciende LED azul
led2.value(1)
# Espera 2 segundo
time.sleep(2)
#Enciende LED verde
led3.value(1)
# Espera 2 segundo
time.sleep(2)


# Apaga el LED
led1.value(0)
led2.value(0)
led3.value(0)
