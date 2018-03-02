#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# /home/pi/test.py

import os
import glob
import re
import sys
import datetime
import time
import commands
import subprocess
import smbus
import Adafruit_BMP.BMP085 as BMP085



from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT, UKR_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)



os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-1f653c126461')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#CELSIUS CALCULATION
def read_temp_c():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = int(temp_string) / 1000.0-1 # TEMP_STRING IS THE SENSOR OUTPUT, MAKE SURE IT'S AN INTEGER TO DO THE MATH
        temp_c = str(round(temp_c, 1)) # ROUND THE RESULT TO 1 PLACE AFTER THE DECIMAL, THEN CONVERT IT TO A STRING
        return temp_c

#FAHRENHEIT CALCULATION
sensor = BMP085.BMP085()



while(True):

    #lcd.cursor_pos = (0, 0)
    #lcd.write_string("Temp: " + read_temp_c() + unichr(223) + "C")
    #lcd.cursor_pos = (1, 0)
    #lcd.write_string("Temp: " + read_temp_f() + unichr(223) + "F")
	
	t = time.strftime("%H:%M")
	d = time.strftime("%d/%m/%Y")
	y = ("  Улица = " + read_temp_c() + " C")
	k = ('  Комната = {0:0.1f} C'.format(sensor.read_temperature()))
	#message = 'Temp: " + read_temp_c() + unichr(223) + "C'

	msg = (d)
        show_message(device, msg, fill="white", font=proportional(LCD_FONT))
        time.sleep(0)
	msg = (t)
        show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
        time.sleep(0)
	msg = (y)
        show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.04)
        time.sleep(0)
	msg = (k)
        show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
        time.sleep(0)		
		
for offset in range(8):
    virtual.set_position((offset, offset))