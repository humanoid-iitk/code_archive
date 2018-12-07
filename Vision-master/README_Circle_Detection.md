# Read Me:- Circle_Detection.py

## Table of Contents

-[Description](#description)

- [Background](#background)

- [Explanation](#explanation)

- [Shortcomings](#shortcomings)

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

def nothing(self):
	pass

#Empty function to be passed while creating trackbars.

```

  

```sh

cap = cv2.VideoCapture(0)

#turn on the camera.

```

  
  

```sh

cv2.namedWindow('trackbars')

#create a window for putting trackbars.

```

  

```sh

hl='H_MIN'
hh='H_MAX'
sl='S_MIN'
sh='S_MAX'
vl='V_MIN'
vh='V_MAX'
rad='R_MIN'

#Store Trackbar names in variables.

```

  

```sh

cv2.createTrackbar(hl, 'trackbars', 30, 179, nothing)
cv2.createTrackbar(hh, 'trackbars', 50, 179, nothing)
cv2.createTrackbar(sl, 'trackbars', 130, 255, nothing)
cv2.createTrackbar(sh, 'trackbars', 255, 255, nothing)
cv2.createTrackbar(vl, 'trackbars', 60, 255, nothing)
cv2.createTrackbar(vh, 'trackbars', 255, 255, nothing)
cv2.createTrackbar(rad, 'trackbars', 5, 100, nothing

#Creates Trackbars.

```

  

```sh

_, frame = cap.read()

#read image frames from the camera

```

  

```sh

h_min = cv2.getTrackbarPos(hl, 'trackbars')
h_max = cv2.getTrackbarPos(hh, 'trackbars')
s_min = cv2.getTrackbarPos(sl, 'trackbars')
s_max = cv2.getTrackbarPos(sh, 'trackbars')
v_min = cv2.getTrackbarPos(vl, 'trackbars')
v_max = cv2.getTrackbarPos(vh, 'trackbars')
r_min = cv2.getTrackbarPos(rad, 'trackbars')

# read values from trackbars.

```

  

```sh

kernal = np.ones((5,5), np.float32)/25
blurred = cv2.filter2D(frame, -1, kernal)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

#blur the image and convert color coding to HSV.

```

```sh

HSV_MIN=np.array([h_min, s_min, v_min])
HSV_MAX=np.array([h_max, s_max, v_max])

#create arrays for storing minimum and maximum HSV values.

```

  

```sh

mask = cv2.erode(mask1, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

#reduce noise.

```

  

```sh

rel, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#find contours in the image.

```

  

```sh

if len(cnts) > 0:

#check if cnts(containing contour arrays) is non empty.

```

  

```sh

cnt = max(cnts, key=cv2.contourArea)

#find the region with maximum area.

```

```sh

((x, y), radius) = cv2.minEnclosingCircle(cnt)

#get center and radius of the smallest circle enclosing the ball.

```

  

```sh

if radius > r_min:

#check if ball is large enough.

```

  

```sh

M = cv2.moments(cnt)
center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
print (center)

#find the center of the contour(ball).

```

  

```sh

cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
cv2.circle(frame, center, 5, (0, 0, 255), -1)

#draw two circles: one showing boundary of the ball, other the center.

```

  

```sh

cv2.imshow('mask', mask)
cv2.imshow('mask1',mask1)
cv2.imshow('blurred',blurred)
cv2.imshow('frame', frame)

#display relevant images.

```

```sh

if cv2.waitKey(1) & 0xFF == ord('q'):
	break 

#ask the system to wait for user to press Q, exit the loop on receiving the input.

```

  

```sh

cap.release()
cv2.destroyAllWindows()

#release the camera and close all windows.

```

  
  

## Background

Line_follower was first written under the summer project of Humanoid club, IIT kanpur.

  

It was written by Mrinal Dogra to work with a small scale humanoid developed indigenously by the Club.

It worked perfectly at the time of final testing.

  

The code was updated by Madhur Deep Jain and Shashi Kant and is currently being moderated by Deepankur Kansal And Paras Mittal.

## Usage

Click on the file Circle_Detection.py to get the full code.

## Explanation

The program finds the coordinates of the boundary of the Largest Circle in camera feed in the given hsv values and marks the boundary of the circle alongwith its centre.

  

There is a window named ‘trackbars’ to adjust the minimum and maximum hsv values and minimum radius.

  

Using opencv functions operations the largest circle contour is found after which the center and boundary is plotted on the ‘frame’ for the circle.

The coordinates are stored in ‘center’ which can be subscribed to a file.

## Shortcomings

1.The code depends on the color of the circle/ball.

2.If the image frame has some region other than the ball having the same color, and has a larger area, the code reports the center of that area.

  

3.Cannot detect balls/circles of different colors together.

  

4.Finds center of only one circle/ball.

  
5 Have to calibrate manually using trackbars.

## Maintainers

[@Deepankur Kansal]([https://github.com/DeepankurK](https://github.com/DeepankurK)).

  

[@Paras Mittal](https://github.com/Paras69/)

## Contributors

[@Shashi Kant](https://github.com/shashikg)

## License

[IITK](LICENSE) © HUMANOID TEAM
