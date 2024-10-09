import cv2
image = cv2.imread('cat.jpg')


#coodinates 
coordinates = (120,50)
#raduis of circle
radius = 20
#color of circle 
color = (255,0,0)
#thickness of line 
border = 2 

#using cv2.circle() inbuilt function 
#draw circle with blue line borders of thickness of 2px
image =cv2.circle(image, coordinates, radius, color, border)

#displaying the image 

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()