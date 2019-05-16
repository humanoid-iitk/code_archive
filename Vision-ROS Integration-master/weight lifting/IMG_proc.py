import cv2
import numpy as np 
import math

class Operations:
	def maxContour(self, Image):
		contours, hierarchy = cv2.findContours(Image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		if len(contours) > 0:
			return [1, max(contours, key = cv2.contourArea)]
		else:
			return [0, contours]

	def threshGray(self, Image, threshValue, Intensity):
		kernal = np.ones((5,5), np.float32)/25
		gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
		blur = cv2.filter2D(gray, -1, kernal)
		rel, thresh = cv2.threshold(blur, threshValue, Intensity, cv2.THRESH_BINARY)
		return thresh 

	def threshHSV(self, Image, (Hmin, Smin, Vmin), (Hmax, Smax, Vmax)):
		kernal = np.ones((5,5), np.float32)/25
		HSV = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
		blur = cv2.filter2D(HSV, -1, kernal)
		return cv2.inRange(blur, (Hmin, Smin, Vmin), (Hmax, Smax, Vmax))

	def findCenter(self, contours):
		points = []
		if len(contours) > 0:
			for contour in contours:
				M = cv2.moments(contour)
				cx = int(M['m10']/(float(M['m00']) + 0.000001))
				cy = int(M['m01']/(float(M['m00']) + 0.000001))
				points.append([cx,cy])
			
			return [1, points]

		else:
			return [0, points]

	def findCenterMax(self, Image):
		success, cntMax = self.maxContour(Image)
		if success:
			s, point = self.findCenter([cntMax])
			return [1, point[0]]

		else:
			return [0, []]
			
