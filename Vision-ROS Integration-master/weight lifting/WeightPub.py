#!/usr/bin/env python

'''
	TEAM HUMANOID, ROBOTICS CLUB, IIT KANPUR.
'''

#import required libraries.
import rospy
import numpy
import sys
import roslib
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
import numpy as np

#initialise camera variable.
cam = cv2.VideoCapture(1)

#define a function to capture images, translate them into image message and publish on the topic.
def camera():
	
	#initialise publisher node.
	image_pub = rospy.Publisher("MuscleMan", Image, queue_size=1)
	
	#initialise translation module.
	bridge = CvBridge()
	
	#define a time interval for halting the program.
	Rate = rospy.Rate(1000)

	#Try to capture images from the camera, translate and publish the message.
	try: 
		while not rospy.is_shutdown():
			rel, cv_image = cam.read()

			#publish the message to a ros topic, halt the programme for a while.
			image_pub.publish(bridge.cv2_to_imgmsg(cv_image, "bgr8"))
			Rate.sleep()

		#update log info when programme ends.
		rospy.loginfo("operation ended")
		
		#shut down the camera, close all active windows.
		cam.release()
		cv2.destroyAllWindows()

	#report error if the above computation fails.
	except CvBridgeError as e:
		print(e)

#Define main function to initialise the node.
def main():
	
	#initialise the node.
	rospy.init_node('imgPublisher', anonymous=True)
	
	#call the camera function to do all the processing.
	camera()
	
#This is a ROS integrated program that is called using rosrun command from the terminal.
if __name__ == '__main__':
	
	#Run the program on recieving command from the user.
	try:
		main()
	#End operation on interruption.	
	except rospy.ROSInterruptException:
		pass