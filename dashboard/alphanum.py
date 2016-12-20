#!/usr/bin/python
# RetroDashboard AlphaNumeric Messages Driver
# @author khinds
# @license http://opensource.org/licenses/gpl-license.php GNU Public License

import time, json
import string, cgi, subprocess, json
from Adafruit_LED_Backpack import AlphaNum4

# Setup pins and initialize all the displays
display1 = AlphaNum4.AlphaNum4(address=0x77, busnum=1)
display2 = AlphaNum4.AlphaNum4(address=0x75, busnum=1)
display3 = AlphaNum4.AlphaNum4(address=0x73, busnum=1)
display4 = AlphaNum4.AlphaNum4(address=0x76, busnum=1)

# dashboard central server host
dashboardServer = 'MY-SERVER-HERE.com'

# how many times to scroll the message
showMessageCount = 3

# how many total alpha numeric characters you have in the scroll
numberLEDCharacters = 16

def initialize(display):
    """ start up the display with a the minimal brightness """
    display.begin()
    display.set_brightness(3)

def writeMessage(display, message):
    display.clear()
    display.print_str(message)
    display.write_display()

# prep displays and set brightness
initialize(display1)
initialize(display2)
initialize(display3)
initialize(display4)

def showNewMessage(message):
    '''Scroll a message across the display'''
    messageBuffer = numberLEDCharacters * " "
    message = messageBuffer + message.upper() + messageBuffer
    messageLength = len(message)
    showMessageIteration = 0
    pos = 0
    while (showMessageIteration < (showMessageCount * messageLength)):
        writeMessage(display1, message[pos:pos+4])
        writeMessage(display2, message[pos+4:pos+8])
        writeMessage(display3, message[pos+8:pos+12])
        writeMessage(display4, message[pos+12:pos+16])
        pos += 1
        showMessageIteration += 1
        if pos > len(message) - numberLEDCharacters:
            pos = 0
        time.sleep(0.175)

def showStaticMessage(message):
    '''show static waiting message'''
    writeMessage(display1, message[0:4])
    writeMessage(display2, message[4:8])
    writeMessage(display3, message[8:12])
    writeMessage(display4, message[12:16])

# Begin new phone notifications listener
currentMessage = ''
staticMessageCounter = 0
while True:

    try:
        phoneDashboardInfo = json.loads(unicode(subprocess.check_output(['curl', "http://" + dashboardServer + "/message"]), errors='ignore'))
        message = str(phoneDashboardInfo["message"])
        if (message != currentMessage):
            currentMessage = message
            showNewMessage(currentMessage)
        else:
            staticMessage = staticMessageCounter * " "
            staticMessage = staticMessage + "-"
            staticMessage = staticMessage + ((numberLEDCharacters - staticMessageCounter) * " ")
            showStaticMessage(staticMessage)
        staticMessageCounter += 1
        if (staticMessageCounter >= numberLEDCharacters):
            staticMessageCounter = 0
    except:
        pass
        
    time.sleep(2)
