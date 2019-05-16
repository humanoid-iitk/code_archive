#!/usr/bin/env python
import rospy
import math
import time
import subprocess
#from geometry_msgs.msg import vector3
from geometry_msgs.msg import Point
from std_msgs.msg import String
from std_msgs.msg import Float64
shooting_time=0.93  #set arrow shooting velocity
target_distance=10  #set target distance manually

LOCATION=None

flag=1


def shoot_mode(R,CENTRE) :
    
   
    subprocess.call("rostopic pub -1 /servo_id5/command std_msgs/Float64 -- 1.0" ,shell=True)
    subprocess.call("rostopic pub -1 /servo_id2/command std_msgs/Float64 -- 0.9" ,shell=True)
    subprocess.call("rostopic pub -1 /servo_id3/command std_msgs/Float64 -- 2.9" ,shell=True)
    subprocess.call("rostopic pub -1 /servo_id7/command std_msgs/Float64 -- 2.2" ,shell=True)
    subprocess.call("rostopic pub -1 /servo_id4/command std_msgs/Float64 -- 4.8" ,shell=True)
    subprocess.call("rostopic pub -1 /servo_id6/command std_msgs/Float64 -- 3.09 & rostopic pub -1 /servo_id7/command std_msgs/Float64 -- 2.89" ,shell=True)
    subprocess.call("rostopic pub -1 /servo_id4/command std_msgs/Float64 -- 4.1" ,shell=True)
    subprocess.call("rostopic pub -1 /servo_id6/command std_msgs/Float64 -- 1.61 & rostopic pub -1 /servo_id7/command std_msgs/Float64 -- 1.75" ,shell=True)       



         

    print("SHOOT_MODE")
    rospy.sleep(10)
    

    
def motion(CENTRE):
    global flag
    pixel_x=640
    pixel_y=480
    
    
    if int(pixel_x/2)>CENTRE:
	#pub3.publish('r')
        print('l')
    else :
	#pub3.publish('l')
        print('r')
    rospy.sleep(5)
    #else :
     #   pub3.publish('shoot')
      #  print('shoot')
       # flag=0
   # print (R)
    #print(omega)
    #print(CENTRE)
    #shooting_data=Point(float(R),float(omega),0.0)
   # pub3.publish(shooting_data)
    


n=0
def callback1(loc_msg1):
    global LOCATION
   
    #print(n)'''
    LOCATION =loc_msg1
    #print('update')
    #print(time.time())
   
    
    
    
    

def start1():
    pixel_x=640 # 640
    pixel_y=480
   
    rospy.init_node('aim_bot')
    rospy.Subscriber('/image_processing/ball_coordinates',Point,callback1)
    
  
    #pub3=rospy.Publisher('motion_commands',String, queue_size=1)
    while LOCATION is None and not rospy.is_shutdown():
	rospy.sleep(.1)
    rate=rospy.Rate(100)
    xlow=[pixel_x,0]
    xhigh=[0,0]
    ylow=[0,pixel_y]
    yhigh=[0,0]

   

   
    
    init_point=(LOCATION.x,LOCATION.y)
  
    global flag
  
    while flag and not rospy.is_shutdown() :
        
   
	
        
        if 10<=(init_point[0]-LOCATION.x)**2+(init_point[1]-LOCATION.y)**2<=100 :
            print((init_point[1]-LOCATION.y)**2+(init_point[0]-LOCATION.x)**2)
            #omega=2*math.pi/(time.time()-start)
            R1=(xhigh[0]-xlow[0])/2
            R2=(yhigh[1]-ylow[1])/2
            CENTRE=((xlow[0]+xhigh[0])/2,(ylow[1]+yhigh[1])/2)
            #print(omega)
            print('entered')
            print(CENTRE)
            print(R1)
            print(R2)
            R=(R1+R2)/2
            #pub1.publish(yhigh[0],yhigh[1],0)
            
           #if counter==1:
            #motion(R,omega,init_point,CENTRE)
		#counter=0
           
            if  abs(int(pixel_x/2)-CENTRE[0])> 10 :
                motion(CENTRE[0])
                print('in if')
            else :
                w_prev=0
                for i in range(6) :
                    print('reached centre')
                   
                    n1=1
                    n2=1
                    n3=1
                    n4=1
                    initial_point=LOCATION
                    while n1 or n3 :
                        if not initial_point==LOCATION :
                            if initial_point.x -CENTRE[0] >=0 and LOCATION.x-CENTRE[0] <=0 and LOCATION.y-CENTRE[1]>=0 and n1:
                                cw=1
                                t1=time.time()
                                n1=0
                                n2=0
                            if initial_point.x -CENTRE[0] <=0 and LOCATION.x-CENTRE[0] >=0 and LOCATION.y-CENTRE[1]>=0 and n2:
                                cw=0
                                t1=time.time()
                                n1=0
                                n2=0
                            if initial_point.x -CENTRE[0] >=0 and LOCATION.x-CENTRE[0] <=0 and LOCATION.y-CENTRE[1]<=0 and n3:
                                cw=0
                                t2=time.time()
                                n3=0
                                n4=0
                            if initial_point.x -CENTRE[0] <=0 and LOCATION.x-CENTRE[0]>=0 and LOCATION.y-CENTRE[1]<=0 and n4:
                                cw=1
                                t2=time.time()
                                n3=0
                                n4=0
                            
                            
                           
                        initial_point=LOCATION
                        rospy.sleep(.001)
                    #print(abs(t1-t2 ))
                    
                    w_new=(math.pi/abs(t1-t2)) +w_prev
                    print(w_new)
                    print(cw)
                    rospy.sleep(1)
                    w_prev=w_new


   
                w=(w_new)/6
                print(w)
                print('hey')

                delta_theta=w*shooting_time
                
                delta_theta=math.degrees(delta_theta)
                print(delta_theta)
                
                
                shoot_mode(R2,CENTRE)

                
                if cw :
                    delta_theta=90+delta_theta
                    release_angle=delta_theta % 360
                    print('release_angle')
                    print(release_angle)
                    #print(release_angle)
                    fleg=1
                    current_pos_old= (LOCATION.x-CENTRE[0] , -(LOCATION.y-CENTRE[1]))
                    x_old=current_pos_old[0]
                    y_old=current_pos_old[1]
    
                    theta_old= math.atan2(y_old,x_old)
                    if y_old<0  :
                       theta_old=2*math.pi+theta_old
                    elif y_old==0 and x_old<0 :
                       theta_old= math.pi
                    theta_old=math.degrees(theta_old)
                    while fleg :
                        current_pos_new= (LOCATION.x-CENTRE[0] , -(LOCATION.y-CENTRE[1]))
                        if not current_pos_new==current_pos_old :
                        
                            
                      	    x_new=current_pos_new[0]
                            y_new=current_pos_new[1]
                
                            theta_new= math.atan2(y_new,x_new)
                            if y_new<0  :
                                theta_new=2*math.pi+theta_new
                            elif y_new==0 and x_new<0 :
                                theta_new= math.pi
                            
                            theta_new=math.degrees(theta_new)
                            print(theta_new)
                            if theta_old > release_angle and theta_new< release_angle :
                                print('thetanew')
                                print(theta_new)
                                print('SHOOT')
                                subprocess.call("gnome-screenshot" ,shell=True)
                             
                                subprocess.call("rostopic pub -1 /servo_id4/command std_msgs/Float64 -- 4.8" ,shell=True)
                              
                                rospy.sleep(5)
                                fleg=0
                            theta_old=theta_new
                            current_pos_old=current_pos_new
                            


                        
                        
                else :

                    
                    delta_theta=90-delta_theta
                    release_angle=delta_theta % 360
                    print('release angle')
                    print(release_angle)
                    fleg=1
                    current_pos_old= (LOCATION.x-CENTRE[0] , -(LOCATION.y-CENTRE[1]))
                    x_old=current_pos_old[0]
                    y_old=current_pos_old[1]
    
                    theta_old= math.atan2(y_old,x_old)
                    if y_old<0  :
                       theta_old=2*math.pi+theta_old
                    elif y_old==0 and x_old<0 :
                       theta_old= math.pi
                    theta_old=math.degrees(theta_old)
                    while fleg :
                        current_pos_new= (LOCATION.x-CENTRE[0] , -(LOCATION.y-CENTRE[1]))
                        if not current_pos_new==current_pos_old :
                        
                            
                      	    x_new=current_pos_new[0]
                            y_new=current_pos_new[1]
                
                            theta_new= math.atan2(y_new,x_new)
                            if y_new<0  :
                                theta_new=2*math.pi+theta_new
                            elif y_new==0 and x_new<0 :
                                theta_new= math.pi
                            theta_new=math.degrees(theta_new)
                            
                            if theta_old< release_angle and theta_new> release_angle :
                                print('SHOOT')
                                subprocess.call("gnome-screenshot" ,shell=True)
                                print('thetanew')
                                print(theta_new)
                               
                                subprocess.call("rostopic pub -1 /servo_id4/command std_msgs/Float64 -- 4.8" ,shell=True)
                                
                                rospy.sleep(5)
                                fleg=0
                            theta_old=theta_new
                            current_pos_old=current_pos_new
                            
                

               
               
              
                flag=0

                
                
                
                  
                          

                 
                 
            

           #start=time.time()
            init_point=(LOCATION.x,LOCATION.y)
            xlow=[pixel_x,0]
            xhigh=[0,0]
            ylow=[0,pixel_y]
            yhigh=[0,0]     
        

  
        
	if LOCATION.z > 0 :
           
            if LOCATION.x<=xlow[0]:
                xlow=[LOCATION.x,LOCATION.y]
            if LOCATION.x>=xhigh[0]:
                xhigh=[LOCATION.x,LOCATION.y]
            if LOCATION.y<=ylow[1]:
                ylow=[LOCATION.x,LOCATION.y]
            if LOCATION.y>=yhigh[1]:
                yhigh=[LOCATION.x,LOCATION.y]
            
              
                        
            

                
            global n
            n=n+1
            print(n)
            
            #print(LOCATION.y)
            #print(time.time())
            print((xhigh[0]-xlow[0])/2)
            print((yhigh[1]-ylow[1])/2)
            #print((init_point[1]-LOCATION.y)**2+(init_point[0]-LOCATION.x)**2)
	rate.sleep()
if __name__ =='__main__' :
    start1()
