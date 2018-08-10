import wiringpi as pi, time

servo_pin = 18
set_degree = -90

pi.wiringPiSetupGpio()
pi.pinMode( servo_pin, 2 )
pi.pwmSetMode(0)
pi.pwmSetRange(1024)
pi.pwmSetClock(375)

if ( set_degree <= 90 and set_degree >= -90 ):
    move_deg = int( 74 + 48 / 90 * set_degree )
    pi.pwmWrite( servo_pin, move_deg )
