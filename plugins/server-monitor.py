#!/usr/bin/python
# Server Monitor plugin for the RetroDashboard
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

# post server cpu percentage / core tempurature (*f) each 2 seconds to central hub
print 'server monitor has started...'
while True:
    try:
        # gather server stats and display any errors
        process = subprocess.Popen("ps -ef | grep psensor-server | grep -v grep", shell=True, stdout=subprocess.PIPE)
        stdout_list = process.communicate()[0].split('\n')
        if not stdout_list[0]:
            print "[PLEASE RUN] $ nohup psensor-server -p 17510 > /dev/null 2>&1"
            exit()

        # get CPU tempurature info from the local psensor server
        tempInfo = json.loads(subprocess.check_output(['curl', 'http://localhost:17510/api/1.1/sensors']))
        temp = (tempInfo[0]["last_measure"]["value"] * 1.8) + 32;
        temp = int(round(temp, 0))

        # get the current CPU load in percentage from the local psensor server
        systemInfo = json.loads(subprocess.check_output(['curl', 'http://localhost:17510/api/1.1/sysinfo']))
        cpu = systemInfo["load"] * 100;
        cpu = int(round(cpu, 0))

        # get the simple integer values and HTTP POST them to central hub
        sendHTTPPOST(temp, '3')
        sendHTTPPOST(cpu, '4')

    except:
        pass

    # sleep for 2 seconds
    time.sleep(2)

