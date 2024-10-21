#in order to create a video, all images must be of the same size

import cv2
import os #operating system 
from PIL import Image  #pillow image processing library

image_folder = r"/Users/yanigrazhdani/Documents/pics" #this mean that the image folder is readable 
#must be taken from laptop documents instead of visual studio folder to eliminate a clash 

os.chdir(image_folder) #change in directory / folder

#required for resizing images in generation of videos
mean_height = 0
mean_width = 0

#for how many files/pictures there are in a folder/directory, the variable will save the files which only have the suitable extentions of images
number_of_images = len([i for i in os.listdir(image_folder)if i.endswith((".jpg",".jpeg",".png"))])

for i in os.listdir(image_folder):
    if i.endswith((".jpg",".jpeg",".png")):
        im = Image.open(os.path.join(image_folder,i))
        width,height = im.size #returns width and height of the image 
        mean_width+=width 
        mean_height+=height 
    

#calculating the mean of the images widths and heights 
mean_width = int(mean_width/number_of_images)
mean_height = int(mean_height/number_of_images)

for i in os.listdir(image_folder):
    if i.endswith((".jpg",".jpeg",".png")):
        im = Image.open(os.path.join(image_folder,i))
        imresize = im.resize((mean_width, mean_height),Image.LANCZOS) #gives you properties of image 
        imresize.save(i,"JPEG",quality = 95) #95% quality

def videoGenerator():
    video_name = "MyFirstVideo.mp4"

    os.chdir(r'/Users/yanigrazhdani/Documents/pics')

    images = []
    for img in os.listdir('.'):
        if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png'):
            images.append(img)
    
    
    print(images)
    
    frame = cv2.imread(os.path.join(".", images[0]))
    
    height, width, layers = frame.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  
    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height)) 

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))

    cv2.destroyAllWindows()
    video.release()

videoGenerator()