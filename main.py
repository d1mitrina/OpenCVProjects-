#Making a solid border of 1 by 1 pixel on an image 
import os #operating system 
import cv2
image=cv2.imread('/Users/yanigrazhdani/Desktop/OpenCVProjects/Lesson2/images/random_image.jpeg',1)
border=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_REFLECT,1,1) #solid line BORDER_REFLECT
cv2.imshow('border image',border)
cv2.waitKey(0)
cv2.destroyAllWindows()

 