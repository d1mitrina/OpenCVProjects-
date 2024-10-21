import cv2
import numpy as np 

night_image = cv2.imread("ImageCalculationHW/starrynight.jpg")
cv2.imshow("Original Image",night_image)
cv2.waitKey(0)


resizedSmaller=cv2.resize(night_image,(200,400))
cv2.imshow("Resized Smaller",resizedSmaller)
cv2.waitKey(0)

resizedBigger=cv2.resize(night_image,(4000,5000))
cv2.imshow("Resized Bigger",resizedBigger)
cv2.waitKey(0)



cv2.destroyAllWindows()
