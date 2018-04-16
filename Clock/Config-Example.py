from GoogleMercatorProjection import LatLng
from PyQt4.QtGui import QColor


# LOCATION(S)
# Further radar configuration (zoom, marker location) can be
# completed under the RADAR section
primary_coordinates = 39.347538, -77.616998  # Change to your Lat/Lon
cur_lat = 39.347538
cur_lon = -77.616998
callsign = 'N0CAL'
usegps = 0


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

metric = 0  # 0 = English, 1 = Metric
radar_refresh = 10      # minutes
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


radar3 = {
    'center': primary_location,
    'zoom': 7,
    'satellite': 0,
    'markers': (
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },
    )
}

radar4 = {
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
