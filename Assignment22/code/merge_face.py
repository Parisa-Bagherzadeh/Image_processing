import cv2

img1=cv2.imread('pp.jpg',0)
img2=cv2.imread('paris.jpg',0)
img1=cv2.resize(img1,(300,300))
img2=cv2.resize(img2,(300,300))



img1_1=img1
img2_1=img2//4
result1=img1_1+img2_1
result1=cv2.resize(result1,(400,400))
cv2.imwrite('merge_face1.jpg',result1)


img1_2=img1//2
img2_2=img2//2
result2=img1_2+img2_2
result2=cv2.resize(result2,(400,400))
cv2.imwrite('merge_face2.jpg',result2)
