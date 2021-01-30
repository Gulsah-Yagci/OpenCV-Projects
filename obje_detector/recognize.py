# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:53:05 2021

@author: HP
"""

import cv2

name = "Gulsah"
frameWidth = 280
frameHeight = 360
color = (255,0,0)

capture = cv2.VideoCapture(0)
capture.set(3,frameWidth)
capture.set(4,frameHeight)


def empty(a):pass

#trackbar
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neighbor","Result",4,50,empty)

# cascade classifier

cascade = cv2.CascadeClassifier("C:\\Users\\HP\Desktop\\obje_detector\\cascade.xml")

while True:
    
    # read image
    success,image = capture.read()
    
    if success:
        # convert bgr2gray
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        #detection parameters
        scaleVal = 1+ (cv2.getTrackbarPos("Scale","Result")/1000)
        neighbor = cv2.getTrackbarPos("Scale","Result")
        
        #detection
        rects = cascade.detectMultiScale(gray,scaleVal,neighbor)
        
        for (x,y,w,h) in rects:
            cv2.rectangle(image,(x,y),(x+w,y+h),color,3)
            cv2.putText(image,name,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            
        cv2.imshow("Result",image)
        
    if cv2.waitKey(1) & 0XFF == ord("q"):break
    
capture.release()
cv2.destroyAllWindows()  
    
                   
                   
                   



