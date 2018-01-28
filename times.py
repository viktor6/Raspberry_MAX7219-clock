#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Copyright (c) 2017-18 Richard Hull and contributors 
# See LICENSE.rst for details. 

import re
import sys
import datetime
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)

while(True):
	    msg = time.strftime("%d-%m-%Y %H:%M")
	    show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
        time.sleep(1)

for offset in range(8):
    virtual.set_position((offset, offset))
