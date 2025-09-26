#Insertamso las librerias de trabajo
from machine import Pin
#libreria para el tiempo
import time

#Asignacion de variables
red = 2
bot = 13

#Asignacion de salidas y entradas 
led = Pin(red, Pin.OUT)
boton = Pin(bot, Pin.IN, Pin.PULL_DOWN)

#inicio e sistema
print("GO")

#inicia un bucle para que se repita
while True:

    #Inicio de las sentencias de pregunta
    if boton.value() == 1:
        led.value(1)
    else:
        led.value(0)
        
    #esperamos un tiempo para evitar rebotes
    time.sleep(0.1)
