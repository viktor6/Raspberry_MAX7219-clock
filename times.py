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



def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()
 
    return int(mytemp[1])
 
  except:
    return 99999
 
if __name__ == '__main__':
 
  # Script has been called directly
  id = '28-5ee327126461'
  #print "Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))

#FAHRENHEIT CALCULATION
sensor = BMP085.BMP085()



while(True):

    #lcd.cursor_pos = (0, 0)
    #lcd.write_string("Temp: " + read_temp_c() + unichr(223) + "C")
    #lcd.cursor_pos = (1, 0)
    #lcd.write_string("Temp: " + read_temp_f() + unichr(223) + "F")
	
	t = time.strftime("%H:%M")
	d = time.strftime("%d/%m/%Y")
	y = ("  Улица = " + '{:.1f} C'.format(gettemp(id)/float(1000)))
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