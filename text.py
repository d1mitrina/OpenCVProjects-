import cv2
image = cv2.imread('cat.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50,50)
fontScale = 1
color = (0,250,0)
thickness = 2

image =cv2.putText(image, 'Hello! Welcome to OpenCV', org,font,fontScale,color,thickness, cv2.LINE_AA)

#displaying the image 

cv2.imshow('TextOnImage',image)
cv2.waitKey(0)
cv2.destroyAllWindows()