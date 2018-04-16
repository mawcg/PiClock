# PiClock


A Ham Radio Clock built around a monitor and a Raspberry Pi

![HamPiClock Picture](http://github.com/mawcg/PiClock/Screen%20Shot%202018-04-16%20at%202.08.21%20PM.png)

This project is a fork from Kevin Uhlir's Pi-clock.  I modified it to be put into a communication trailer I am building.  It takes it's current location from a GPS receiver and provides the current coordinates and grid location.

Because I was adding so much more information I removed the analog clock option.  I am still working on what happens when there is no internet to get the weather information.  I might eventually try to hook it into APRS or a local weather station on the trailer.

I want to also add the the UTM coordintates but I have not figured out yet how to convert Lat/Lon into UTM.

If you are using a GPS to get your current location, be sure to also use it to set the clock on the Pi.  My Pi that is running this clock also has an NTP server running on it so the other computers in the trailer can use it as a time server.

Here is a link to the original clock that was created by Kevin: https://github.com/n0bel/PiClock

