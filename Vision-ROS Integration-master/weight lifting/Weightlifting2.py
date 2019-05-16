import rospy
import numpy as np 
import roslib 
import cv2
import math

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError 

from IMG_proc import Operations as op 
from calliberation import Mapper as mp 

stopCommand = 0
count = 1
MinDist = 20

cam = cv2.VideoCapture(0)

def callback2(data):
	if data.data == 'stop':
		stopCommand = 1
	elif data.data == 'continue':
		stopCommand = 0
	else:
		pass

def callback1(data):
	while(stopCommand):
		pass

	bridge = CvBridge()
	try:
		img = bridge.imgmsg_to_cv2(data, 'bgr8')
	except CvBridgeError as e:
		print(e)

	rows, cols, val = img.shape
	thresh = op().threshGray(img, 195, 255)

	frame = np.zeros((rows + 2, 3*cols/5 + 2), np.uint8)
	frame[1:rows + 1, 1: 3*cols/5 + 1] = thresh[0:rows, cols/5:4*cols/5]

	dist = 15
	success, center = op().findCenterMax(frame)
	if success:
		dist = mp().GetYa(rows/2+1-center[1], 70*np.pi/180)

		if dist < MinDist:
			if count == 1:
				pub.publish("lift")
				count = count + 1
			elif count == 2:
				pub.publish("stop")

		else:
			suc, cnt = op().maxContour(frame)
			if suc:
				[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
				theta = -(math.atan(vy/vx))

				if theta > 0.05:
					pub.publish("anticlock")
				elif theta < -0.05:
					pub.publish("clock")
				else:
					pub.publish("front")

			else:
				print("ERROR: Contour Not Found") 
	else:
		print("ERROR: Center Not Found")

def run():
	rospy.init_node('image_printer', anonymous=True)

	pub = rospy.Publisher("Directions", Sting, queue_size=10)

	image_sub = rospy.Subscriber("MuscleMan", Image, callback1)
	sub = rospy.Subscriber("command", Sting, callback2)

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
