#!/usr/bin/env python
import rospy
import numpy as np 
import roslib 
import cv2
import math
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 

from IMG_proc import Operations as op 
from calliberation import Mapper as mp 

stopCommand = 0
count = 1
MinDist = 17

cam = cv2.VideoCapture(2)

def callback2(data):
	'''if data.data == 'stop':
		stopCommand = 1
	elif data.data == 'continue':
		stopCommand = 0
	else:
		pass

	'''

def imp() :
	while True :

		global MinDist
		global count

		pub = rospy.Publisher("Directions", String, queue_size=10)
		
		try:
			_,img = cam.read()
			cv2.imshow("image", img)
			if cv2.waitKey(30) & 0xff == ord('q'):
				break
		except CvBridgeError as e:
			print(e)
		#if stopCommand:
		#	continue


		rows, cols, val = img.shape
		thresh = op().threshGray(img, 195, 255)

		frame = np.zeros((rows + 2, 3*cols/5 + 2), np.uint8)
		frame[1:rows + 1, 1: 3*cols/5 + 1] = thresh[0:rows, cols/5:4*cols/5]

		dist = 17
		success, center = op().findCenterMax(frame)
		print(count)
		print(MinDist)
		if success:
			dist = mp().GetYa(rows/2+1-center[1], 55*np.pi/180)
			print(dist)

			if dist < MinDist:
				if count == 1:
					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					time.sleep(5)
					
				        MinDist= 45 
					for i in range (1,9) :					
						_,img = cam.read()
					count = count + 1
				elif count == 2:
					pub.publish("pk")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					count=count+1
					MinDist = 17
				elif count == 3:
					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					pub.publish("f")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()

					time.sleep(5)
					MinDist = 45 
					for i in range (1,9) :					
						_,img = cam.read()				
					count =count+1

				
				elif count == 4:
					pub.publish("lt")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()
					count=count+1
					MinDist=0
		                

								


			else:
				suc, cnt = op().maxContour(frame)
				if suc:
					[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
					theta = -(math.atan(vy/vx))

					if theta > 0.05:
						if count == 1 or count == 2:
							pub.publish("cc")
						if count == 3 or count==4:
							pub.publish("pcc")
						if count == 5:
							pub.publish("lcc")
					elif theta < -0.05:
						if count == 1 or count == 2:
							pub.publish("c")
						if count == 3 or count==4:
							pub.publish("pc")
						if count == 5:
							pub.publish("lc")
					else:
						if count == 1 or count == 2:
							pub.publish("f")
						if count == 3 or count==4:
							pub.publish("pf")
						if count == 5:
							pub.publish("lf")
					time.sleep(1)
					for i in range (1,9) :					
						_,img = cam.read()
					
				else:
					print("ERROR: Contour Not Found") 
		else:
			print("ERROR: Center Not Found")

def run():
	rospy.init_node('image_printer', anonymous=True)

	pub = rospy.Publisher("Directions", String, queue_size=10)

	
	sub = rospy.Subscriber("command", String, callback2)
        imp()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass

def main():

	run()
	rospy.loginfo("Operation Ended")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
