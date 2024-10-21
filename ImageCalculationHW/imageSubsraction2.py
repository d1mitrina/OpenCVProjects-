import cv2
import numpy as np 

flower_image = cv2.imread("ImageCalculationHW/flowers.jpg")
star_image = cv2.imread("ImageCalculationHW/starrynight.jpg")


substracted = cv2.subtract(star_image,flower_image)

cv2.imshow("Substracted image",substracted)
cv2.waitKey(0)
cv2.destroyAllWindows()