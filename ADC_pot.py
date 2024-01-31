from machine import Pin, ADC
import time

# Configura el pin del potenciómetro
pot = ADC(Pin(34)) # Asume que el potenciómetro está conectado al pin 34

while True:
    pot_value = pot.read() # Lee el valor del potenciómetro
    print("Valor del potenciómetro:", pot_value)
    time.sleep(0.5) # Pequeña pausa para facilitar la lectura de los valores

