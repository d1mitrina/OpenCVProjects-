#Drawing diagonal line on image 
import cv2
image = cv2.imread('cat.jpg')

 
start = (0,0)
end=(250,250)
color = (255,0,0)
border = 2 
image =cv2.line(image, start, end, color, border)


cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()