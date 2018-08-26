import wiringpi as pi,time

motor1_pin = 22
motor2_pin = 24

pi.wiringPiSetupGpio()
pi.pinMode( motor1_pin, 1 )
pi.pinMode( motor2_pin, 1 )


pi.digitalWrite( motor1_pin, 1 )
pi.digitalWrite( motor2_pin, 0 )
time.sleep(4)

pi.digitalWrite( motor1_pin, 0 )
pi.digitalWrite( motor2_pin, 0 )


