from machine import Pin, ADC, PWM
import time

# Configura el pin del potenciómetro
pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB) # Configura la atenuación para un rango completo de 0 a 3.3V

# Configura el pin del LED
led1 = Pin(21, Pin.OUT)
led2 = Pin(17, Pin.OUT)
led3 = Pin(2, Pin.OUT)

print('go')
while True:
    pot_value = pot.read() # Lee el valor del potenciómetro
    print(pot_value) # Mostramos en Pantalla el valor dle potenciómetro
    if pot_value >= 1365 and pot_value <= 2730:   #delimitamos la prendida del leds entre dos rangos 
        led1.value(1)
    elif pot_value >= 2730 and pot_value <= 4092: #delimitamos la prendida del leds entre dos rangos 
        led1.value(1)
        led2.value(1)
    elif pot_value >= 4092: #delimitamos la prendida del leds para rangos mayores a 4092
        led1.value(1)
        led2.value(1)
        led3.value(1)
    else:  
        led1.value(0)
        led2.value(0)
        led3.value(0)  
    time.sleep(0.1)  
