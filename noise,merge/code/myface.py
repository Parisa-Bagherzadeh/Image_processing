import cv2

img1=cv2.imread('pp.jpg',0)
img2=cv2.imread('paris.jpg',0)
img1=cv2.resize(img1,(500,500))
img2=cv2.resize(img2,(500,500))
img1_1=img1
img2_1=img2//4
result1=img1_1+img2_1

cv2.imwrite('face1.jpg',result1)

img1_2=img1//2
img2_2=img2//2
result2=img1_2+img2_2
cv2.imwrite('face2.jpg',result2)

