#!/usr/bin/env python
import rospy
import cv2
import numpy as np 
import time
import roslib
import serial
from std_msgs.msg import String


ser=serial.Serial('/dev/rfcomm5' , 57600)
def motion(data) :
	if data == 'f':
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(19)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(218)
		ser.write(a)
		a = chr(13)
		ser.write(a)
                #time.sleep(2)
	if data == 'b' :
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(20)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(217)
		ser.write(a)
		a = chr(159)
		ser.write(a)


	if data == 'c':
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(15)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(217)
		ser.write(a)
		a = chr(197)
		ser.write(a)
		#time.sleep(2)
	if data == 'cc':
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(16)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(218)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		#time.sleep(2)
		
	if data == 'rs' :
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(17)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(217)
		ser.write(a)
		a = chr(129)
		ser.write(a)
	if data == 'ls'	:
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(17) 
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(217)
		ser.write(a)
		a = chr(129)
		ser.write(a)
	
	if data == 'pk' :
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(46)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(217)
		ser.write(a)
		a = chr(3)
		ser.write(a)
	

	if data == 'pf':
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(45) 
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(217)
		ser.write(a)
		a = chr(9)
		ser.write(a)
	


	if data == 'lf':
		a = chr(255)
 		ser.write(a)
		a = chr(255)
		ser.write(a)
		a = chr(253)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(200)
		ser.write(a)
		a = chr(7)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(3)
		ser.write(a)
		a = chr(66)
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(43) 
		ser.write(a)
		a = chr(0)
		ser.write(a)
		a = chr(217)
		ser.write(a)
		a = chr(29)
		ser.write(a)
	






def callback(data):
	if data.data == 'cc':
		print "anticlock"
		motion('cc')
	elif data.data == 'c':
		print "clock"
		motion('c')

	elif data.data == 'f':
		print "front"
		motion('f')	
				#instead of print statements, put in operation piece of code.
	elif data.data == "ls":
		print "left_sidestep"
		motion('ls')

	elif data.data == "rs":
		print "right_sidestep"
		motion('rs')

	elif data.data == "lt":
		print "lift"
		pub.publish("stop")
		motion('lf')
			

	elif data.data == "pk":
		print "pick"
		motion('pk')
	elif data.data == 'pcc':
		print "pick_anticlock"
		motion('pf')

	elif data.data == 'pc':
		print "pick_clock"
		motion('pf')

	elif data.data == 'pf':
		print "pick_front"
		motion('pf')	
				     
	elif data.data == "pls":
		print "pick_left_sidestep"

	elif data.data == "prs":
		print "pick_right_sidestep"
		motion('prs')

	elif data.data == 'lcc':
		print "lift_anticlock"
		motion('lf')

	elif data.data == 'lc':
		print "lift_clock"
		motion('lf')

	elif data.data == 'lf':
		print "lift_front"
		motion('lf')	
				     
	elif data.data == "lls":
		print "lift_left_sidestep"
		motion('lls')

	elif data.data == "lrs":
		print "lift_right_sidestep"
		motion('lrs')
	

	elif data.data == "st":
		print "stop"
		pub.publish("stop")

def run():
	rospy.init_node('Actuator', anonymous=True)
	pub = rospy.Publisher("command", String, queue_size=10)
	sub = rospy.Subscriber("Directions", String, callback)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass

def main():
	run()
	rospy.loginfo("Operation Ended")

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
