#Insertamso las librerias de trabajo
from machine import Pin
#libreria para el tiempo
import time

# Reemplaza 'pin_number' con el número del pin GPIO que estás usando
pin_number = 2

# Configura el pin como salida
led = Pin(pin_number, Pin.OUT)

while True:
    # Enciende el LED
    led.value(1)
    # Espera un segundo
    time.sleep(1)
    # Apaga el LED
    led.value(0)
    # Espera un segundo
    time.sleep(1)
