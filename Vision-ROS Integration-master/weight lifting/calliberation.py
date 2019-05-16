import cv2
import numpy as np 
import math
'''
Ya = ctual distance along Y axis 
Xa = actual distance along X axis
Xp = pixel lenght X-axis
Yp = pixel length Y-axis
Dist = distance of center point on ground to the camera
				Yp
	| Ya			|
	|			|(0,0)
	|		________|________Xp
	|			|
 _______|________Xa		|
	0,0

'''

h = 49
class Mapper:

	def GetXp(self, Xa, Dist):
		return int((Xa*(Dist ** (-1.02))*692.00) + 0.5)

	def GetYp(self, Ya, th):
		y = h*(Ya - math.tan(th)*h)/(h*math.cos(th) + Ya*math.sin(th))
		return self.GetXp(y, h*math.tan(th))

	def GetXa(self, Xp, Dist):
		return Xp*(Dist ** (1.02))/692.00

	def GetYa(self, Yp, th):
		y = self.GetXa(Yp, h*math.tan(th))
		return h*(h*math.tan(th) + y*math.cos(th))/(h - y*math.sin(th))

	def GetDist(self, Ya, th):
		return (Ya - h*math.tan(th))*math.sin(th) + h*math.tan(th)
