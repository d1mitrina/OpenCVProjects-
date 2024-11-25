import cv2 
import sys 
import os 
import numpy as np

capture = cv2.VideoCapture("LastLessonCarDetection/cara.mp4")
ml = cv2.CascadeClassifier("LastLessonCarDetection/cars.xml")#identifies vehicles 

while True:
    number, frames = capture.read()
    grey = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY) #convert colour = cvt 
    cars = ml.detectMultiScale(grey,1.1,1) #1.1, 1 are the different sizes of cars 
    for (x,y,w,h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,100,255),2) #2 means sides
    cv2.imshow("Car Detection Video", frames)
    key = cv2.waitKey(10)
    if key == 27:
        break
cv2.destroyAllWindows()
