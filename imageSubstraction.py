import cv2
import numpy as np

first_image=cv2.imread("ImageCalculation/image1.png")
second_image=cv2.imread("ImageCalculation/image2.png")

#weighted sum is the sum of pixels 

subtraction=cv2.subtract(second_image,first_image) 
#gamma - mesuremnet of light - 0 takes exact lighting values 

cv2.imshow("Subtraction",subtraction)
cv2.waitKey(0) 
cv2.destroyAllWindows()
