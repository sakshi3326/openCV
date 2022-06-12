import cv2 as cv
img = cv.imread('photos/cat.jpg')
cv.imshow('cat',img)
#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gay',gray)

#blur
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT )
cv.imshow('Blur',blur)

cv.waitKey(0)