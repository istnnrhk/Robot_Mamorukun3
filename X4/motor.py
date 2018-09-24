import sys
import wiringpi as pi,time


args = sys.argv
shootsec = int(args[1])

laser_pin  = 23
motor1_pin = 22
motor2_pin = 24


pi.wiringPiSetupGpio()
pi.pinMode( motor1_pin, 1 )
pi.pinMode( motor1_pin, 1 )
pi.pinMode( motor2_pin, 1 )

pi.digitalWrite( laser_pin, 1 ) # LED on
pi.digitalWrite( motor1_pin, 1 )
pi.digitalWrite( motor2_pin, 0 )
time.sleep(shootsec)

pi.digitalWrite( motor1_pin, 0 )
pi.digitalWrite( motor2_pin, 0 )
pi.digitalWrite( laser_pin , 0 ) # LED off
