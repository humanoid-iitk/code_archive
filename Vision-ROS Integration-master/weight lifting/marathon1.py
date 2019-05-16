import cv2
import numpy as np 

cam = cv2.VideoCapture(1)

def Arrow(ArrowImage):
	ArrowImage = cv2.bitwise_not(ArrowImage.copy())
	cntArrow, _ = cv2.findContours(ArrowImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	if len(cntArrow) > 0:

		cntmax = max(cntArrow, key=cv2.contourArea)
		x1, y1, w1, h1 = cv2.boundingRect(cntmax)
		#roiL = np.zeros((h1 + 2,w1/3 + 2), np.uint8)
		#roiM = np.zeros((h1 + 2,w1/3 + 2), np.uint8)
		#roiR = np.zeros((h1 + 2,w1/3 + 2), np.uint8)
	
		#roiL[1 :h1 + 1, 1: w1/3 + 1] = ArrowImage[y1 : y1 + h1, x1 : x1 + w1/3]
		#roiM[1 :h1 + 1, 1: w1/3 + 1] = ArrowImage[y1 : y1 + h1, x1+w1/3 :x1 + (2*w1)/3]
		#roiR[1 :h1 + 1, 1: w1/3 + 1] = ArrowImage[y1 : y1 + h1, x1+(2*w1)/3 :x1 + w1]
		roiL = ArrowImage[y1 : y1 + h1, x1 : x1 + w1/3]
		roiM = ArrowImage[y1 : y1 + h1, x1+w1/3 :x1 + (2*w1)/3]
		roiR = ArrowImage[y1 : y1 + h1, x1+(2*w1)/3 :x1 + w1]

		cntl, _ = cv2.findContours(roiL, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cntm, _ = cv2.findContours(roiM, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cntr, _ = cv2.findContours(roiR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		lArea = 0
		mArea = 0
		rArea = 0
		if len(cntl) > 0:
			lArea = cv2.contourArea(max(cntl, key= cv2.contourArea))
		if len(cntl) > 0:
			mArea = cv2.contourArea(max(cntm, key= cv2.contourArea))
		if len(cntl) > 0:
			rArea = cv2.contourArea(max(cntr, key= cv2.contourArea))

		if abs(lArea - rArea) > 200:
			if lArea > rArea:	
				print "right Arrow"
			else:
				print "left Arrow"
		else:
			print "front Arrow"

while True:
	_, image = cam.read()
	kernal = np.ones((5, 5), np.float32)/25
	mask = cv2.filter2D(image, -1, kernal)
	gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
	
	_, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
	rows, cols = thresh.shape
	
	_, Line = cv2.threshold(gray[8*rows/10 : 9*rows/10, 0: cols], 220, 255, cv2.THRESH_BINARY)
	lineroi = np.zeros((rows/10 + 2, cols+2), np.uint8)
	lineroi[1:rows/10+1, 1:cols+1] = Line

	cntLine, _ = cv2.findContours(lineroi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cntArrowBox, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	BoxArea = 0
	if len(cntArrowBox) > 0:
		Box = max(cntArrowBox, key=cv2.contourArea)
		BoxArea = cv2.contourArea(Box)
		if BoxArea > 1000:
			x,y,w,h = cv2.boundingRect(Box)
			cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
			print (x+w/2, y+h/2)
			cv2.imshow('arrow image', thresh[y :y+h, x: x + w])
			Arrow(thresh[y: y+h,x: x + w])

	if len(cntLine) > 0 an dBoxArea < 1000:
		M = cv2.moments(max(cntLine, key=cv2.contourArea))
		cx = int(M['m10']/(float(M['m00'])+0.000001))
		dist = cx - cols/2 - 1
		if dist > 1.5:
			print('right', dist)
		elif dist < -1.5:
			print('left', dist)
		else:
			print('front', dist)

	elif BoxArea < 1000:
		print "line not found"

	cv2.imshow("image", image)
	cv2.imshow('line tracker', lineroi)
	cv2.imshow("thresh", thresh)
	cv2.imshow('gray', gray)

	if cv2.waitKey(40) & 0xff == ord('q'):
		break

cv2.destroyAllWindows()
cam.release()