from GoogleMercatorProjection import LatLng
from PyQt4.QtGui import QColor


# LOCATION(S)
# Further radar configuration (zoom, marker location) can be
# completed under the RADAR section
primary_coordinates = 39.347538, -77.616998  # Change to your Lat/Lon
cur_lat = 39.347538
cur_lon = -77.616998
callsign = 'N0CALL'
usegps = 0

# right sidebar setup
# Types:
#   0 = Hourly Weather
#   1 = Daily Weather
#   2 = Time Zone Time
#   3 = Tide Details

# Hourly Weather values
#   Number of hours into the future to display.
#   Numbers have to be greater than zero and less than 48

# Daily Weather Values
#   0 = Tomorrow
#   1 = Day After Tomorrow
#   2 = Three Days ahead of today
#   3 = Four Days ahead of today
#   4 = Five Days ahead of today
#   5 = Six Days ahead of today
#   6 = Seven Days ahead of today
#   7 = Eight Days ahead of today

# Time Zone Time values
# hours (negative or positive) from UTC

sidebar = {
    0 : ({
        'type'  : 0,
        'value' : 1
        }),
    1 : {
        'type'  : 0,
        'value' : 3
        },
    2 : {
        'type'  : 0,
        'value' : 6
        },
    3 : {
        'type'  : 1,
        'value' : 0
        },
    4 : {
        'type'  : 1,
        'value' : 1
        },
    5 : {
        'type'  : 1,
        'value' : 2
        },
    6 : {
        'type'  : 1,
        'value' : 2
        },
    7 : {
        'type'  : 1,
        'value' : 2
        },
    8 : {
        'type'  : 1,
        'value' : 2
        },
    9 : {
        'type'  : 1,
        'value' : 2
        }
}

wuprefix = 'http://api.wunderground.com/api/'
wulocation = LatLng(primary_coordinates[0], primary_coordinates[1])
primary_location = LatLng(primary_coordinates[0], primary_coordinates[1])
noaastream = 'http://audioplayer.wunderground.com:80/tim273/edina'
background = 'images/clockbackground-.png'
squares1 = 'images/squares1-jean.png'
squares2 = 'images/squares2-jean.png'
icons = 'icons-lightblue'
textcolor = '#bef'


# Goes with light blue config (like the default one)
digitalcolor = "#FFFFFF"
digitalformat = "{0:%I:%M}"  # The format of the time
digitalsize = 200
callsignsize = 150
latlonsize = 70
gridsquaresize = 70
# The above example shows in this way:
#  https://github.com/n0bel/PiClock/blob/master/Documentation/Digital%20Clock%20v1.jpg
# ( specifications of the time string are documented here:
#  https://docs.python.org/2/library/time.html#time.strftime )

# digitalformat = "{0:%I:%M}"
# digitalsize = 250
#  The above example shows in this way:
#  https://github.com/n0bel/PiClock/blob/master/Documentation/Digital%20Clock%20v2.jpg


metric = 0  # 0 = English, 1 = Metric
radar_refresh = 20      # minutes
weather_refresh = 30    # minutes
# Wind in degrees instead of cardinal 0 = cardinal, 1 = degrees
wind_degrees = 0
# Depreciated: use 'satellite' key in radar section, on a per radar basis
# if this is used, all radar blocks will get satellite images
satellite = 0

# gives all text additional attributes using QT style notation
# example: fontattr = 'font-weight: bold; '
fontattr = ''

# These are to dim the radar images, if needed.
# see and try Config-Example-Bedside.py
dimcolor = QColor('#000000')
dimcolor.setAlpha(0)

# Language Specific wording
# Weather Undeground Language code
#  (https://www.wunderground.com/weather/api/d/docs?d=language-support&MR=1)
wuLanguage = "EN"

# The Python Locale for date/time (locale.setlocale)
#  '' for default Pi Setting
# Locales must be installed in your Pi.. to check what is installed
# locale -a
# to install locales
# sudo dpkg-reconfigure locales
DateLocale = ''

# Language specific wording
LPressure = "Pressure "
LHumidity = "Humidity "
LWind = "Wind "
Lgusting = " gusting "
LFeelslike = "Feels like "
LPrecip1hr = " Precip 1hr:"
LToday = "Today: "
LSunRise = "Sun Rise:"
LSet = " Set: "
LMoonPhase = " Moon Phase:"
LInsideTemp = "Inside Temp "
LRain = " Rain: "
LSnow = " Snow: "


# RADAR
# By default, primary_location entered will be the
#  center and marker of all radar images.
# To update centers/markers, change radar sections below the desired lat/lon as:
# -FROM-
# primary_location,
# -TO-
# LatLng(44.9764016,-93.2486732),
radar1 = {
    'center': primary_location,  # the center of your radar block
    'zoom': 7,  # this is a google maps zoom factor, bigger = smaller area
    'satellite': 0,    # 1 => show satellite images (colorized IR images)
    'markers': (   # google maps markers can be overlayed
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },          # dangling comma is on purpose.
    )
}


radar2 = {
    'center': primary_location,
    'zoom': 11,
    'satellite': 0,
    'markers': (
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },
    )
}


