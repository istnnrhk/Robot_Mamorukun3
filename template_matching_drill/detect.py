#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2

#画像をグレースケールで読み込む
img = cv2.imread("test/img.png", 0)
temp = cv2.imread("test/temp.png", 0)

#マッチングテンプレートを実行
#比較方法はcv2.TM_CCOEFF_NORMEDを選択
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)

#検出結果から検出領域の位置を取得
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
w, h = temp.shape[::-1]
bottom_right = (top_left[0] + w, top_left[1] + h)

#検出領域を四角で囲んで保存
result = cv2.imread("img.png")
cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
cv2.imwrite("result.png", result)

print("Target location\n top_left = {}\n bottom_right = bottom_right {}\n center = {}\n".format(top_left, bottom_right, (top_left[0]+int(w/2), top_left[1]+ int(h/2))))
