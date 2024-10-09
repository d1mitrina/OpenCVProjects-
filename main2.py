import cv2
import numpy as np
blobby = cv2.imread("circles.jpeg")

#getting paramters 
params = cv2.SimpleBlobDetector_Params()

#parameter for area filtering 
params.filterByArea = True 
params.minArea = 100 

#parameter for setting circular filtering 
params.filterByCircularity = True 
params.minCircularity = 0.9 

#parameter for setting convexity
#Convexity, in the context of shapes or objects
#refers to a property where any line segement drawn between two points on the boundry of the shape lies entirely within the shape
#Example of convex shapes include circles,ellipses,triangles,rectangles, and polygons
#These shapes have a consistent curvature and do not contain any inward 'curves' or indentations 
params.filterByConvexity = True 
params.minConvexity = 0.2

#parameter for inertia 
params.filterByInertia = True 
params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)
circles = detector.detect(blobby)

#drawing circles on the image 
#np.#zeros is a NumPy function that creates a new list/array with zeros. It is often used to initialise arrays before filling them with actual data 


blank = np.zeros((1,1)) #one row one column 

blobs = cv2.drawKeypoints(blobby,circles,blank,(200,10,30),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) #whereever you found the keypoints of the circle - draw them there
noblobs = len(circles)
text = "Number of circular Blobs: "+str(noblobs)
cv2.putText(blobs,text,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)

cv2.imshow("Blob",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()