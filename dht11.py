from machine import Pin
import time
from dht import DHT11

dht11 = DHT11(Pin(5))

while  True:
    time.sleep(1)
    dht11.measure()
    temp = dht11.temperature()
    hum = dht11.humidity()
    print('T = {:02d} C, h={:02d}%'.format(temp,hum))
    from machine import Pin
import time
from dht import DHT11

dht11 = DHT11(Pin(5))

while  True:
    time.sleep(1)
    dht11.measure()
    temp = dht11.temperature()
    hum = dht11.humidity()
    print('T = {:02d} C, h={:02d}%'.format(temp,hum))
    
