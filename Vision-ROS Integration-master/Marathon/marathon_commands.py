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


	elif data.data == "st":
		print "stop"
		pub.publish("stop")


def run():
	rospy.init_node('Actuator', anonymous=True)
	
	sub = rospy.Subscriber("commands", String, callback)
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
