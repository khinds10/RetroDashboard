#DashboardPI - Retro Display Dashboard
![Final Construction](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/6-final.jpg "Final Construction")

####Flashing RaspberriPi Hard Disk / Install Required Software (Using Ubuntu Linux)

Download "RASPBIAN JESSIE LITE"
https://www.raspberrypi.org/downloads/raspbian/

**Create your new hard disk for DashboardPI**
>Insert the microSD to your computer via USB adapter and create the disk image using the `dd` command
>
> Locate your inserted microSD card via the `df -h` command, unmount it and create the disk image with the disk copy `dd` command
> 
> $ `df -h`
> */dev/sdb1       7.4G   32K  7.4G   1% /media/XXX/1234-5678*
> 
> $ `umount /dev/sdb1`
> 
> **Caution: be sure the command is completely accurate, you can damage other disks with this command**
> 
> *if=location of RASPBIAN JESSIE LITE image file*
> *of=location of your microSD card*
> 
> $ `sudo dd bs=4M if=/path/to/raspbian-jessie-lite.img of=/dev/sdb`
> *(note: in this case, it's /dev/sdb, /dev/sdb1 was an existing factory partition on the microSD)*

**Setting up your RaspberriPi**

*Insert your new microSD card to the raspberrypi and power it on with a monitor connected to the HDMI port*

Login
> user: **pi**
> pass: **raspberry**

Change your account password for security
>`sudo passwd pi`

Enable RaspberriPi Advanced Options
>`sudo raspi-config`

Choose:
`1 Expand File System`

`9 Advanced Options`
>`A2 Hostname`
>*change it to "DashboardPI"*
>
>`A4 SSH`
>*Enable SSH Server*
>
>`A7 I2C`
>*Enable i2c interface*

**Enable the English/US Keyboard**

>`sudo nano /etc/default/keyboard`

> Change the following line:
>`XKBLAYOUT="us"`

**Reboot PI for Keyboard layout changes / file system resizing to take effect**
>$ `sudo shutdown -r now`

**Auto-Connect to your WiFi**

>`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

Add the following lines to have your raspberrypi automatically connect to your home WiFi
*(if your wireless network is named "linksys" for example, in the following example)*

	network={
	   ssid="linksys"
	   psk="WIRELESS PASSWORD HERE"
	}

**Reboot PI to connect to WiFi network**

>$ `sudo shutdown -r now`
>
>Now that your PI is finally on the local network, you can login remotely to it via SSH.
>But first you need to get the IP address it currently has.
>
>$ `ifconfig`
>*Look for "inet addr: 192.168.XXX.XXX" in the following command's output for your PI's IP Address*

**Go to another machine and login to your raspberrypi via ssh**

> $ `ssh pi@192.168.XXX.XXX`

**Start Installing required packages**

>$ `sudo apt-get update`
>
>$ `sudo apt-get install vim git python-smbus i2c-tools python-imaging python-smbus build-essential python-dev rpi.gpio python3 python3-pip`

**Setup the simple directory `l` command [optional]**

>`vi ~/.bashrc`
>
>*add the following line:*
>`alias l='ls -lh'`
>`source ~/.bashrc`

**Install i2c Backpack Python Drivers**

>$ `git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack`

>$ `cd Adafruit_Python_LED_Backpack/`

>$ `sudo python setup.py install`

#Supplies Needed

Raspberry PI 2

0.56" 4-Digit 7-Segment Display w/I2C Backpack (x4)

![7 Segment Display](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/7-segment.jpg "7 Segment Display")

Quad Alphanumeric Display - 0.54" Digits w/ I2C Backpack (x4)

![14 Segment Display](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/14-segment.jpg "14 Segment Display")

LED Lights (x4)

![LED Lights](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/led.jpg "LED Lights")

Wooden Keepsake Box

![Keepsake Box](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/keepsake.jpg "Keepsake Box")

Hook and Eye

![Hook and Eye](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/hook-and-eye.jpg "Hook and Eye")

Dremel Tool with small saw blade

Black Spray Paint

#Building the Dashboard

##1) Measure and Cut
Measure and cut one long 4 - 14 segment display long hole near the top, 4 - 7 segment display individual holes in a square pattern and 4 LED sized holes in the lid of the wooden box.  I used a dremel tool with small saw for the square hole cuts and a regular drill for the LED holes.
![Measure and Cut](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/1-measure-cut.jpg "Measure and Cut")

##2) Solder Unique Display Jumpers
*NOTE: All the I2C backpacks must be soldered on the back of each of the displays, the backpacks come with the display and must all be soldered on first.*

For each of the I2C backpack displays you must solder the jumpers on the back in the **all the possible combinations** to have your RaspberriPI I2C interface to recognize each display with a **unique address**.  

Leave the first display with no jumper soldered, the 2nd with the farthest right soldered, the 3rd with only the middle soldered and so on...  Eventually you'll have to solder jumpers in all the combinations of 2 at a time connected and the final display with all 3 jumpers soldered to be connected.

*There's a total of 3 pins so you should have a total combination of 8 unique combinations.*

![Solder Unique Display Jumpers](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/2-displays.jpg "Solder Unique Display Jumpers")

##3) Mount Displays in box
Using a hot glue gun, mount the displays in the holes and glue them in place.  The LED lights may hold by friction if you drilled just the right sized hole, else use hot glue to hold them in place as well.
![Mount Displays](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/3-mount.jpg "Mount Displays")

**NOTE: I have written down on the back of the box cover the HEX addresses x70 - x77 that each display has based on the soldering jumpers (see section #2)**

##4) Cut RaspberryPI Access hole / glue in place
Using the Dremel tool like I did or a small saw, cut a hole in the right side of the wooden box, closest to the back of the box.  Place the RaspberryPI with the USB connectors facing out next to the hole so they're accessible after you've closed the box, and hot glue the RaspberryPI in place.
![Glue Raspberry PI](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/4-raspberry-pi.jpg "Glue Raspberry PI")

##5) Wiring all Displays

Each of the 14 segment alpha numeric displays needs to have a connection to the RaspberryPI GND, 5V and 3V pins.  The 7 segment display only needs connectivity to the GND and 5V pins.  

![Wiring Diagram](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/wiring-diagram.png "Wiring Diagram")

I've used standard jumper wires to connect to all the pins on the display / RaspberryPI pins and grouped the common connections (all the GND wires, 5V wires) with a wirenut.

Each LED light needs to have a 270 ohm resister solder to the ground (short) pin and connect each positive LED pin to the corresponding GPIO pins on the PI, I've used GPIO pins 18, 13, 15 and 16.

For each display in the dashboard ALL of the D and C pins need to be connected to the SCL and SDA pins on the PI.

![Wire all Displays](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/5-wire.jpg "Wire all Displays")

##6) Finished (Final Touches)

**Add a hook and eye to close the box on the top**

![Hook on Top](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/hook-on-top.jpg "Hook on Top")

**Cut a hole for the USB power cable to enter the box and power the RaspberryPI**

*Note: because this has external USB ports, this dashboard doubles as a charging station for other devices as well!*

![Power and Charging](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/power-and-charging.jpg "Power and Charging")


You're now ready to run the Dashboard!

![Finished](https://raw.githubusercontent.com/khinds10/RetroDashboard/master/construction/6-final.jpg "Finished")

##7) Install Central Webhost 
This project includes a small PHP server that you can host on almost any low cost linux webhost.  From this project copy the files from the "server/" folder and place them on your PHP webhost and remember the domain name.  
> For our example it will be installed on a hypothetical host with the public domain name of: www.mydashboard.com

The **server/README.md** file contains all the details about how to get/set message values, measurement values and flag values to the PHP server.  These values will then be listened for on the Retrodashboard to display to you as output via the alphanumeric / numeric and led lights turning on and off.


##8) Install & Run Dashboard Drivers

Start up your RaspberryPi and make sure the I2C bus recognizes all your connected 7/14 segment displays. 
*[each display is given a unique address described above by how you solder each display's jumpers in different combinations]*  

If you have all 8 displays with jumpers soldered in all 8 combinations, you should have the following output for the `i2cdetect` command:

`sudo i2cdetect -y 1`
     
>    0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
>     
> 00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
> 
> 10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
> 
> 20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
> 
> 30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
> 
> 40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
> 
> 50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
> 
> 60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
> 
> 70: 70 71 72 73 74 75 76 77   


*(in this case all the displays numbered 0 to 7 are being recognized on the PI as I2C available devices)*

**Install all 3 python driver scripts from this project (in the dashboard/ folder) to your home directory of the RaspberryPI. **
So your PI has the following home directory files:

`cd ~`
`ls -lh`

    -rwxrwxr-x 1 pi pi 2.8K May 21 01:56 alphanum.py
    -rwxrwxr-x 1 pi pi 2.2K May 21 01:54 dashboard.py
    -rwxrwxr-x 1 pi pi 1.4K May 21 02:36 indicators.py


Edit each python scripts variable to reference your running PHP data server (see Step 7)

	dashboardServer = 'CHANGE TO YOUR SERVER.com'

**alphanum.py**

*Change the python code to reflect the HEX addresses each display is assigned based on the solder jumpers (see section #2)*

	display1 = AlphaNum4.AlphaNum4(address=0x77, busnum=1)
	display2 = AlphaNum4.AlphaNum4(address=0x76, busnum=1)
	display3 = AlphaNum4.AlphaNum4(address=0x75, busnum=1)
	display4 = AlphaNum4.AlphaNum4(address=0x73, busnum=1)
	
**dashboard.py**

*Change the python code to reflect the HEX addresses each display is assigned based on the solder jumpers (see section #2)*

	blueDisplay = SevenSegment.SevenSegment(address=0x70, busnum=1) 
	yellowDisplay = SevenSegment.SevenSegment(address=0x71, busnum=1) 
	greenDisplay = SevenSegment.SevenSegment(address=0x72, busnum=1) 
	redDisplay = SevenSegment.SevenSegment(address=0x74, busnum=1)
	
**indicators.py**

*Change the python code to reflect the GPIO pin numbers each LED is assigned based on your exact wiring (I've used GPIO pins: 13,15,16,18)

	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18,GPIO.LOW)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13,GPIO.LOW)
	GPIO.setup(15, GPIO.OUT)
	GPIO.output(15,GPIO.LOW)
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16,GPIO.LOW)

Now that your 3 scripts are pointing to your own data server you're now ready to run the dashboard to display your output.

Run the following commands to start your Dashboard displays.

$  `nohup python indicators.py > indicators.out &`

$  `nohup python dashboard.py > dashboard.out &`

$  `nohup python alphanum.py > alphanum.out &`

This will allow you to logout of your PI and have the python drivers remain running as a background process, if they do fail for any reason, the error message will be found in the [.out] from the commands above.

##9) Running Plugins for Populating Display Data

####(These plugins run on different machines of your choosing for the dashboard to then monitor them)

The **'plugins/'** folder contains plugins to get started populating the central server with information that the dashboard will display as output.  

**network-monitor.py**

*This plugin will persist to the central data hub local network information such as your current upload and download speed in KBPS.*

**Software Requirements:**

ifstat is required

	sudo apt-get install ifstat

Configure and run the script:

	dashboardServer = 'CHANGE TO YOUR SERVER.com'

$  `nohup python network-monitor.py > network-monitor.out &`

**server-monitor.py**

*This plugin will persist to the central data hub local CPU usage and temperature statistics.*

**Software Requirements:**

psensor-server is required

	sudo apt-get install psensor-server

Configure the script:

	dashboardServer = 'CHANGE TO YOUR SERVER.com'

Run pensor server on port 17510, then run the server monitor script:

$ `nohup psensor-server -p 17510 > /dev/null 2>&1`

$  `nohup python server-monitor.py > server-monitor.out &`


**DashboardPhone/**

*This is a fully functional Android App that runs on your phone as a service and will persist to the central data hub notifications and indicator flags (coming soon).*

**Configure the App**
You need to update the settings.java file with your local settings

		// host with the PHP server script installed for the RetroDashboard
		public static String remoteDashboardHost = "CHANGE TO YOUR SERVER.com";
	
		// create a list of notifications (by title) your phone always produces but don't need to broadcast
		public static String[] ignoredNotifications = new String[] { "Privacy Guard active", "Change keyboard" };

**Build the App**

Using an Android IDE, import the project locally and build it to an APK file.  Install the APK on your phone locally and it should start working for you.

