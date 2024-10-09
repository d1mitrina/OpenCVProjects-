import cv2
image = cv2.imread('cat.jpg')


start = (5,5)
end = (220,220)
color = (255,0,0)
border = -1

image =cv2.rectangle(image, start, end, color, border)

#displaying the image 

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()