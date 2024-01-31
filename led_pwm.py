from machine import Pin,PWM
import time

#Asignamos los pines del pwm
led_pin = 2
led = PWM(led_pin, freq=1000) #frecuencia de trabajo para el led

print('go')

#inicilo del programa
while True:
    #Cambio de potencia del led en subida
    for b in range(0, 1023, 15):
        led.duty(b)
        time.sleep_ms(10) #espera 10 mili segundos
    #Cambio de potencia del led en bajada
    for b in range(1023, 0, -15):
        led.duty(b)
        time.sleep_ms(10)#espera 10 mili segundos 
