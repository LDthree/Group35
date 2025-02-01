import cv2 as cv
img = cv.imread("/home/Group35/Code/image.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0)