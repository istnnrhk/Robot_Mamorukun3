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
def arm_control( a_deg = 0 , b_deg = 0, waiting = 0, keep_led = 0):
  a_deg_offset = 77
  b_deg_offset = 83

  pi.digitalWrite( laser_pin    , 1 ) # Laser on
  move_A_deg = int( a_deg_offset + a_deg )
  move_B_deg = int( b_deg_offset - b_deg )
  pi.pwmWrite( servoA_pin, move_A_deg )
  pi.pwmWrite( servoB_pin, move_B_deg )
  time.sleep(waiting)
  pi.digitalWrite( laser_pin    , keep_led ) # Laser off
  return

#-------------------------------------------------------
# Setup
#-------------------------------------------------------
pi.wiringPiSetupGpio()

laser_pin   = 23
red_led_pin = 10
servoA_pin  = 18 # elevation angle
servoB_pin  = 13 # azimuth angle

# set pinMode
pi.pinMode( laser_pin   , 1 )
pi.pinMode( red_led_pin , 1 )
pi.pinMode( servoA_pin  , 2 )
pi.pinMode( servoB_pin  , 2 )
# set pwm
pi.pwmSetMode(0)
pi.pwmSetRange(1024)
pi.pwmSetClock(375)

#--------------------------------------------------------
# MAIN PROCESS
#--------------------------------------------------------

def main():
  args = sys.argv

  azimuth_angle   = int(args[1])
  elevation_angle = int(args[2])
  shooting_sec    = int(args[3])
  keep_led        = int(args[4])

  arm_control( azimuth_angle, elevation_angle, shooting_sec, keep_led)



if __name__ == '__main__':
  main()
