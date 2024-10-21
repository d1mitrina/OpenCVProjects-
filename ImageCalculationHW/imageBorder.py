import cv2
import numpy as np 

flower_image = cv2.imread("ImageCalculationHW/flowers.jpg")
#border=cv2.copyMakeBorder(flower_image,100,100,100,100,cv2.BORDER_REFLECT,1,1) 
border=cv2.copyMakeBorder(flower_image,60,60,60,60,cv2.BORDER_WRAP,1,1)

#Other values for BORDER_TYPE are possible, such as BORDER_DEFAULT, BORDER_REPLICATE, BORDER_WRAP.
cv2.imshow("Bordered Image",border)
cv2.waitKey(0)
cv2.destroyAllWindows()

