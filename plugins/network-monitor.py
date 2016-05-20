#!/usr/bin/python
# Network Monitor plugin for the RetroDashboard
# @author khinds
# @license http://opensource.org/licenses/gpl-license.php GNU Public License
import time, subprocess, json, urllib2

# dashboard central server host
dashboardServer = 'MY-SERVER-HERE.com'

def sendHTTPPOST(readingValue, readingNumber):
    ''' for given reading integer value and which number to persist it as HTTP Post it to central hub '''
    req = urllib2.Request('http://'+dashboardServer+'/reading/'+readingNumber+'/set')
    req.add_header('Content-Type', 'application/json')
    urllib2.urlopen(req, json.dumps(readingValue))

# post network in / out in KBPS each 2 seconds to central hub
print 'network monitor has started...'
while True:

    # get local computer network stats from ifstat command
    networkInfo = str(subprocess.check_output(['ifstat', '1', '1']))
    networkInfo = networkInfo.replace("eth1", "")
    networkInfo = networkInfo.replace("wlan1", "")
    networkInfo = networkInfo.replace("tun0", "")
    networkInfo = networkInfo.replace("KB/s in", "")
    networkInfo = networkInfo.replace("KB/s out", "")
    networkInfo = networkInfo.split()

    # get the simple integer values and HTTP POST them to central hub
    sendHTTPPOST(int(round(float(networkInfo[0]))), '1')
    sendHTTPPOST(int(round(float(networkInfo[1]))), '2')
    
    # sleep for 2 seconds
    time.sleep(2)