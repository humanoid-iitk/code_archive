
'''
    courtesy: 
        IITk Humanoid Team.

    Line Follower code sample.


    This sample shows how CV can be used to guide robots
    to follow lines having reasonable width.

    The program finds the coordinates of the boundary
    of the segment of the line inside a narrow strip of
    image frame near the bot. 

    Using mathematical operations the position of line 
    relative to the center line of the image frame 
    is found out and accordingly 'r', 'l' or 'f' which 
    mean right, left and front respectively, are printed
    depicting the direction in which the bot should move 
    to reach the line.

    these characters are stored in the variable 'move'
    which can be passed to the ros for giving command to
    the bot to move in the desired direction.
    
    Key:
         Q    - exit

    Usage:
        In case background is darker than line
        add the commented statement, else it is 
        good to go. 

'''


#import required libraries
import numpy as np
import cv2

#create an empty function to be passed while creating trackbars
def track():
    pass

#create trackbar to callibrate threshold value.
cv2.namedWindow("control")
cv2.createTrackbar("threshMin", "control", 60, 255, track)  
 
#switch on the camera.
video_capture = cv2.VideoCapture(0)

while(True):

    #read frames from the camera.
    ret, frame = video_capture.read()
    
    #get dimentions of the frame.
    imx, imy, s = frame.shape
    
    #crop the image.
    crop_img =  frame[(2*imx)/3 : (3*imx)/4 , 0 : imy - 0]
    
    #convert cropped image to greyscale.
    threshMin = cv2.getTrackbarPos("threshMin", "control")
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    
    ##IF BACKGROUND IS DARKER THAN LINE REMOVE # FROM THE COMMENT BELOW
    #gray = cv2.bitwise_not(gray)

    #blur to remove noice and convert to binary image.
    kernal = np.ones((5,5), np.float32)/25
    mask = cv2.filter2D(gray, -1, kernal)
    ret,thresh = cv2.threshold(mask,threshMin,255,cv2.THRESH_BINARY_INV)

    #get contours of cropped image.
    rel, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #check if contours is empty.
    if len(contours) > 0:

        #find contour with maximum area.
        cnt = max(contours, key = cv2.contourArea)
        
        #find coordinates of vertices of its bounding rectangle.
        x, y, w, h = cv2.boundingRect(cnt)
        cx = float(x)
        
        #find relative position of bounding rectangle wrt center line
        #in form of a parameter t.

        '''
            t has been calculated by taking ratio of the x 
            coordinate of the bounding rectangle with the total 
            width of the cropped image, and then substracting it 
            from 1, giving its relative position.

            in the end multiply it by 5 to give some window for
            approximate comparision.

        '''
        t = float(1.0 - 2.0*(cx /(imx - 20.0)))*5

        '''
        if t is negative, line is on right side of center line
        if positive line is on left side, else in the center.
        we keep a range of 0.20 on either side to fit in the 
        width of the line.

        print 'f', 'r', or 'l' accordingly.
       
        '''
        move = ''
        if t > -0.20 and t < 0.20:
            move = 'f'
        elif t <= -0.20:
            move = 'r'
        elif t >= 0.20:
            move = 'l'
        print(move, t)

        #draw contours of the line.
        cv2.drawContours(crop_img, [cnt], -1, (255,255,0), 3)
       
    # display images showing thresh image, crop image
    # and the original image.
    cv2.imshow('frame',frame)
    cv2.imshow('thresh',thresh)
    cv2.imshow('crop_img',crop_img)

    # wait for user to press q from the keyboard
    # exit on receiving input.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#turn off the camera.
video_capture.release()
cv2.destroyAllWindows()
