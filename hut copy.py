#using funcation to create a hut 

import cv2
import numpy as np
image = cv2.imread("Lesson4.shapes/cat.jpg")


def draw_rect(x,y,a,b):
    global image
    start = (x,y)
    end = (a,b)
    color = (255,0,0)
    border = 1
    image = cv2.rectangle(image, start, end, color, border)

def draw_line(x,y,a,b):
    global image 
    start = (x,y)
    end=(a,b)
    color = (255,0,0)
    border = 1
    image =cv2.line(image, start, end, color, border)


draw_rect(200,200,300,300)

draw_line(200,200,250,100)
draw_line(200,100,300,200)


cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()



cv2.imshow('Hut',image)
cv2.waitKey(0)
cv2.destroyAllWindows()