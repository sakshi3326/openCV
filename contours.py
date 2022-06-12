import cv2 as cv
from cv2 import blur

img = cv.imread('photos/panda.webp')

resized = cv.resize(img,(550,550),interpolation=cv.INTER_CUBIC)
cv.imshow('Img',resized)
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
    
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#canny = cv.Canny(blur,125,175)
#cv.imshow('Canny edged',canny)

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)