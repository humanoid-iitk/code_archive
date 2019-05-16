'''
	courtesy: 
		Team humanoid, Robotics club, IITk

	Obstacle detection
	About:	
		This code finds area of color green(the favourable portion)
		in three different segments of the image, And directs the bot
		to the center of the segment having the largest percentage of 
		color green, i.e. the segment having the largest free path.

	Bugs:
		works poorly in low lit or too bright places. 

'''
import numpy as np 
import cv2

eps = 0.1

def empty(self):
	pass

cam = cv2.VideoCapture(0)

'''
cv2.namedWindow("trackbar")
cv2.createTrackbar('thresh', 'trackbar',20, 255, empty)
cv2.createTrackbar('hmin', 'trackbar',20, 255, empty)
cv2.createTrackbar('vmin', 'trackbar',20, 255, empty)
cv2.createTrackbar('smin', 'trackbar',20, 255, empty)
cv2.createTrackbar('hmax', 'trackbar',20, 255, empty)
cv2.createTrackbar('vmax', 'trackbar',20, 255, empty)
cv2.createTrackbar('smax', 'trackbar',20, 255, empty)
'''

while True:
	rel, frame = cam.read()

	'''
	thresh = cv2.getTrackbarPos('thresh', 'trackbar')
	hmin = cv2.getTrackbarPos('hmin', 'trackbar')
	vmin = cv2.getTrackbarPos('vmin', 'trackbar')
	smin = cv2.getTrackbarPos('smin', 'trackbar')
	hmax = cv2.getTrackbarPos('hmax', 'trackbar')
	vmax = cv2b.getTarckbarPos('vmax', 'trackbar')
	smax = cv2.getTrackbarPos('smax', 'trackbar')
	'''

	HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	kernal = np.ones((5,5), np.float32)/25
	mask = cv2.filter2D(HSV, -1, kernal)

	rows, cols, val = HSV.shape
	imArea = rows*cols

	top1 = cv2.inRange(HSV[0 : rows/3, 0 : cols], (0, 40, 40), (17, 210, 210))
	top2 = cv2.inRange(HSV[0 : rows/3, 0 : cols], (160, 40, 40), (179, 210, 210))
	
	left1 = cv2.inRange(HSV[3*rows/8 : rows, 0 : cols/4], (42, 40, 40), (75, 210, 210))
	middle1 = cv2.inRange(HSV[3*rows/8 : rows, cols/4 : 3*cols/4], (42, 40, 40), (75, 210, 210))
	right1 = cv2.inRange(HSV[3*rows/8 : rows, 3*cols/4 : cols], (42, 40, 40), (75, 210, 210))

	top = np.zeros((rows/3 + 2, cols + 2), np.uint8)
	middle = np.zeros((5*rows/8 + 2, cols/2 + 2), np.uint8)
	left = np.zeros((5*rows/8 + 2, cols/4 + 2), np.uint8)
	right = np.zeros((5*rows/8 + 2, cols/4 + 2), np.uint8)

	top[1 : rows/3 + 1, 1 : cols + 1] = top1 + top2
	left[1 : 5*rows/8 + 1, 1 : cols/4 + 1] = left1
	middle[1 : 5*rows/8 + 1, 1 : cols/2 + 1] = middle1
	right[1 : 5*rows/8 + 1, 1 : cols/4 + 1] = right1

	contourTop, hierarchy = cv2.findContours(top, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	contourLeft, hierarchy = cv2.findContours(left, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	contourMiddle, hierarchy = cv2.findContours(middle, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	contourRight, hierarchy = cv2.findContours(right, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	AreaTop = 0
	if len(contourTop) > 0:
		cntTop = max(contourTop, key = cv2.contourArea)
		AreaTop = cv2.contourArea(cntTop)

		if 3*AreaTop/imArea > 0.75:
			print "crouch"

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
				print "Return"
			else: 
				Mr = cv2.moments(cntRight)
				cxr = int(Mr['m10']/Mr['m00'])
				print "Right", cxr
		elif AreaRight < AreaLeft:
			if AreaLeft < 0.15:
				print "Return"
			else:
				Ml = cv2.moments(cntLeft)
				cxl = int(Ml['m10']/Ml['m00'])
				print "Left", cxl

	elif AreaMid >= AreaRight: 
		if AreaLeft > AreaMid:
			if AreaLeft < 0.15:
				print "Return"
			else:
				Ml = cv2.moments(cntLeft)
				cxl = int(Ml['m10']/Ml['m00'])
				print "Left", cxl
		else:
			if AreaMid < 0.15:
				print "Return"
			else:
				Mf = cv2.moments(cntMid)
				cxf = int(Mf['m10']/Mf['m00'])
				print "Front", cxf

	elif AreaMid >= AreaLeft:
		if AreaRight > AreaMid:
			if AreaRight < 0.15:
				print "Return"
			else:
				Mr = cv2.moments(cntRight)
				cxr = int(Mr['m10']/Mr['m00'])
				print "Right", cxr
		else:
			if AreaMid < 0.15:
				print "Return"
			else:
				Mf = cv2.moments(cntMid)
				cxf = int(Mf['m10']/Mf['m00'])
				print "Front", cxf

	cv2.imshow("top", top)
	cv2.imshow("middle", middle)
	cv2.imshow("left", left)
	cv2.imshow("right", right)
	cv2.imshow("original", frame)


	if cv2.waitKey(40) & 0xff == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()