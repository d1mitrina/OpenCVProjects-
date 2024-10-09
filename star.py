import cv2
import numpy as np
image = cv2.imread('cat.jpg')


#first triangle
start = (200,200)
end=(300,200)
color = (255,0,0)
border = 2
image =cv2.line(image, start, end, color, border)

start = (200,200)
end=(250,100)
color = (255,0,0)
border = 2 
image =cv2.line(image, start, end, color, border)

start = (250,100)
end=(300,200)
color = (255,0,0)
border = 2 
image =cv2.line(image, start, end, color, border)

#second triangle
start = (200,120)
end=(300,120)
color = (255,0,0)
border = 2 
image =cv2.line(image, start, end, color, border)

start = (200,120)
end=(250,220)
color = (255,0,0)
border = 2 
image =cv2.line(image, start, end, color, border)

start = (250,220)
end=(300,120)
color = (255,0,0)
border = 2 
image =cv2.line(image, start, end, color, border)







cv2.imshow("Star", image)
cv2.waitKey()
cv2.destroyAllWindows()










image =cv2.rectangle(image, start, end, color, border)

cv2.imshow('Hut',image)
cv2.waitKey(0)
cv2.destroyAllWindows()