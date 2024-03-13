from machine import Pin
import time
from hcsr04 import HCSR04

medidor1 = HCSR04(trigger_pin = 5, echo_pin = 18)

while  True:
    distancia = round(medidor1.distance_cm(),3)
    print(distancia)
    time.sleep(0.1)
