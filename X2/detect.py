#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from time import sleep
from numpy import sqrt
import copy
import subprocess

#################################################################

def loop(rx, ry):

    cmd = "raspistill -e png -o img.png -rot 180 -w 1024 -h 768 -t 1 -n"
    print(cmd)
    subprocess.check_call(cmd.split())
    
    #画像をグレースケールで読み込む
    img_color = cv2.imread("img.png",  cv2.IMREAD_COLOR)
    temp_gray = cv2.imread("temp.png", cv2.IMREAD_GRAYSCALE)

    #
    img_gray  = cv2.cvtColor(img_color,cv2.COLOR_RGB2GRAY)
    
    #マッチングテンプレートを実行
    #比較方法はcv2.TM_CCOEFF_NORMEDを選択
    result = cv2.matchTemplate(img_gray, temp_gray, cv2.TM_CCOEFF_NORMED)
    
    #検出結果から検出領域の位置を取得
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    w, h = temp_gray.shape[::-1]
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    #検出領域を四角で囲んで保存
    result = img_color
    cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)


    target_x = top_left[0]+int(w/2)
    target_y = top_left[1]+int(h/2)

    print("Target position : center   = ({}, {}) : max_val = {:.2f}".
          format(target_x, target_y, max_val))

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
    
    cv2.imshow('result',result)
    cv2.waitKey(1) # waiting key input [ms]
    cv2.destroyAllWindows()
    
    diff_x = lasar_x - target_x
    diff_y = lasar_y - target_y
    
    print("diff_x, diff_y = {}, {}".format(diff_x, diff_y))

    
    def shift(x):
        if x < 0 :
            return 1
        return -1
        
    rx +=  1 * shift(diff_x)
    ry += -1 * shift(diff_y)

    cmd = "sudo python3 arm_control.py {} {}".format(rx, ry)
    print(cmd)
    subprocess.check_call(cmd.split())

    return(rx, ry)
    
##############################################################

rx = 0
ry = 0

for i in range(0, 10):
    rx, ry = loop(rx, ry)
