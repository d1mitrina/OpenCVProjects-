#1 - Imports 
import cv2
import sys
import os
import numpy as np

#2 - Creating Variabls
haar = "faceRecognition1/haarcascade_frontalface_default.xml"
data_set = "faceRecognition1/dataset"
size = 4
print ("Ensure lighting is sifficient, please wait recognising face... ")
names = {}
labels =[]
images = []
id = 0 

for (subdir,dir,files) in os.walk(data_set):  #walk is a function that will guide you through data set one by one 
    for subdir in dir:
        names[id] = subdir  #subdir is the parent directory 
        subject_path = os.path.join(data_set,subdir) #combining path of folder with the full access 
    

#3 - Image proccessing

for i in os.listdir(subject_path): #function that lists all the directories under a folder 
    path = os.path.join(subject_path,i)
    label = id
    img = cv2.imread(path,0) #0 used as it reads the images in grayscale 

#4 - Image Resizing

img = cv2.resize(img, (130,100))

#5 - Data Collection

images.append(img)
labels.append(label)
id+=1


#6 - Images are concverted into numerical numbers using NumPy

images = np.array(images) #converting all images into numbers using np.array 
print(images)
labels = np.array(label)

#7 - Call ML Model for face recognition (FACE RECOGNISER)

recogniser = cv2.face.LBPHFaceRecognizer_create()
recogniser.train(images,labels)


#8 - Create a set- up for face detection 

face_capture = cv2.CascadeClassifier(haar) #this function is used to call your ML model 
webcam = cv2.VideoCapture(0) 

#9 - Face detection Loop

while True: 
    (_,im) = webcam.read() #webcam reading a picture and assigns its own name
    grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #converts into grey --> minimum requiremnet for machine learning model to undertsnad requirement.This is because some color holds its specific numbers  
    faces = face_capture.detectMultiScale(grey,1.3,4) #numbers given to grey color 
    
    for (x,y,w,h) in faces:
        face = grey[y:y+h,x:x+w]
        face_resized = cv2.resize(face,(130,100))
        prediction = recogniser.predict(face_resized)
        if prediction[1] < 500: #confidence percentage 
            confidence = int(100 * (1 - (prediction[1] / 300))) #formula for converting percentage into confidence form 
            cv2.putText(im, f'{names[prediction[0]]} - {confidence}%', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
        else: 
            cv2.putText(im, 'Not recognized', (x - 10, y - 10),cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
    
    cv2.imshow("Face Recognition",im)
    key = cv2.waitKey(10) #needs to wait for 10 miliseconds for 30 pics to be captured 
    if key == 27: #27 means you are pressing escape key. 
        break
cv2.destroyAllWindows()





















