#Applying gaussian blurring tequnique to an image 
import cv2 
import numpy as np 
image=cv2.imread("cat.jpg",1)
#gaussian blur used in machine learning proccesses
gaussian=cv2.GaussianBlur(image,(5,5),0) #used to reduce image noise - reduces background blur by averaging pixel values
cv2.imshow("Gauss",gaussian) #'gauss is the title for the window'


cv2.waitKey(0)
cv2.destroyAllWindows()
