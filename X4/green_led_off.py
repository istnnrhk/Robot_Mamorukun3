#-------------------------------------------------------
#
# arm-control program
#
#-------------------------------------------------------
import sys
import wiringpi as pi, time

#-------------------------------------------------------
# Setup
#-------------------------------------------------------
pi.wiringPiSetupGpio()

led_pin    = 9

# set pinMode
pi.pinMode( led_pin, 1 )

#--------------------------------------------------------
# MAIN PROCESS
#--------------------------------------------------------
pi.digitalWrite( led_pin, 0 ) # LED off
