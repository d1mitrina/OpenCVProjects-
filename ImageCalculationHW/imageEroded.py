import cv2 
import numpy as np

flower_image = cv2.imread("ImageCalculationHW/flowers.jpg")
stars_image = cv2.imread("ImageCalculationHW/starrynight.jpg")
cv2.imshow("Original Image",flower_image)
cv2.waitKey(0)

x = np.ones((50,75))
y = np.ones((10,10))
eroded = cv2.erode(flower_image,x)
eroded2 = cv2.erode(stars_image,y)


image=cv2.imshow("Eroded Image",eroded)
image2=cv2.imshow("Eroded Image 2",eroded2)



cv2.waitKey(0)
cv2.destroyAllWindows()