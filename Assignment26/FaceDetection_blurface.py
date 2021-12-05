import cv2
import numpy as np


file_face = 'haarcascade_frontalface_default.xml'
face_detector = cv2.CascadeClassifier(file_face)

file_eye = 'haarcascade_eye.xml'
eye_detector = cv2.CascadeClassifier(file_eye)

file_mouth = 'mouth.xml'
mouth_detector = cv2.CascadeClassifier(file_mouth)

emoji_face = cv2.imread('face5.png',0)
emoji_eye = cv2.imread('eye6.png',0)
emoji_mouth = cv2.imread('lips8.jpg',0)



vid = cv2.VideoCapture(0)

flag_face = False

while (True):

    ret, frame = vid.read()
    

    if ret == False:
        break


    filter=np.ones((7,7))/49
    

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame_gray)
    f=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    faces = face_detector.detectMultiScale(frame_gray, 1.3)
    eyes = eye_detector.detectMultiScale(frame_gray, 1.1)
    mouth = mouth_detector.detectMultiScale(frame_gray, 1.1)

    

    if cv2.waitKey(1) & 0xFF == ord('1'):

        
        for (x, y, w, h) in faces:
            emoji_face_resized = cv2.resize(emoji_face, (w, h))
            frame_gray[y:y+h,x:x+w]=emoji_face_resized
            for i in range(y,y+h):
                for j in range(x,x+w):
                    if frame_gray[i,j]>=246 and frame_gray[i,j]<=255:
                        frame_gray[i,j]=f[i,j]
   

    
    if cv2.waitKey(1) & 0xFF == ord('2'):
        
        for (ex, ey, ew, eh) in eyes:
            emoji_eye_resized = cv2.resize(emoji_eye, (ew, eh))
            frame_gray[ey:ey+eh, ex:ex+ew] = emoji_eye_resized
            for i in range(ey,ey+eh):
                for j in range(ex,ex+ew):
                    if frame_gray[i,j]==0:
                        frame_gray[i,j]=f[i,j]


 

        for (mx, my, mw, mh) in mouth:
            emoji_mouth_resized = cv2.resize(emoji_mouth, (mw, mh))
            frame_gray[my:my + mh, mx:mx + mw] = emoji_mouth_resized
            for i in range(my,my+mh):
                for j in range(mx,mx+mw):
                    if frame_gray[i,j]==255:
                       frame_gray[i,j]=f[i,j]

        cv2.imshow('frame', frame_gray)

    if cv2.waitKey(1) & 0xFF == ord('3'):
        for (x, y, w, h) in faces:
           temp=cv2.resize(frame_gray[y:y+h,x:x+w],(16,16),interpolation=cv2.INTER_LINEAR)
           frame_gray[y:y+h,x:x+w]=cv2.resize(temp,(w,h),interpolation=cv2.INTER_NEAREST)   

        cv2.imshow('frame',frame_gray)      

    if cv2.waitKey(1) & 0xFF == ord('4'):
        for (x,y,w,h) in faces:
            frame_gray[y:y+h,x:x+w]= cv2.rotate(frame_gray[y:y+h,x:x+w],cv2.ROTATE_90_CLOCKWISE)

        cv2.imshow('frame',frame_gray)    

    if cv2.waitKey(1) & 0xFF==ord('5'): 
        for (x,y,w,h)in faces:
            face=cv2.rectangle(frame_gray,(x,y),(x+w,y+h),(0,255,0),1)
            face[y:y+h,x:x+w]=cv2.medianBlur(face[y:y+h,x:x+w],35)    
        cv2.imshow('frame',frame_gray)    



    cv2.imshow('frame', frame_gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

vid.release()
cv2.destroyAllWindows()


