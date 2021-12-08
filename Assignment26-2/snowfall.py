import cv2
import glob
import random
import os
import imageio

def make_snow():
    image_winter=cv2.imread('winter.jpg',0)    
    rows=image_winter.shape[0]
    cols=image_winter.shape[1]
    file_counter=0
    step=0

    list_len=3
    snow_x=[]
    snow_y=[]
    snow_r=[]
    r_move=[]
    counter=0
    
    for i in range(0,rows,3):
        step+=1
        for j in range(list_len):
            x=random.randint(4,cols)
            y=random.randint(0,5)
            r=random.randint(3,4)
            snow_x.append(x)
            snow_y.append(y)
            snow_r.append(r)

        for k in range(list_len*step):
            
            image=cv2.circle(image_winter,(snow_x[k],snow_y[k]),snow_r[k],(200,210,215),-1)
            if k%4==0:
                snow_y[k]+=4
            elif k%3==0:
                snow_x[k]+=3
                snow_y[k]+=3
            else: 
                snow_x[k]-=4
                snow_y[k]+=3
                    
        cv2.imwrite(f'images/{counter}.jpg',image)
        counter+=1
        image_winter=cv2.imread('winter.jpg',0)

    return counter            

counter=make_snow()

def read_frames():
    frame_array=[]
    #print(counter)
    images=[]
    # for i in range(counter):
    #     for filename in glob.glob(f'images/{i}.jpg'):
    #         if filename.endswith('.jpg'):
    #             file_path=os.path.join(filename)
    #             images.append(imageio.imread(file_path))
    #         imageio.mimsave('images/snowfall.gif',images)

    for i in range(counter):
        for filename in glob.glob(f'images/{i}.jpg'):      
            frame=cv2.imread(filename,0)
            height,width=frame.shape
            size=(width,height)
            frame_array.append(frame)
    out=cv2.VideoWriter('snowfall.avi',cv2.VideoWriter_fourcc(*'DIVX'),20, size,0)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
        
    out.release()

read_frames()    
