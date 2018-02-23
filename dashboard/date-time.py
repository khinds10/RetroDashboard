#!/usr/bin/python
# RetroDashboard Numeric Messages Driver
# @author khinds
# @license http://opensource.org/licenses/gpl-license.php GNU Public License

import time, json
import string, cgi, subprocess, json, datetime
from Adafruit_LED_Backpack import SevenSegment

# setup the displays by colors
yellowDisplay = SevenSegment.SevenSegment(address=0x71, busnum=1) 
redDisplay = SevenSegment.SevenSegment(address=0x74, busnum=1)
blinkDecimal = True

# dashboard central server host
#dashboardServer = 'MY-SERVER-HERE.com'

def initialize(display):
    """ start up the display with a the minimal brightness """
    display.begin()
    display.set_brightness(3)

def setReadingValue(display, reading, blinkDecimal):
    """ set the reading to the display in question and blink the decimal """
    display.clear()
    display.print_float(reading, 0)
    display.set_decimal(3, blinkDecimal)
    display.write_display()
    
    
def setStringValue(display, value, blinkDecimal, showColon):
    """ set the reading to the display in question and blink the decimal """
    display.clear()
    display.print_number_str(value, 0)
    display.set_decimal(3, blinkDecimal)
    
    if showColon:
        display.set_colon(True)
    display.write_display()

def setToError(display):
    """ set the display to error state """
    display.clear()
    display.print_number_str("----", 0)
    display.write_display()

# initialize the displays
initialize(redDisplay)
initialize(yellowDisplay)

# start the dashboard
while(True):
    try:

        d = datetime.datetime.now()
        setStringValue(redDisplay, d.strftime("%I%M"), blinkDecimal, True)
        setStringValue(yellowDisplay, d.strftime("%m%d"), blinkDecimal, False)

        # invert the decimal blinking value and wait 2 seconds
        blinkDecimal = not blinkDecimal
        time.sleep(1)

    except:
    
        # show the error state on the dashboard displays  
        setToError(yellowDisplay)
        setToError(redDisplay)
        time.sleep(2)
