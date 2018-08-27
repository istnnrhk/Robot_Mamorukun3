sudo python3 green_led_on.py

for i in 1 2 3 4 5 6 7 8 9 10 ; do
  echo ${i}
  vcgencmd measure_temp
  sh camera.sh
  python3 detect.py
  vcgencmd measure_temp
done

sudo python3 green_led_off.py
