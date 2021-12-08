import cv2

img=cv2.imread('mnist.png',0)
rows=img.shape[0]
cols=img.shape[1]
height=rows//(10*5)
width=cols//100
counter=0
folder_counter=-1

for k in range(0,rows,height*5):
    folder_counter+=1
    for i in range(k,k+(height*5),height):
        for j in range(0,cols,width):
            small_img=img[i:i+height,j:j+width]
            cv2.imwrite(f'mnist_images/{folder_counter}/{counter}.jpg',small_img)
            counter+=1
            





