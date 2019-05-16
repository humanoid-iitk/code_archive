#!/usr/bin/env python

import rospy
import sys
import numpy as np
import roslib
import cv2
from std_msgs.msg import Float64

cam =cv2.VideoCapture(0)

def publish():
	pub = rospy.Publisher("Obstacle", Float64, queue_size=1)
	Rate = rospy.Rate(1000)
	try:
		while not rospy.is_shutdown():
			ret, frame = cam.read()
			HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			kernal = np.ones((5,5), np.float32)/25
			mask = cv2.filter2D(HSV, -1, kernal)

			rows, cols, val = HSV.shape
			imArea = rows*cols

			top1 = cv2.inRange(HSV[0 : rows/3, 0 : cols], (0, 40, 40), (14, 210, 210))
			top2 = cv2.inRange(HSV[0 : rows/3, 0 : cols], (160, 40, 40), (179, 210, 210))
	
			left1 = cv2.inRange(HSV[3*rows/8 : rows, 0 : cols/4], (42, 40, 40), (90, 210, 210))
			middle1 = cv2.inRange(HSV[3*rows/8 : rows, cols/4 : 3*cols/4], (42, 40, 40), (90, 210, 210))
			right1 = cv2.inRange(HSV[3*rows/8 : rows, 3*cols/4 : cols], (42, 40, 40), (90, 210, 210))

			top = np.zeros((rows/3 + 2, cols + 2), np.uint8)
			middle = np.zeros((5*rows/8 + 2, cols/2 + 2), np.uint8)
			left = np.zeros((5*rows/8 + 2, cols/4 + 2), np.uint8)
			right = np.zeros((5*rows/8 + 2, cols/4 + 2), np.uint8)

			Lmid = np.zeros((5*rows/8 + 2, 3*cols/4 + 2), np.uint8)
			Rmid = np.zeros((5*rows/8 + 2, 3*cols/4 + 2), np.uint8)

			top[1 : rows/3 + 1, 1 : cols + 1] = top1 + top2
			left[1 : 5*rows/8 + 1, 1 : cols/4 + 1] = left1
			middle[1 : 5*rows/8 + 1, 1 : cols/2 + 1] = middle1
			right[1 : 5*rows/8 + 1, 1 : cols/4 + 1] = right1

			Lmid[1 : 5*rows/8 + 1, 1 : cols/4 + 1] = left1
			Lmid[1 : 5*rows/8 + 1, 1 + cols/4 : 3*cols/4 + 1] = middle1

			Rmid[1 : 5*rows/8 + 1, 1 : cols/2 + 1] = middle1
			Rmid[1 : 5*rows/8 + 1, 1 + cols/2 : 3*cols/4 + 1] = right1


			contourTop, hierarchy = cv2.findContours(top, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			contourLeft, hierarchy = cv2.findContours(left, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			contourMiddle, hierarchy = cv2.findContours(middle, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			contourRight, hierarchy = cv2.findContours(right, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

			contourLmid, hierarchy = cv2.findContours(Lmid, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			contourRmid, hierarchy = cv2.findContours(Rmid, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 

			AreaTop = 0
			if len(contourTop) > 0:
				cntTop = max(contourTop, key = cv2.contourArea)
				AreaTop = cv2.contourArea(cntTop)

				if 3*AreaTop/imArea > 0.75:
					pub.publish(2000)

			AreaLeft = 0
			AreaMid = 0
			AreaRight = 0
			if len(contourLeft) > 0: 
				cntLeft = max(contourLeft, key = cv2.contourArea)
				AreaLeft = 32*cv2.contourArea(cntLeft)/(5*imArea)

			if len(contourMiddle) > 0:
				cntMid = max(contourMiddle, key =cv2.contourArea)
				AreaMid = 16*cv2.contourArea(cntMid)/(5*imArea) 

			if len(contourRight) > 0:
				cntRight = max(contourRight, key = cv2.contourArea)
				AreaRight = 32*cv2.contourArea(cntRight)/(5*imArea)

			if AreaMid < AreaRight*(AreaRight < AreaLeft) + AreaLeft*(AreaLeft < AreaRight):

				if AreaLeft < AreaRight:
					if AreaRight < 0.15:
						pub.publish(1000)
					
					else: 
						Mr = cv2.moments(max(contourRmid, key = cv2.contourArea))
						cxr = int(Mr['m10']/Mr['m00'])
						pub.publish(cxr - cols/4.0)

				elif AreaRight < AreaLeft:
					if AreaLeft < 0.15:
						pub.publish(1000)
					else:
						Ml = cv2.moments(max(contourLmid, key = cv2.contourArea))
						cxl = int(Ml['m10']/Ml['m00'])
						pub.publish(cxl - cols/2.0) 

			elif AreaMid >= AreaRight: 
				if AreaLeft > AreaMid:
					if AreaLeft < 0.15:
						pub.publish(1000)
					else:
						Ml = cv2.moments(max(contourLmid, key = cv2.contourArea))
						cxl = int(Ml['m10']/Ml['m00'])
						pub.publish(cxl - cols/2.0)
				else:
					if AreaMid < 0.15:
						pub.publish(1000)
					else:
						Mf = cv2.moments(cntMid)
						cxf = int(Mf['m10']/Mf['m00'])
						pub.publish(cxf - cols/4.0)

			elif AreaMid >= AreaLeft:
				if AreaRight > AreaMid:
					if AreaRight < 0.15:
						pub.publish(1000)
					else:
						Mr = cv2.moments(max(contourRmid, key = cv2.contourArea))
						cxr = int(Mr['m10']/Mr['m00'])
						pub.publish(cxr - cols/4.0)
				else:
					if AreaMid < 0.15:
						pub.publish(1000)
					else:
						Mf = cv2.moments(cntMid)
						cxf = int(Mf['m10']/Mf['m00'])
						pub.publish(cxf - cols/4.0)
			'''
			cv2.imshow("frame", frame)
			cv2.imshow("top", top)
			cv2.imshow("right", right)
			cv2.imshow("left", left)
			cv2.imshow("middle", middle)
			cv2.imshow("Rightmiddle", Rmid)
			cv2.imshow("Leftmiddle", Lmid)

			cv2.waitKey(2)
			'''
			Rate.sleep()

		rospy.loginfo("operation ended")
		cam.release()
		cv2.destroyAllWindows()

	except rospy.ROSInterruptException:
		pass

def main():
	rospy.init_node("ObstacleGuide", anonymous=True)
	publish()



if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
			

