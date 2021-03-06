import cv2 as cv
from cv2 import erode
from cv2 import INTER_CUBIC
from numpy import ediff1d
img = cv.imread('photos/cat.jpg')
cv.imshow('cat',img)
#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gay',gray)

#blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT )
cv.imshow('Blur',blur)

#eddge cascade
edge = cv.Canny(img,125,175)
cv.imshow('Edge',edge)
#Dilate
dilate = cv.dilate(edge,(7,7),iterations=3)
cv.imshow('Dilate',dilate)
#Eroding
erode = cv.erode(dilate,(7,7),iterations=3)
cv.imshow('Erode',erode)
#resizing
resized = cv.resize(img,(550,550),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)
#crop
cropped= img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
