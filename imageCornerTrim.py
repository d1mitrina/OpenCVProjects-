import cv2
import numpy as np

second_image=cv2.imread("ImageCalculation/image2.png")
cv2.imshow("OriginalSize",second_image)


cv2.waitKey(0) 
array1 = np.ones((9,9)) #function of numpy array -->((rows, columns)) data type interger - will occupy 8 bits of space
#array1 = np.ones((9,9),np.uint8) --> same
image = cv2.erode(second_image,array1) #will bring image into this array 

cv2.imshow("Eroded Image",image)
cv2.waitKey(0) 

cv2.destroyAllWindows()
