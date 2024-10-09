# Converting the original image to grey scale image 
import os 
import cv2
img=cv2.imread('Lesson1IntroToOpenCV/images/cat.jpg',cv2.IMREAD_GRAYSCALE) #image read
cv2.imshow('cat image display',img) #image show
cv2.waitKey(0) #infinite time
cv2.destroyAllWindows()
#cv2.IMREAD_COLOR --> load the picture in color 
