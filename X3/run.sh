#!/bin/bash

set -eux

cd /home/pi/Lab/Robot_Mamorukun3/X3/

sudo python3 /home/pi/Lab/Robot_Mamorukun3/X3/green_led_on.py
sudo python3 /home/pi/Lab/Robot_Mamorukun3/X3/arm_init.py

for i in {1..3} ; do
  echo ${i}
  vcgencmd measure_temp
  sh /home/pi/Lab/Robot_Mamorukun3/X3/camera.sh
  python3 /home/pi/Lab/Robot_Mamorukun3/X3/detect.py
  vcgencmd measure_temp
  # sleep 2s
done

sudo python3 /home/pi/Lab/Robot_Mamorukun3/X3/arm_init.py
sudo python3 /home/pi/Lab/Robot_Mamorukun3/X3/green_led_off.py

# sleep 3s
