#Applying median blurring tequnique to an image, Applying bilateral filter - smooths out image 
import os, cv2 
import numpy as np 
image=cv2.imread("cat.jpg")
#median blur : used in digital proccesses / keeps the edges and removes the noise in the image 
median=cv2.medianBlur(image,5,0)
cv2.imshow("Median",median)

#bilateral filter - opposite of median 
#smooths images perserving the edges
bilateral = cv2.bilateralFilter(image, 5,70,70) # image, diameter of pixels, sigma color, sigma space
cv2.imshow("Bilateral",bilateral)



cv2.waitKey(0)
cv2.destroyAllWindows()