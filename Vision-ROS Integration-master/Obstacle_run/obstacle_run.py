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
# min_green = (40, 130, 60)
# max_green = (80, 255, 255)s

# # HSV values for bull's eye
# min_orange = (0, 120, 117)
# max_orange = (15, 250, 192)


# # HSV values for yellow board
# min_orange = (20, 100, 100)
# max_orange = (30, 255,255)




#HSV_MIN=[90,100,100]
#HSV_MAX=[120,255,255]

HSV_MIN=[0,0,0]
HSV_MAX=[0,0,0]
r_min=5


#cap=cv2.VideoCapture(0)

n=10




def analyser(data):
    tolerance=1000
    pub = rospy.Publisher('/image_processing/ball_coordinates', Point, queue_size=1)
    rate = rospy.Rate(5000)
    global HSV_MIN
    global HSV_MAX
    steps=[0]
    
    X=[0,0]
    length_old = 0
    length_new = 0

    frame = bridge.imgmsg_to_cv2(data, "bgr8")
    #frame = cv2.imread('/home/lucy/Desktop/green.jpg',1)
    cv2.imshow("frame" , frame)
    cv2.waitKey(1)
    
 
    blurred = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    HSV_MIN1=(HSV_MIN[0],HSV_MIN[1], HSV_MIN[2])
    HSV_MAX1=(HSV_MAX[0],HSV_MAX[1], HSV_MAX[2])
    mask = cv2.inRange(hsv, HSV_MIN1, HSV_MAX1)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('image',mask)
    cv2.waitKey(1)
    

    

    (I,J) = np.shape(mask)
    print(I,J)
    print("next frame")
    
    no_of_steps = int((I+1)/n) 

    a=0
    
    for i in range (0 , no_of_steps) :
        X=[0,0]
        length_old = 0
        length_new = 0
	a=0
        print(i)
        for j in range (0 , J) :
            
	    if mask[I-n/2-i*n][j] :
                a=1
                #print("next2")
                #print(I-n/2-i*n)
		if mask[I-n/2-i*n][j-1] :
		    X[1] = j
                    length_new = j-X[0]
                    thej=j
                else :
		    X[0]=j
            else :
                X=[0,0]
		if length_new > length_old :
		    length_old = length_new
                    
		    appending_no = int(thej-length_old/2)
                    end_points=[thej-length_old , thej]
                    
                    #print(abs(steps[len(steps)-1]-steps[len(steps)-2]))
                    
                    
	
        if a :
            steps.append(appending_no)
            print(steps)
            print(end_points)
            a=0
        
        if abs(len(steps)>2) and (abs(steps[len(steps)-1]-steps[len(steps)-2]) > tolerance ):
            break		   
            	
	


    rate.sleep()
    






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
    sub2=rospy.Subscriber('HSV_MAX_VALUES', Point , hmax)
    sub3=rospy.Subscriber('HSV_MIN_VALUES', Point , hmin)
    sub = rospy.Subscriber('image', Image, analyser)
    rospy.spin()
   
    

    


       




