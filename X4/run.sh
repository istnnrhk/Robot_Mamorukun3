#!/bin/bash

set -eux

cd /home/pi/Lab/Robot_Mamorukun3/X4/

sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/green_led_on.py

sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/arm_control.py -10 0 0 0
sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/motor.py 10
sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/arm_init.py

for i in {1..3} ; do
  echo ${i}
  vcgencmd measure_temp
  sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/red_led_on.py
  sh /home/pi/Lab/Robot_Mamorukun3/X4/camera.sh
  python3 /home/pi/Lab/Robot_Mamorukun3/X4/detect.py
  vcgencmd measure_temp
  sleep 2s
done

sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/arm_init.py
sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/green_led_off.py

sleep 3s
