import cv2 as cv
from cv2 import resize
img = cv.imread('photos/panda.webp')
resized = cv.resize(img,(500,500))
cv.imshow('Img',resized)

#BRG to HSV
hsv = cv.cvtColor(resized,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

cv.waitKey(0)