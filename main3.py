#Applying a saturated filter - colour is converted to HSV
import cv2, os 
import numpy as np

image = cv2.imread("Lesson3.blur/random_image.jpeg")
saturated = cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #cvt - converted color 
cv2.imshow("Saturated",saturated)

cv2.waitKey(0)
cv2.destroyAllWindows()