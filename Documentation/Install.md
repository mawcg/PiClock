# Install Instructions for HamClock 
## For Raspbian Jessie 

HamClock and this install guide are based on Raspian Jessie
released on https://www.raspberrypi.org/downloads/ It will work with many
raspbian versions, but you may have to add more packages, etc.  That exercise
is left for the reader.

What follows is a step by step guide.  If you start with a new clean raspbian
image, it should just work. I'm assuming that you already know how to hook
up your Raspi, monitor, and keyboard/mouse.   If not, please do a web search
regarding setting up the basic hardware for your Raspi.
 
### Download Raspbian Jessie and put it on an SD Card

The image and instructions for doing this are on the following page:
https://www.raspberrypi.org/downloads/  

### First boot and configure
A keyboard and mouse are really handy at this point.
When you first boot your Pi, you'll be presented with the desktop.
Navigate to Menu->Preferences->Raspberry Pi Configuration.
Just change the Items below.
 - General Tab
  - Change User Password -- this will set the password for the use pi,
     for ssh logins.
  - Hostname: (Maybe set this to HamClock?)
  - Boot: To Desktop
  - Auto Login: Checked
  - Underscan: (Initally leave as default, but if your monitor has extra black area on the border, or bleeds off the edge, then change this)
 - Interfaces
  - 1-Wire Enable (for the inside temperature, DS18B20 if you're using it)
 - Internationalization Tab
   - Set Locale.
    - Set Language  -- if you set language and country here, the date will automaticly be in your language
    				-- other settings in Config.py (described later) control the language of the weather data
    - Set Country
    - Character Set: UTF-8
  - Set Timezone.
    -  You'll want this to be correct, or the clock will be wrong.
  - Set Keyboard
    -  Generally not needed, but good to check if you like the default
  - Set WiFi Country (may not always show up)

Finish and let it reboot.

I've found that sometimes on reboot, Jessie doesn't go back to desktop mode.  
If this is the case, 
```
sudo raspi-config
``` 
and change the boot option to Desktop/Auto-login

### editing config.txt

Log into your Pi, (either on the screen or via ssh)

reboot
```
sudo reboot
```

### Get connected to the internet

Either connect to your wired network, or setup wifi and verify you have
internet access from the Pi

```
ping github.com
```
(remember ctrl-c aborts programs, like breaking out of ping, which will
go on forever)

### Get all the software that HamClock needs.

Become super user! (root)  
```
sudo su -
```
update the repository
```
apt-get update
```
then get qt4 for python
```
apt-get install python-qt4
```
you may need to confirm some things, like:
After this operation, 44.4 MB of additional disk space will be used.
Do you want to continue [Y/n]? y
Go ahead, say yes

then get libboost for python (optional for the NeoPixel LED Driver)
```
apt-get install libboost-python1.49.0
```

then get unclutter (disables the mouse pointer when there's no activity)
```
apt-get install unclutter
```

### reboot
To get some things running, and ensure the final config is right, we'll do
a reboot
```
reboot
```

### Get the HamClock software
Log into your Pi, (either on the screen or via ssh) (NOT as root)
You'll be in the home directory of the user pi (/home/pi) by default,
and this is where we want to be.
```
git clone https://github.com/mawcg/PiClock.git
```
Once that is done, you'll have a new directory called HamClock

### Install gps python module
sudo apt-get install python-gps

### Configure the HamClock api keys

The first is to set API keys for Weather Underground and Google Maps.  
These are both free, unless you have large volume.
The HamClock usage is well below the maximums  imposed by the free api keys.

Weather Underground api keys are created at this link: 
http://www.wunderground.com/weather/api/ Here too, it'll ask you for an
Application (maybe HamClock?) that you're using the api key with.

## Optional Google Maps API key

A Google Maps api key is _not required_, unless you pull a large volume of maps.
Most everyone can leave this key empty.  

You only need a key if you're continually pulling maps because you're restarting
the clock often durning development.   The maps are pulled once at the start.

If you want a key, this is how its done. Google Maps api keys are created at this link:
https://console.developers.google.com/flows/enableapi?apiid=maps_backend&keyType=CLIENT_SIDE
You'll require a google user and password.  After that it'll require
you create a "project" (maybe HamClock for a project name?)
It will also ask about Client Ids, which you can skip (just clock ok/create).  You need to 
then activate the key.



Now that you have your api keys...

```
cd HamClock
cd Clock
cp ApiKeys-example.py ApiKeys.py
nano ApiKeys.py
```
Put your api keys in the file as indicated
```
#change this to your API keys
# Weather Underground API key
wuapi = 'YOUR WEATHER UNDERGROUND API KEY'
# Google Maps API key
googleapi = ''  #Empty string, the key is optional -- if you pull a small volume, you'll be ok
```

### Configure your HamClock
here's were you tell HamClock where your weather should come from, and the
radar map centers and markers. 

```
cd HamClock
cd Clock
cp Config-Example.py Config.py
nano Config.py
```

This file is a python script, subject to python rules and syntax.
The configuration is a set of variables, objects and arrays,
set up in python syntax.  The positioning of the {} and () and ','
are not arbitrary.  If you're not familiar with python, use extra
care not to disturb the format while changing the data.

The first thing is to change the primary_coordinates to yours.  That is really
all that is manditory.  Further customization of the radar maps can be done in
the Radar section.  There you can customize where your radar images are centered
and where the markers appear on those images.  Markers are those little red
location pointers.  Radar1 and 2 show on the first page, and 3 and 4 show on the
second page of the display (here's a post of about that:
https://www.facebook.com/permalink.php?story_fbid=1371576642857593&id=946361588712436&substory_index=0 )

### Run it!
You'll need to be on the desktop, in a terminal program.

```
cd HamClock
sh startup.sh -n -s
```
Your screen should be covered by the HamClock 

There will be some output on the terminal screen as startup.sh executes.
If everything works, it can be ignored.  If for some reason the clock
doesn't work, or maps are missing, etc the output may give a reason
or reasons, which usually reference something to do with the config
file (Config.py)  

### Logs
The -s option causes no log files to be created, but
instead logs to your terminal screen.  If -s is omitted, logs are
created in HamClock/Clock as PyQtHamClock.[1-7].log, which can also help
you find issues.  -s is normally omitted when started from the desktop icon
or from crontab.  Logs are then created for debugging auto starts.

### First Use

  * The space bar or right or left arrows will change the page.
  * F2 will start and stop the NOAA weather radio stream
  * F4 will close the clock
  
If you're using the temperature feature AND you have multiple temperature sensors,
you'll see the clock display: 000000283872:74.6 00000023489:65.4 or something similar.
Note the numbers exactly.   Use F4 to stop the clock,
then..
```
nano Temperature/TempNames.py
```
Give each number a name, like is shown in the examples in that file

### setting the clock to auto start
At this point the clock will only start when you manually start it, as
described in the Run It section.

Use only one autostart method.
## Autostart Method 1
(NOT as root)
```
cd HamClock
chmod +x HamClock.desktop
ln HamClock.desktop ~/Desktop
mkdir ~/.config/autostart
ln HamClock.desktop ~/.config/autostart
```
This puts the a HamClock icon on your desktop.  It also runs it when
the desktop starts.

## Autostart Method 2
To have it auto start on boot we need to do one more thing, edit the
crontab file as follows: (it will automatically start nano)  (NOT as root)
```
crontab -e
```
and add the following line:
```
@reboot sh /home/pi/HamClock/startup.sh
```
save the file
and reboot to test
```
sudo reboot
```

## Some notes about startup.sh
startup.sh has a few options:
* -n or --no-delay			Don't delay on starting the clock right away (default is 45 seconds delay)
* -d X or --delay X			Delay X seconds before starting the clock
* -m X or --message-delay X 	Delay X seconds while displaying a message on the desktop

Startup also looks at the various optional HamClock items (Buttons, Temperature, NeoPixel, etc)
and only starts those things that are configured to run.   It also checks if they are already
running, and refrains from starting them again if they are.

### Switching skins at certain times of the day
This is optional, but if its just too bright at night, a switcher script will kill and restart
PyQtHamClock with an alternate config.

First you need to set up an alternate config.   Config.py is the normal name, so perhaps Config-Night.py
might be appropriate.  For a dimmer display use Config-Example-Bedside.py as a guide.

Now we'll tell our friend cron to run the switcher script (switcher.sh) on day/night cycles.
Run the cron editor: (should *not* be roor)
```
crontab -e
```
Add lines similar to this:
```
0 8 * * * sh /home/pi/HamClock/switcher.sh Config
0 21 * * * sh /home/pi/HamClock/switcher.sh Config-Night
```
The 8 there means 8am, to switch to the normal config, and the 21 means switch to Config-Night at 9pm.
More info on crontab can be found here: https://en.wikipedia.org/wiki/Cron

### Setting the Pi to auto reboot every day
This is optional but some may want their HamClock to reboot every day.  I do this with mine,
but it is probably not needed.
```
sudo crontab -e
```
add the following line
```
22 3 * * * /sbin/reboot
```
save the file

This sets the reboot to occur at 3:22am every day.   Adjust as needed.

### Updating to newer/updated versions
Since we pulled the software from github originally, it can be updated
using git and github.
```
cd HamClock
git pull
python update.py
```
This will automatically update any part(s) of the software that has changed.
The update.py program will then convert any config files as needed.

You'll want to reboot after the update.

Note: If you get errors because you've made changes to the base code you might need
```
git reset --hard
```
Backup your changes first!
(This won't bother your Config.py nor ApiKeys.py because they are not tracked in git.

Also, if you're using gpio-keys, you may need to remake it:
```
cd HamClock/Buttons
rm gpio-keys
make gpio-keys
```

