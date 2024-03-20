from machine import RTC, I2C, Pin
from ssd1306 import SSD1306_I2C
import time

print("Conectando ...")
oled = SSD1306_I2C(128, 64, I2C(0,scl=Pin(22), sda=Pin(21)))
oled.fill(0)
oled.text("Conectando ...", 0, 0)
oled.show()
time.sleep(2)


while True:
	print('led, prendido')
	oled.fill(0)
	oled.text('led, prendido',0,32)
	oled.show()
	time.sleep(2)
	print('led, apagado')
	oled.fill(0)
	oled.text('led, apagado',0,0)
	oled.show()
	time.sleep(2)
