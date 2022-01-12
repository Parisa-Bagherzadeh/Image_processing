import cv2
import numpy as np



video=cv2.VideoCapture(0)


min_HSV=np.array([0,58,30],dtype='uint8')
max_HSV=np.array([33,255,255],dtype='uint8')

while(True):
    ret,BGR_frame=video.read()

    if ret==False:
        break
   
    HSV_frame=cv2.cvtColor(BGR_frame,cv2.COLOR_BGR2HSV)
    skinRegionHSV=cv2.inRange(HSV_frame,min_HSV,max_HSV)
    skinHSV=cv2.bitwise_and(BGR_frame,BGR_frame,mask=skinRegionHSV)
    cv2.imshow('frame',skinHSV)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()    