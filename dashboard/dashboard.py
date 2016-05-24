#!/usr/bin/python
# RetroDashboard Numeric Messages Driver
# @author khinds
# @license http://opensource.org/licenses/gpl-license.php GNU Public License

import time, json
import string, cgi, subprocess, json
from Adafruit_LED_Backpack import SevenSegment

# setup the displays by colors
blueDisplay = SevenSegment.SevenSegment(address=0x70, busnum=1) 
yellowDisplay = SevenSegment.SevenSegment(address=0x71, busnum=1) 
greenDisplay = SevenSegment.SevenSegment(address=0x72, busnum=1) 
redDisplay = SevenSegment.SevenSegment(address=0x74, busnum=1)
blinkDecimal = True

# dashboard central server host
dashboardServer = 'MY-SERVER-HERE.com'

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

def setToError(display):
    """ set the display to error state """
    display.clear()
    display.print_number_str("----", 0)
    display.write_display()

# initialize the displays
initialize(greenDisplay)
initialize(redDisplay)
initialize(yellowDisplay)
initialize(blueDisplay)

# start the dashboard
while(True):
    try:

        # get all 4 readings
        readingsInfo = json.loads(subprocess.check_output(['curl', "http://" + dashboardServer + "/reading/all"]))
        setReadingValue(yellowDisplay, int(readingsInfo['message'][0]), blinkDecimal)
        setReadingValue(blueDisplay, int(readingsInfo['message'][1]), blinkDecimal)
        setReadingValue(redDisplay, int(readingsInfo['message'][2]), blinkDecimal)
        setReadingValue(greenDisplay, int(readingsInfo['message'][3]), blinkDecimal)

        # invert the decimal blinking value and wait 2 seconds
        blinkDecimal = not blinkDecimal
        time.sleep(1)

    except:
        # show the error state on the dashboard displays  
        setToError(yellowDisplay)
        setToError(blueDisplay)
        setToError(redDisplay)
        setToError(greenDisplay)        
        time.sleep(2)
