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
  a_deg_offset = 77
  b_deg_offset = 83

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

if   x_position < 124:
  x_degree = -10
elif x_position < 221:
  x_degree = -8
elif x_position < 310:
  x_degree = -5
elif x_position < 394:
  x_degree = -2
elif x_position < 496:
  x_degree = 0
elif x_position < 602:
  x_degree = 3
elif x_position < 692:
  x_degree = 5
elif x_position < 783:
  x_degree = 8
elif x_position < 879:
  x_degree = 10
else:
  x_degree = 11

# y

if   y_position < 123:
  y_degree = 17
elif y_position < 234:
  y_degree = 13
elif y_position < 350:
  y_degree = 9
elif y_position < 470:
  y_degree = 6
elif y_position < 595:
  y_degree = 0
elif y_position < 723:
  y_degree = -6
else:
  y_degree = -7


move( x_degree, y_degree, 0.1 )

#pi.digitalWrite( led_pin, 0 ) # LED off

