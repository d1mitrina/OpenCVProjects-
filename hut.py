#Drawing triangles / squares to make a hut 
import cv2
import numpy as np
image = cv2.imread('cat.jpg')

start = (200,200)
end = (300,300)
color = (255,0,0)
border = 1
image = cv2.rectangle(image, start, end, color, border)

start = (200,200)
end=(250,100)
color = (255,0,0)
border = 1
image =cv2.line(image, start, end, color, border)

start = (250,100)
end=(300,200)
color = (255,0,0)
border = 1
image =cv2.line(image, start, end, color, border)



cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()


image =cv2.rectangle(image, start, end, color, border)

cv2.imshow('Hut',image)
cv2.waitKey(0)
cv2.destroyAllWindows()