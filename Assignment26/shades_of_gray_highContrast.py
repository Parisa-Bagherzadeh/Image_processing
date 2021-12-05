import cv2
import numpy as np
from numpy.lib import average


video=cv2.VideoCapture(0)

frame_width=int(video.get(3))
frame_height=int(video.get(4))
size=(frame_width,frame_height)
result=cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*"MJPG"),30,size,0)
filter=np.ones((15,15))/125
upper_left = (50, 50)
bottom_right = (300, 300)


while(True):

    ret,frame=video.read()

    if ret==False:
        break
    
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    border=frame_gray[150:250,250:350]
    
    frame_gray=cv2.filter2D(frame_gray,0,kernel=filter)
    

    ii=-1
    jj=-1       
 
    for i in range(150,250):
        ii=ii+1
        for j in range(250,350):
            jj=jj+1
            frame_gray[i,j]=border[ii-1,jj-1]
        jj=-1    

    high_contrast_border=cv2.normalize(border,border,0,255,cv2.NORM_MINMAX)
    frame_gray[150:250,250:350]=high_contrast_border
    avg_border=np.average(border)

    if avg_border>=0 and avg_border<=70:
        cv2.putText(frame_gray,'Black',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA)   
    elif avg_border>=71 and avg_border<190:
        cv2.putText(frame_gray,'Gray',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA) 
    elif avg_border>=191 and avg_border<=255:
       cv2.putText(frame_gray,'White',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA)                       


    result.write(frame_gray)  
    cv2.imshow('frame',frame_gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()


    