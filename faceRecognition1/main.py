import cv2
import sys
import os

haar = "faceRecognition1/haarcascade_frontalface_default.xml"
data_set = "faceRecognition1/dataset" #machine learning model applied to our code 
sub_folder = "dimi"
path = os.path.join(data_set,sub_folder) #path od dataset 

if not os.path.isdir(path): #is directory. If path doesnt exist, it will create its own folder
    os.mkdir() #make directory


#widgth and height of gthe image that the camera is going to capture
width = 130
height = 100

face_capture = cv2.CascadeClassifier(haar) #this function is used to call your ML model

webcam = cv2.VideoCapture(0) #0 means it will capture exact image - only face will be captured 
count = 1
while count <30:
    (_,im) = webcam.read() #webcam reading a picture and assigns its own name
    grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #converts into grey --> minimum requiremnet for machine learning model to undertsnad requirement.This is because some color holds its specific numbers  
    faces = face_capture.detectMultiScale(grey,1.3,4) #numbers given to grey color 
    
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),5) #2 --> thickness of rectangle
        face = grey[y:y+h,x:x+w]
        face_resized = cv2.resize(face,(width,height))
        cv2.imwrite('% s/% s.png'%(path,count),face_resized) #% s gives a random number 
        count+=1
    cv2.imshow("opencv",im) # displays frames
    key = cv2.waitKey(10) #needs to wait for 10 miliseconds for 30 pics to be captured 
    if key == 27:
        break #exits the while loop 

webcam.release()
cv2.destroyAllWindows()















