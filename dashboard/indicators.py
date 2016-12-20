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
GPIO.setup(18, GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13,GPIO.LOW)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15,GPIO.LOW)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16,GPIO.LOW)

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
        setLight(13, int(flagsInfo['message'][0]))
        setLight(15, int(flagsInfo['message'][1]))
        setLight(16, int(flagsInfo['message'][2]))
        setLight(18, int(flagsInfo['message'][3]))
        time.sleep(2)
    except:
        setLight(13, 0)
        setLight(15, 0)
        setLight(16, 0)
        setLight(18, 0)
        time.sleep(2)
