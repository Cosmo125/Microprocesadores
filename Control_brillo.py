from machine import Pin, ADC, PWM
import time

# Configura el pin del potenciómetro
pot = ADC(Pin(34)) # Asume que el potenciómetro está conectado al pin 34
pot.atten(ADC.ATTN_11DB) # Configura la atenuación para un rango completo de 0 a 3.3V

# Configura el pin del LED
led = PWM(Pin(2)) # Asume que el LED está conectado al pin 5
led.freq(1000) # Configura la frecuencia de PWM
print('go')
while True:
    pot_value = pot.read() # Lee el valor del potenciómetro
    led_duty = int(pot_value / 4095 * 1023) # Convierte el valor a un rango adecuado para el LED
    led.duty(led_duty) # Establece el ciclo de trabajo del LED
    time.sleep(0.1) # Pequeña pausa para estabilidad
