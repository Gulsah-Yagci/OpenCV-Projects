# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 00:59:43 2021

@author: HP
"""

import cv2
import os

# depo
path = "images"

# image size

image_width = 100
image_height = 120

# video capture
capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)
capture.set(10,180)

global countFolder

def saveDataFunc():
    global countFolder
    countFolder = 0
    
    while os.path.exists(path+str(countFolder)):
        countFolder += 1
        
    os.makedirs(path+str(countFolder))
    
saveDataFunc()

# veri toplama

count = 0
countSave = 0

while True:
    success,image = capture.read()
    
    if success:
        image = cv2.resize(image,(image_width,image_height))
        
        if count % 5 ==0:
            
            cv2.imwrite(path+str(countFolder)+"/"+str(countSave)+"_"+".png",image)
            countSave += 1
            
            print(countSave)
            
            cv2.imshow("Image",image)
            
    if cv2.waitKey(1) & 0xFF == ord("q"):break
    
capture.release()
cv2.destroyAllWindows()
            










