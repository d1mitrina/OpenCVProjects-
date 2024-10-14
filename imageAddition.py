import cv2
import numpy as np # numerical python library, all function which do mathematical and statistical operations 

first_image=cv2.imread("ImageCalculation/image1.png")
second_image=cv2.imread("ImageCalculation/image2.png")

#weighted sum is the sum of pixels 

weightedsum=cv2.addWeighted(first_image, 0.5, second_image, 0.5 ,0) 
#gamma - mesuremnet of light - 0 takes exact lighting values 

cv2.imshow("Weightedsum",weightedsum)
cv2.waitKey(0) #when output is on screen, can close by pressing any key from the keybored
cv2.destroyAllWindows()