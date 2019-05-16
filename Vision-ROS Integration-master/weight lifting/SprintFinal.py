import cv2
import numpy as np
import time
import math

cam = cv2.VideoCapture(0)

def moveBack():
	isParallel = False

	while isParallel:
		rel, img = cam.read()
		kernal = np.ones((5, 5), np.float32)/25
		mask = cv2.filter2D(img, -1, kernal)
		gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
		rel, thresh_1 = cv2.threshold(gray[0:rows, 0:cols/2], 195, 255, cv2.THRESH_BINARY)
		rel, thresh_2 = cv2.threshold(gray[0:rows, 0:cols/2], 195, 255, cv2.THRESH_BINARY)
		contours_1, hierarchy = cv2.findContours(thresh_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		contours_2, hierarchy = cv2.findContours(thresh_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		if len(contours_1) > 0:
			cnt_1 = max(contours, key=cv2.contourArea)
			[ax1, ay1, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
			theta = -(math.atan(float(ay1)/ax1))

		if len(contours_1) > 0:
			cnt_1 = max(contours, key=cv2.contourArea)
			[ax2, ay2, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
			theta = -(math.atan(float(ay2)/ax2))
		theta = theta1 + theta2
		if abs(theta) < 0.025:
			print ("forward", theta)
			isParallel = True
		elif theta > 0.025:
			print ("clock", theta)
		else:
			print ("counterclock", theta)

		cv2.imshow("frame1", img)
		cv2.imshow('thresh1', thresh)
		if cv2.waitKey(30) & 0xff == ord('q'):
			break
	print("start walking")
	t = time.time()
	while (time.time() - t < 5):  
		pass			

while True:
	rel, img1 = cam.read()
	kernal1 = np.ones((5, 5), np.float32)/25
	mask1 = cv2.filter2D(img1, -1, kernal1)
	gray1 = cv2.cvtColor(mask1, cv2.COLOR_BGR2GRAY)
	rows, cols = gray1.shape
	rel, thresh1 = cv2.threshold(gray1[0 : rows, 0 : cols/2], 230, 255, cv2.THRESH_BINARY)
	rel, thresh2 = cv2.threshold(gray1[0 : rows, cols/2 : cols], 230, 255, cv2.THRESH_BINARY)

	contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours2, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	theta1 = 0
	theta2 = 0
	if len(contours1) > 0:
		cnt1 = max(contours1, key=cv2.contourArea)
		[vx1, vy1, x, y] = cv2.fitLine(cnt1, cv2.DIST_L2, 0, 0.01, 0.01)
		theta1 = -(math.atan(float(vy1)/vx1))
	else:
		print "move left (line to the left not found)"
	
	if len(contours2) > 0:
		cnt2 = max(contours2, key = cv2.contourArea)
		[vx2, vy2, x, y] = cv2.fitLine(cnt2, cv2.DIST_L2, 0, 0.01, 0.01)
		theta2 = -(math.atan(float(vy2)/vx2))
	else:
		print "move right (line to the right not found)"
	
	theta = theta1 + theta2
	if abs(theta) < 0.025:
		print ("forward", theta)
	elif theta > 0.025:
		print ("clock", theta)
	else:
		print ("counterclock", theta)

	obj = cv2.cvtColor(mask1, cv2.COLOR_BGR2HSV)
	objThresh = cv2.inRange(obj[0:rows, cols/4 : 3*cols/4], (), ())
	objcnt, hierarchy = cv2.findContours(objThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	if len(objcnt) > 0:
		cntmax = max(objcnt, key = cv2.contourArea)
		if cv2.contourArea(cntmax) > 50 || cv2.contourArea(cntmax) < 5:
			moveBack()

	cv2.imshow("frame", img1)
	cv2.imshow('thresh1', thresh1)
	cv2.imshow('thresh2', thresh12)
	cv2.imshow("object", objThresh)
	if cv2.waitKey(30) & 0xff == ord('q'):
		break

cv2.destroyAllWindows()
cam.release()

