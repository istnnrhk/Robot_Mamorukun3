import wiringpi as pi, time

pi.wiringPiSetupGpio()

led_pin = 23
servoA_pin = 18
servoB_pin = 13

# set pinMode
pi.pinMode( led_pin, 1 )
pi.pinMode( servoA_pin, 2 )
pi.pinMode( servoB_pin, 2 )
# set pwm
pi.pwmSetMode(0)
pi.pwmSetRange(1024)
pi.pwmSetClock(375)

# LED on
pi.digitalWrite( led_pin, 1 )
# Servo A : -30, Servo B : -30

set_A_deg = -30
move_A_deg = int( 74 + 48 / 90 + set_A_deg )
pi.pwmWrite( servoA_pin, move_A_deg )
print("servoA_pin: {} move_A_deg: {}".format(servoA_pin, move_A_deg))

set_B_deg = -30
move_B_deg = int( 74 + 48 / 90 + set_B_deg )
pi.pwmWrite( servoB_pin, move_B_deg )
print("servoB_pin: {} move_B_deg: {}".format(servoB_pin, move_B_deg))

time.sleep(2)

# Servo A : +30, Servo B : +30
set_A_deg = 30
move_A_deg = int( 74 + 48 / 90 + set_A_deg )
pi.pwmWrite( servoA_pin, move_A_deg )
print("servoA_pin: {} move_A_deg: {}".format(servoA_pin, move_A_deg))

set_B_deg = 30
move_B_deg = int( 74 + 48 / 90 + set_B_deg )
pi.pwmWrite( servoB_pin, move_B_deg )
print("servoA_pin: {} move_B_deg: {}".format(servoB_pin, move_B_deg))

time.sleep(2)

# Servo A :   0, Servo B :  0
set_A_deg = 0
move_A_deg = int( 74 + 48 / 90 + set_A_deg )
pi.pwmWrite( servoA_pin, move_A_deg )
print("servoA_pin: {} move_A_deg: {}".format(servoA_pin, move_A_deg))

set_B_deg = 0
move_B_deg = int( 74 + 48 / 90 + set_B_deg )
pi.pwmWrite( servoB_pin, move_B_deg )
print("servoA_pin: {} move_B_deg: {}".format(servoB_pin, move_B_deg))

# LED off
pi.digitalWrite( led_pin, 0 )
