import cv2

im = cv2.imread('img.png')

min_val, max_val, min_loc, max_loc = \
        cv2.minMaxLoc(cv2.cvtColor(im,cv2.COLOR_RGB2GRAY))

print("max loc = {}".format(max_loc))

im[:, : ,(0, 1)] = 0

min_val, max_val, min_loc, max_loc = \
        cv2.minMaxLoc(cv2.cvtColor(im,cv2.COLOR_RGB2GRAY))

print("max loc = {}".format(max_loc))

cv2.imshow('led', im)
cv2.waitKey(10000)
cv2.destroyAllWindows()

