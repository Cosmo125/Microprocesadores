#Importar librerias nuevas
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

#creamos el objeto de pantalla
I2C_ADDr = 0x27 #canal de la pantalla
#tamaño de la pantalla
Rows = 2
Columns = 16
#configuracion de la pantalla
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDr, Rows, Columns)

#inicio de mensaje
while True:
	lcd.putstr("HOLA MUNDO.......")
	time.sleep(2)
	lcd.clear()
