#!/usr/bin/env python
import cv2
import numpy as np 
import math

h = 19
class Mapper:

	def GetXp(self, Xa, Dist):
		return int((Xa*(Dist ** (-1.02))*692.00) + 0.5)

	def GetYp(self, Ya ,th):
		y = h*(Ya - math.tan(th)*h)/(h*math.cos(th) + Ya*math.sin(th))
		return self.GetXp(y, h*math.tan(th))

	def GetXa(self, Xp, Dist):
		return Xp*(Dist ** (1.02))/692.00

	def GetYa(self, Yp , th):
		y = self.GetXa(Yp, h*math.tan(th))
		return h*(h*math.tan(th) + y*math.cos(th))/(h - y*math.sin(th))

	def GetDist(self, Ya, th):
		return (Ya - h*math.tan(th))*math.sin(th) + h*math.tan(th)
