#Drawing a filled circle on image
import cv2
image = cv2.imread('cat.jpg')
window_name = 'circle filled'
co_ords = (120,100)
radius = 30
color = (0,0,255)
border= -1 #filled
image = cv2.circle(image, co_ords, radius, color, border)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()