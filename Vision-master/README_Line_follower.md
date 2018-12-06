# Read Me:- Line_follower.py  
 ## Table of Contents  
 
- [Background](#background)  
- [Explanation](#explanation)  
- [Related Efforts](#related-efforts)  
- [Maintainers](#maintainers)  
- [Contributors](#contributors)  
- [License](#license)  
 


## Description:
Read_me is written to facilitate the understanding of the code.  
```sh


import numpy as np
import cv2


#imports required libraries


```


 


```sh


def track():
        pass


#creates an empty function to be passed while creating trackbars


```


 


```sh


cv2.namedWindow("control")
cv2.createTrackbar("threshMin", "control", 60, 255, track)


#creates trackbar to calibrate threshold value.


```


 


```sh


video_capture = cv2.VideoCapture(0)


#switches on the camera.


```


 


```sh


ret, frame = video_capture.read()


#reads frames from the camera.


```


 


```sh


imx, imy, s = frame.shape


#get dimentions of the frame.


```


 


```sh


crop_img = frame[(2*imx)/3 : (3*imx)/4 , 0 : imy - 0]


#cropes the image.


````


 


```sh


threshMin = cv2.getTrackbarPos("threshMin", "control")
gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)


#convertes cropped image to greyscale.


##IF BACKGROUND IS DARKER THAN LINE ADD THIS TO THE CODE.
#gray = cv2.bitwise_not(gray)


```


 


```sh


kernal = np.ones((5,5), np.float32)/25
mask = cv2.filter2D(gray, -1, kernal)
ret,thresh = cv2.threshold(mask,threshMin,255,cv2.THRESH_BINARY_INV)


#blur to remove noice and convert to binary image.


```


 


```sh


rel, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


#get contours of cropped image.


```


 


```sh


if len(contours) > 0:


#check if contours is empty.


```


 


```sh


cnt = max(contours, key = cv2.contourArea)


#find contour with maximum area.


```


 


```sh


x, y, w, h = cv2.boundingRect(cnt)
cx = float(x)


#find coordinates of vertices of its bounding rectangle.


```


 


```sh


t = float(1.0 - 2.0*(cx /(imx - 20.0)))*5


#find relative position of bounding rectangle wrt center line in form of a parameter t.


```


 


```sh


move = ' '
if t > -0.20 and t < 0.20:
        move = 'f'
elif t <= -0.20:
        move = 'r'
elif t >= 0.20:
        move = 'l'
print(move, t)


#print ‘f’, ‘r’ or ‘l’ according to position.


```


 


```sh


cv2.drawContours(crop_img, [cnt], -1, (255,255,0), 3)


#draw contours of the line.


```


 


```sh


cv2.imshow('frame',frame)
cv2.imshow('thresh',thresh)
cv2.imshow('crop_img',crop_img)


# display images showing thresh image, crop image and the original image.


```


 


```sh


if cv2.waitKey(1) & 0xFF == ord('q'):
break


# wait for user to press q from the keyboard, exit on receiving input.


```


 


```sh


video_capture.release()
cv2.destroyAllWindows()


#turn off the camera.


```


 
 
## Background  
Line_follower was first written in c++ under the summer project of Humanoid club, IIT kanpur.


It was written by Mrinal Dogra to work with a biped developed indigenously by the Club.


 


The code was updated by Madhur Deep Jain and Shashi Kant and is currently being moderated by Deepankur Kansal And Paras Mittal.


 
## Usage  
Click on the file Line_follower.py to get the full code.  
 


## Explanation


 


The program finds the coordinates of the boundary of the segment of the line inside a narrow strip of image frame near the bot.


 


Using mathematical operations the position of line relative to the centerline of the image frame is found out and accordingly 'r', 'l' or 'f' which mean right, left and front respectively, are printed depicting the direction in which the bot should move to reach the line.


 


These characters are stored in the variable 'move' which can be passed to the ros for giving command to the bot to move in the desired direction.


 


Parameter t (line 102) has been calculated by taking ratio of the x coordinate of the bounding rectangle with the total width of the cropped image, and then subtracting it from 1, giving its relative position.


In the end multiply it by 5 to give some window for approximate comparison and account for whatever physical dimensions the line has.


 


if t is negative, line is on right side of center line, if positive, line is on left side, else in the center. we keep a range of 0.20 on either side to fit in the width of the line.


 


 
## Related Efforts  
Under Construction  
## Maintainers  
 
[@Deepankur Kansal]([https://github.com/DeepankurK](https://github.com/DeepankurK)).


[@Paras Mittal](https://github.com/Paras69/)  
 
## Contributors  
[@Shashi Kant](https://github.com/shashikg)
[@Madhur Deep Jain](https://github.com/madhurdeepjain)  
## License  
[IITK](LICENSE) © HUMANOID CLUB
