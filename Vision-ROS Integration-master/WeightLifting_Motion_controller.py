#!/usr/bin/env python

'''
	TEAM HUMANOID, ROBOTICS CLUB, IIT KANPUR.

'''

#Import required libraries.
from __future__ import print_function
import rospy
import numpy as np
import roslib
import sys
import cv2
import math
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

#This constant represents the location at which the code has to stop for 5 seconds.
#constant = 

#define callback funtion that takes data from the topic and performs image processing operations.
def callback(data):
	
	#load the function that translates the image message to numpy array.
	bridge = CvBridge()
	
	#Try to translate thr message, in fails report the error.
	try:
		cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
	except CvBridgeError as e:
		print(e)

	#Get the dimensions of the image.	
	rows, cols, val = cv_image.shape
	
	#Convert the image to grayscale.
	cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
	
	#Threshold the image to get only the white part.
	ret, thresh = cv2.threshold(cv_image, 250, 255, cv2.THRESH_BINARY)
	
	#create an empty 'frame' image for cropping and adding a border to the original image.
	frame = np.zeros((2*rows/3 + 2, 3*cols/5 + 2), np.uint8)
	
	#blur the image for processing it.
	kernal = np.ones((5, 5), np.float32)/25
	mask = cv2.filter2D(thresh, -1, kernal)
	
	#Add the relavent part of the image to the frame created earlier.
	frame[1 : 2*rows/3 + 1, 1 : 3*cols/5 + 1] = mask[rows/3 : rows, cols/5 : 4*cols/5]
	
	'''
	#This is the idea I was using earlier.

	edges = cv2.Canny(frame, 50, 150, apertureSize = 1)
	lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
	
	for rho, theta in lines[0]:
		if abs(theta - eps) > 0 and abs(theta - eps) < np.pi/2:
			print("anticlock")
		elif abs(theta - eps) < 0 or abs(theta - eps) > np.pi/2:
			print("clock")
	'''
	
	#Get the contour features of the image.
	rel, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	##Used for debugging: #print(lines)
	
	#check if there are detectable features in the image.
	if len(contours) > 0:
		
		#find the active region with max area(to remove background elements and focus on the line.)
		cnt = max(contours, key = cv2.contourArea)
		
		#If the line area reaches a certain value, hault the program for 5 seconds.
		#if cv2.contourArea(cnt) > constant:
		#	cv2.waitKey(5000)
		
		'''
		Another Idea I used earlier. 

		rect = cv2.minAreaRect(cnt)
		#print(rect[2])
		theta = (-rect[2])*np.pi/180
		'''

		#Get data about the best fitting line.
		[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
		
		#Get inclination of this line.
		theta = -(math.atan(vy/vx))
		##Used for calliberation: #print (theta)

		#check the orientation of the line and direct the bot accordingly.
		if theta > 0.05:
			print("anticlock")
		elif theta < -0.05:
			print("clock")
		elif theta > -0.05 and theta < 0.05:
			print("front")

	#display the processed image, for calliberation.
	cv2.imshow("Image Window1", frame)
	cv2.waitKey(3)

#Define a function to initalise the node and run the callback function.
def run():
		
		#initialise the node.
		rospy.init_node('image_printer', anonymous=True)
		
		#Tell the node to recieve data from a certain topic.
		image_sub = rospy.Subscriber("MuscleMan", Image, callback)
		
		#Keep the program spinning.	
		try:
			rospy.spin()
		except KeyboardInterrupt:
			pass

#Define the main function.
def main():
	
	#Call the initialising function.
	run()

	#update log info when the program stops.
	rospy.loginfo("Operation Ended")
	
	#Close all active windows.
	cv2.destroyAllWindows()

#This is a ROS integrated program, so it has to be called using rosrun command.
#so this part recieves the command from terminal and starts processing.
#Try to run the main funtion, report eroor if failed.
if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass