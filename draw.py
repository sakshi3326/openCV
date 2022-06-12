import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('blank',blank)

#blank[100:200 , 200:300] = 0,255,0
#cv.imshow('Green',blank)

#cv.rectangle(blank, (0,0), (250,250),(0,250,0),thickness=3)
#cv.imshow('Rectangle',blank)
cv.putText(blank,'hii my name is sakshi',(0,225), cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)

