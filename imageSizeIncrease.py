import cv2

second_image=cv2.imread("ImageCalculation/image2.png")

cv2.imshow("OriginalSize",second_image)
cv2.waitKey(0) 

resize=cv2.resize(second_image,(700,750))

cv2.imshow("Increased Image",resize)
cv2.waitKey(0) 

cv2.destroyAllWindows()

#open computer vision - OpenCv
