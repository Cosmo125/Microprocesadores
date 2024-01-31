from machine import Pin, ADC, PWM
import time

# Configura el pin del potenciómetro
pot = ADC(Pin(33)) 
pot.atten(ADC.ATTN_11DB) # Para ESP32, permite leer hasta 3.3V

# Configura el pin del servo
servo_pin = Pin(5)
servo = PWM(servo_pin, freq=50)

print('go')
while True:
    pot_value = pot.read() # Lee valor del potenciómetro (0 a 4095)
    angle = pot_value / 4095 * 180 # Convierte el valor a un ángulo (0 a 180)
    print(angle)
    ton = (angle + 45) * 100000/9 #convertimo los angulos a frecuencia
    servo.duty_ns(int(ton)) #cambiamos la frecuencia de salida de PWM
