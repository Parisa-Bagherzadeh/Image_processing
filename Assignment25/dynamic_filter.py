import cv2
import numpy as np

filter_size=int(input('filter size:'))
img=cv2.imread('paris.jpg',0)
cv2.imwrite('paris_gray.jpg',img)
rows,cols=img.shape
result=np.zeros(img.shape)




def filter(filter_size):
    
    filter=np.ones((filter_size,filter_size))/(filter_size*filter_size)
    

    if filter_size==3:
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                small_img=img[i-1:i+2,j-1:j+2]
                result[i,j]=np.sum(small_img*filter)
       
        return result

    elif filter_size==5:
        for i in range(2,rows-2):
            for j in range(2,cols-2):
                small_img=img[i-2:i+3,j-2:j+3]
                result[i,j]=np.sum(small_img*filter)
       
        return result

    elif filter_size==7:
        for i in range(3,rows-3):
            for j in range(3,cols-3):
                small_img=img[i-3:i+4,j-3:j+4]
                result[i,j]=np.sum(small_img*filter)
         
        return result

    elif filter_size==15:
        for i in range(7,rows-7):
            for j in range(7,cols-7):
                small_img=img[i-7:i+8,j-7:j+8]
                result[i,j]=np.sum(small_img*filter)
           
        return result


img_result=filter(filter_size)

cv2.imwrite(f'{filter_size}x{filter_size} filter.jpg',img_result)        









    






