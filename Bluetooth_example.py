#importamos librerias necesarias
from machine import Pin
import bluetooth
from BLE import BLEUART #esta libreria se añade manualmente
import time

#configuramos el bluetooth
name = 'ESP32'
ble = bluetooth.BLE()
uart = BLEUART(ble,name)
 
#definimos funciones
def on_rx():
    #este comando lee lo que escribimos
    rx_buffer = uart.read().decode().strip()
    #berifica que lo que escribimos si es lo correcto
    uart.write('ESP32 says:' + str(rx_buffer)+"\n")
    #solo imprimimos
    if rx_buffer == 't':
        print('la temperatura es')
        uart.write('la temperatura es')
    if rx_buffer == 'hola':
        print('como estas')
        uart.write('la temperatura es')

#creamos otra funcion que en este caso es una alerta este recibe los parametros de temperatura
def warning(temp):
    #converte temp en un entero ya que recibe una cadena de caracteres
    temp = int(temp)
    #compara la temperatura
    if temp >= 100:
        uart.write('alerta')
        print('alerta')
#inicia el codigo, con una lectura de funcion, esta lo unico que hace es que si lee algo del dispositivo usa la funcion on_rx
uart.irq(handler=on_rx)
#este while solo es el conparador de la funcion
while True:
    temp = input("cual es la temperatura: ")
    warning(temp)
    time.sleep(1)
    
    
