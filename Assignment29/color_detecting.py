import cv2
import numpy as np


video=cv2.VideoCapture(0)

frame_width=int(video.get(3))
frame_height=int(video.get(4))

size=(frame_width,frame_height)
result=cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*"MJPG"),30,size)
filter=np.ones((15,15))/125

while(True):
    ret,frame=video.read()
    
    if ret==False:
        break

    border=frame[150:250,250:350]
    frame=cv2.filter2D(frame,0,kernel=filter)

    ii=-1
    jj=-1       
 
    for i in range(150,250):
        ii=ii+1
        for j in range(250,350):
            jj=jj+1
            frame[i,j]=border[ii-1,jj-1]
        jj=-1  

    # high_contrast_border=cv2.normalize(border,border,0,255,cv2.NORM_MINMAX)
    # frame[150:250,250:350]=high_contrast_border    


    # avg_border=int(np.average(border))
    # cv2.putText(frame,str(avg_border),(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3,cv2.LINE_AA)

    # if avg_border>=0 and avg_border<=15:
    #     cv2.putText(frame,'Black',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA) 
    #    #
    # elif  avg_border>=16 and avg_border<=30:  
    #     cv2.putText(frame,'Blue',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA) 

    # elif  avg_border>=17 and avg_border<=45:  
    #     cv2.putText(frame,'Red',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA) 

    #elif  avg_border>=46 or avg_border<=60:    
    #     cv2.putText(frame,'Red',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA)




    B,G,R=cv2.split(border) 
 
    B_avg=int(np.average(B))
    G_avg=int(np.average(G))
    R_avg=int(np.average(R))
    print(B_avg,G_avg,R_avg)


    if ((B_avg>=0 and B_avg<=70) and (G_avg>=0 and G_avg<=70) and (R_avg>=90 and R_avg<=255)):
        cv2.putText(frame,'Red',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA) 

    elif ((B_avg>=100 and B_avg<=255) and (G_avg>=0 and G_avg<=100) and (R_avg>=0 and R_avg<=100)):
        cv2.putText(frame,'Blue',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA) 

    elif ((B_avg>=0 and B_avg<=50) and (G_avg>=50 and G_avg<=255) and (R_avg>=0 and R_avg<=50)):
        cv2.putText(frame,'Green',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA)    
   

    elif((B_avg>=50 and B_avg<=100) and (G_avg>=35 and G_avg<=45) and (R_avg>=50 and R_avg<=100)):   
        cv2.putText(frame,'Purple',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA) 

    elif((B_avg>=130 and B_avg<=255) and (G_avg>=130 and G_avg<=255) and (R_avg>=130 and R_avg<=255)):   
        cv2.putText(frame,'White',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA) 

    elif((B_avg>=0 and B_avg<=50) and (G_avg>=0 and G_avg<=30) and (R_avg>=0 and R_avg<=30)):   
        cv2.putText(frame,'Black',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA)    

    elif((B_avg>=65 and B_avg<=95) and (G_avg>=65 and G_avg<=95) and (R_avg>=65 and R_avg<=95)):
        cv2.putText(frame,'Gray',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA) 
    
    elif((B_avg>=190 and B_avg<=255) and (G_avg>=190 and G_avg<=255) and (R_avg>=0 and R_avg<=150)):
        cv2.putText(frame,'Cyan',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA) 

    elif((B_avg>=0 and B_avg<=70) and (G_avg>=75 and G_avg<=255) and (R_avg>=75 and R_avg<=255)):
        cv2.putText(frame,'Yellow',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA)    


    cv2.imshow('frame',frame)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()     
