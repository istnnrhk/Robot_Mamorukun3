#-------------------------------------------------------
#
# arm-control program
#
#-------------------------------------------------------
import wiringpi as pi, time

#-------------------------------------------------------
# PARTS
#-------------------------------------------------------
def move( a_deg = 0 , b_deg = 0, waiting = 0):
  a_deg_offset = 73
  b_deg_offset = 80

  move_A_deg = int( a_deg_offset - a_deg )
  move_B_deg = int( b_deg_offset - b_deg )
  pi.pwmWrite( servoA_pin, move_A_deg )
  pi.pwmWrite( servoB_pin, move_B_deg )
  time.sleep(waiting)
  return

#-------------------------------------------------------
# Setup
#-------------------------------------------------------
pi.wiringPiSetupGpio()

led_pin = 23
servoA_pin = 18 # Altura
servoB_pin = 13 # Azimuth

# set pinMode
pi.pinMode( led_pin, 1 )
pi.pinMode( servoA_pin, 2 )
pi.pinMode( servoB_pin, 2 )
# set pwm
pi.pwmSetMode(0)
pi.pwmSetRange(1024)
pi.pwmSetClock(375)

#--------------------------------------------------------
# MAIN PROCESS
#--------------------------------------------------------
pi.digitalWrite( led_pin, 1 ) # LED on
#move(   0,   0, 0)

for y in range(-10, 10):
  for x in range(-5, 10):
    move( x, y, 0.1 )


#move(  10,  15, 1 )
#move(  10,  -5, 1 )
#move( -10,  -5, 1 )
#move( -10,  15, 1 )
#move(   0,   0, 1 )
pi.digitalWrite( led_pin, 0 ) # LED off

