import cv2 as cv
from matplotlib.pyplot import sca
img = cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions  = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img,scale=.9)
cv.imshow('Image', resized_image)  
capture = cv.VideoCapture('videos/caty.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=.5)
    #cv.imshow('video',frame)
    cv.imshow('video resized',frame_resized)
    
    
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    

capture.release()
cv.destroyAllWindows()
   