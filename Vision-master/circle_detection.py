'''
Function: Detects largest circle lying in the given HSV range
Author: Madhur Deep Jain
'''

import cv2
import numpy as np

def nothing(self):
    pass

cap = cv2.VideoCapture(0)

# # HSV values for tennis ball
# min_green = (30, 130, 60)
# max_green = (50, 255, 255)

# # HSV values for bull's eye
# min_orange = (0, 120, 117)
# max_orange = (15, 250, 192)

cv2.namedWindow('trackbars')

hl='H_MIN'
hh='H_MAX'
sl='S_MIN'
sh='S_MAX'
vl='V_MIN'
vh='V_MAX'
rad='R_MIN'

cv2.createTrackbar(hl, 'trackbars', 30, 179, nothing)
cv2.createTrackbar(hh, 'trackbars', 50, 179, nothing)
cv2.createTrackbar(sl, 'trackbars', 130, 255, nothing)
cv2.createTrackbar(sh, 'trackbars', 255, 255, nothing)
cv2.createTrackbar(vl, 'trackbars', 60, 255, nothing)
cv2.createTrackbar(vh, 'trackbars', 255, 255, nothing)
cv2.createTrackbar(rad, 'trackbars', 5, 100, nothing)

while(True):
    _, frame = cap.read()

    h_min = cv2.getTrackbarPos(hl, 'trackbars')
    h_max = cv2.getTrackbarPos(hh, 'trackbars')
    s_min = cv2.getTrackbarPos(sl, 'trackbars')
    s_max = cv2.getTrackbarPos(sh, 'trackbars')
    v_min = cv2.getTrackbarPos(vl, 'trackbars')
    v_max = cv2.getTrackbarPos(vh, 'trackbars')
    r_min = cv2.getTrackbarPos(rad, 'trackbars')

    blurred = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    HSV_MIN=np.array([h_min, s_min, v_min])
    HSV_MAX=np.array([h_max, s_max, v_max])

    mask1 = cv2.inRange(hsv, HSV_MIN, HSV_MAX)
    mask = cv2.erode(mask1, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0]
    center = None

    if len(cnts) > 0:
        cnt = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        if radius > r_min:
            M = cv2.moments(cnt)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            print (center)
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    cv2.imshow('mask', mask)
    cv2.imshow('mask1',mask1)
    cv2.imshow('blurred',blurred)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows( )
