#!/usr/bin/python
# RetroDashboard Indicator Lights Driver
# @author khinds
# @license http://opensource.org/licenses/gpl-license.php GNU Public License

import time, json
import string, cgi, subprocess, json
import RPi.GPIO as GPIO  

# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)
 
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

# dashboard central server host
dashboardServer = 'MY-SERVER-HERE.com'

def setLight(pin, isLit):
    """ set light to on or off based on boolean value """
    if isLit:
        GPIO.output(pin,GPIO.HIGH)
    else:
        GPIO.output(pin,GPIO.LOW)

while(True):
    try:
        # get all 4 flag set values and set the lights to on or off accordingly
        flagsInfo = json.loads(subprocess.check_output(['curl', "http://" + dashboardServer + "/flag/all"]))
	    setLight(11, int(flagsInfo[0]))
	    setLight(13, int(flagsInfo[1]))
	    setLight(15, int(flagsInfo[2]))
	    setLight(16, int(flagsInfo[3]))
        sleep(2)
    except:
	    setLight(11, 0)
	    setLight(13, 0)
	    setLight(15, 0)
	    setLight(16, 0)
        sleep(2)
