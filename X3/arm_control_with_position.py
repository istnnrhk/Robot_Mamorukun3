#-------------------------------------------------------
#
# arm-control program
#
#-------------------------------------------------------
import sys
import wiringpi as pi, time

#-------------------------------------------------------
# PARTS
#-------------------------------------------------------
def move( a_deg = 0 , b_deg = 0, waiting = 0):
  a_deg_offset = 73
  b_deg_offset = 80

  move_A_deg = int( a_deg_offset + a_deg )
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

#for y in range(-10, 10):
#  for x in range(-5, 10):
#    move( x, y, 0.1 )

#move(  10,  15, 1 )
#move(  10,  -5, 1 )
#move( -10,  -5, 1 )
#move( -10,  15, 1 )
#move(   0,   0, 1 )

args = sys.argv

x_position = int(args[1])
y_position = int(args[2])

# x

if   x_position < 270:
  x_degree = -10
elif x_position < 351:
  x_degree = -7
elif x_position < 432:
  x_degree = -4
elif x_position < 524:
  x_degree = -2
elif x_position < 616:
  x_degree = 1
elif x_position < 698:
  x_degree = 4
elif x_position < 779:
  x_degree = 6
else:
  x_degree = 10

# y

if   y_position < 0:
  y_degree = 15
elif y_position < 93:
  y_degree = 12
elif y_position < 202:
  y_degree = 9
elif y_position < 310:
  y_degree = 5
elif y_position < 417:
  y_degree = 2
elif y_position < 523:
  y_degree = -2
else:
  y_degree = -5


move( x_degree, y_degree, 0.1 )

#pi.digitalWrite( led_pin, 0 ) # LED off

