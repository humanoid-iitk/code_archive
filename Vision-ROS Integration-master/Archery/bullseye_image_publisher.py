#!/usr/bin/env python
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy
import time
bridge = CvBridge()

cap = cv2.VideoCapture(2)

def talker():
    pub = rospy.Publisher('image', Image, queue_size=10)
    rospy.init_node('image_publisher', anonymous=True)
    rate = rospy.Rate(100000)
    #frame=cv2.imread('/home/lucy/Templates/tennis.jpg',0)
    #cv2.imshow('image',frame)
    #,frame=cap.read()
    #cv2.imshow('image',frame)
    
    while not rospy.is_shutdown():
        _,frame = cap.read()
        
        cv2.imshow('raw',frame)
        cv2.waitKey(1)
        raw_image = bridge.cv2_to_imgmsg(frame,encoding='bgr8')
	print(time.time())
        pub.publish(raw_image)
        print(time.time())
        
        rate.sleep()
       	
        
if __name__ == '__main__':
    try:
	talker()
       

    except rospy.ROSInterruptException:
        pass
