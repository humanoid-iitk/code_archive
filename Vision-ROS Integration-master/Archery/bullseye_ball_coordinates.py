#!/usr/bin/env python
import cv2
import rospy
import time
import numpy as np
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from cv_bridge import CvBridge
def f ():
    pass

bridge = CvBridge()

# # HSV values for tennis ball
# min_green = (30, 130, 60)
# max_green = (50, 255, 255)s

# # HSV values for bull's eye
# min_orange = (0, 120, 117)
# max_orange = (15, 250, 192)

HSV_MIN=(0, 120, 117)
HSV_MAX=(15, 250, 255)
r_min=5


'''cv2.createTrackbar('H_min', 'H_min', 0,360,f)
cv2.createTrackbar('H_max', 'H_max', 0,360,f)
cv2.createTrackbar('S_min', 'S_min', 0,255,f)
cv2.createTrackbar('S_max', 'S_max', 0,255, f)
cv2.createTrackbar('V_min', 'V_min', 0,255, f)
cv2.createTrackbar('V_max', 'V_max', 0,255, f)
'''

#cap=cv2.VideoCapture(0)


global key
key=1
	
def ball_detector(data):
    pub = rospy.Publisher('/image_processing/ball_coordinates', Point, queue_size=1)
    rate = rospy.Rate(100000)
    
    global HSV_MIN
    global HSV_MAX
    '''HSV_MIN=(cv2.getTrackbarPos('H_min','H_min'),cv2.getTrackbarPos('S_min','S_min'),cv2.getTrackbarPos('V_min','V_min'))
    HSV_MAX=(cv2.getTrackbarPos('H_max','H_max'),cv2.getTrackbarPos('S_max','S_max'),cv2.getTrackbarPos('V_max','V_max'))
    
    '''
    

    frame = bridge.imgmsg_to_cv2(data, "bgr8")
   # _,frame=cap.read()
    #frame = cv2.imread('/home/lucy/Templates/tennis.jpg', -1)
    blurred = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    HSV_MIN1=(HSV_MIN[0],HSV_MIN[1], HSV_MIN[2])
    HSV_MAX1=(HSV_MAX[0],HSV_MAX[1], HSV_MAX[2])
   

    mask = cv2.inRange(hsv, HSV_MIN, HSV_MAX)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    
    #print(time.time())
    cv2.imshow('image',mask)
    cv2.waitKey(1)
    _,cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   # cnts = cnts[0]
    center = None
    #print(len(cnts))	
    if len(cnts) > 0:
        cnt = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
	print('reached here')
        if radius > r_min:
            M = cv2.moments(cnt)
           # coordinates=Point(float(M["m10"]/M["m00"]),float(M["m01"]/M["m00"]),float(radius))
            coordinates=Point(float(x),float(y),float(radius))
            print(float(radius))

        else:
            coordinates = Point(-1.0,-1.0,-1.0)
    else:
        coordinates = Point(-1.0,-1.0,-1.0)

    pub.publish(coordinates)
    rate.sleep()
    print(time.time())



def switch (data):
    global key
    key=data.x

def hmin(data):
    global HSV_MAX 
    HSV_MIN[0]=data.x
    HSV_MIN[1]=data.y
    HSV_MIN[2]=data.z

def hmax(data):
    global HSV_MAX 
    HSV_MAX[0]=data.x
    HSV_MAX[1]=data.y
    HSV_MAX[2]=data.z

if __name__=='__main__':

    
    rospy.init_node('ball_detector', anonymous=True)
    sub1 = rospy.Subscriber('switch', Point, switch)
    sub2=rospy.Subscriber('HSV_MAX_VALUES', Point , hmax)
    sub3=rospy.Subscriber('HSV_MIN_VALUES', Point , hmin)
    sub = rospy.Subscriber('image', Image, ball_detector)
    
    
    while key:



	time.sleep(.1)

        
	    	    


       





