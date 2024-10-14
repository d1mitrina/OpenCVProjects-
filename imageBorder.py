import os #operating system - takes image from the system 
import cv2
second_image=cv2.imread("ImageCalculation/image2.png")
cv2.imshow('Original',second_image)
cv2.waitKey(0)



border=cv2.copyMakeBorder(second_image,20,20,20,20,cv2.BORDER_REFLECT,1,1) 

cv2.imshow('Bordered Image',border)
cv2.waitKey(0)
cv2.destroyAllWindows()

 