import cv2
import numpy as np

flower_image = cv2.imread('ImageCalculationHW/flowers.jpg')
stars_image = cv2.imread('ImageCalculationHW/starrynight.jpg')


weighted_sum = cv2.addWeighted(flower_image,0.1,stars_image,0.4,0)


cv2.imshow('Added Images',weighted_sum)
cv2.waitKey(0)
cv2.destroyAllWindows()