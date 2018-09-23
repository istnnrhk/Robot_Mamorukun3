#! /usr/bin/env python
# -*- coding: utf-8 -*-
#import picamera
import cv2
#from time import sleep
from numpy import sqrt
import copy
import subprocess


#画像をグレースケールで読み込む
img_color = cv2.imread("/home/pi/Lab/Robot_Mamorukun3/X4/img.png",  cv2.IMREAD_COLOR)
temp_gray = cv2.imread("/home/pi/Lab/Robot_Mamorukun3/X4/temp.png", cv2.IMREAD_GRAYSCALE)

#
img_gray  = cv2.cvtColor(img_color,cv2.COLOR_RGB2GRAY)

#マッチングテンプレートを実行
#比較方法はcv2.TM_CCOEFF_NORMEDを選択
result = cv2.matchTemplate(img_gray, temp_gray, cv2.TM_CCOEFF_NORMED)

#検出結果から検出領域の位置を取得
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
w, h = temp_gray.shape[::-1]

if True:
    # to reduce temperature, omit saving process
    bottom_right = (top_left[0] + w, top_left[1] + h)

    #検出領域を四角で囲んで保存
    result = img_color
    cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)


target_x = top_left[0]+int(w/2)
target_y = top_left[1]+int(h/2)

print("Target position : center   = ({}, {}) : max_val = {:.2f}".
      format(target_x, target_y, max_val))

# if confidence is less than 0.5, skip this process
if max_val < 0.3:
    print("low confidence")
    exit(0)

if True:
    ''' to reduce temperature, omit LED process '''
    # 
    img_red = copy.deepcopy(img_color)
    img_red[:, : ,(0, 1)] = 0

    min_val, max_val, min_loc, max_loc = \
        cv2.minMaxLoc(cv2.cvtColor(img_red,cv2.COLOR_RGB2GRAY))

    lasar_x = max_loc[0]
    lasar_y = max_loc[1]

    top_left     = (lasar_x - 10, lasar_y - 10)
    bottom_right = (lasar_x + 10, lasar_y + 10)

    #検出領域を四角で囲んで保存
    #result = cv2.imread("img.png")
    cv2.rectangle(result,top_left, bottom_right, (0, 255, 0), 2)
    cv2.imwrite("result.png", result)

    print("lasar (brightest) position = {}".format(max_loc))

    distance = sqrt((target_x - lasar_x)**2 + (target_y - lasar_y)**2)
    print("Distance between target and lasar : {:.0f}".format(distance))

    
if False:
    '''
    display result image
    '''
    cv2.imshow('result',result)
    cv2.waitKey(10000) # waiting key input [ms]
    cv2.destroyAllWindows()


# servo controll
cmd = "sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/arm_control_with_position.py {} {}".format(target_x, target_y)
print(cmd)
subprocess.check_call(cmd.split())

# motor controll
cmd = "sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/motor.py {}".format(3)
print(cmd)
subprocess.check_call(cmd.split())

# home position
cmd = "sudo python3 /home/pi/Lab/Robot_Mamorukun3/X4/arm_control.py {} {}".format(0, 0, 1, 0)
print(cmd)
subprocess.check_call(cmd.split())
