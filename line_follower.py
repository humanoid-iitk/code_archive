import cv2
import numpy as np

minMaxCx,counter=-1,0
Tmin=75
def test(self):
	pass
cv2.namedWindow('Track_bar')
cv2.createTrackbar('Thresh_Min','Track_bar',Tmin,255,test)
cap=cv2.VideoCapture(0)
ret,img=cap.read()
rows,cols,channels = img.shape
while (True):
	ret,img=cap.read()
	roi=img[2*rows/3:3*rows/4,10:cols-10]
	mask=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
	Tmin=cv2.getTrackbarPos('Thresh_Min','Track_bar')
	ret,thresh=cv2.threshold(mask,Tmin,255,cv2.THRESH_BINARY)
	image,contours,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cv2.imshow('Thresh',thresh)
	if len(contours)>0:
		maxarea,index=0,0
		for j in range(0,len(contours)):
			moment=cv2.moments(contours[j])
			area=moment['m00']
			if(maxarea<area):
				maxarea=area
				index=j
		moment=cv2.moments(contours[index])
		x,y,w,h=cv2.boundingRect(contours[index])
		if minMaxCx!=x:
				minMaxCx=x
		if minMaxCx==-1:
			t=0.0
		else:
			t=(1.0-2*(minMaxCx/(cols-20.0)))*5
		if t>-0.20 and t<0.20:
			ch='f'
		elif t<-0.20:
			ch='r'
		else:
			ch='l'
		t=abs(t)
		chres=(ch,int(t+48),'-')
		if counter>2*t:
			print chres
			counter=0
		counter+=1
	cv2.rectangle(img,(10,2*rows/3),(cols-10,3*rows/4),(0,255,0),1)
	cv2.imshow("IMAGE",img)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
