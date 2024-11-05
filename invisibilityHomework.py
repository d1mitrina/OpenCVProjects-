import cv2
import numpy as np 
import time 

count = 0
background  = 0

raw_video = cv2.VideoCapture("InvisibilityHW/hw.mp4")
time.sleep(1)

for i in range(61):
    return_value, background = raw_video.read()
    if return_value == False:
        continue
background = np.flip(background,axis=1)


while raw_video.isOpened():
    return_value, image = raw_video.read()
    if not return_value: 
        break 
    count+=1 
    image = np.flip(image,axis=1)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    start = np.array([40,100,40])
    end = np.array([255,100,255])
    
    mask1 = cv2.inRange(hsv,start,end)  
    
    start1 = np.array([40,155,40])
    end1 = np.array([255,180,255])
    mask2 = cv2.inRange(hsv,start1,end1)
    mask1 = mask1 + mask2  
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 2)
    mask1 = cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1) 
    mask2 = cv2.bitwise_not(mask1) 
    res1 = cv2.bitwise_and(background, background, mask = mask1)
    res2 = cv2.bitwise_and(image, image, mask = mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)


    cv2.imshow("INVISIBLE MAN", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break