right_leg=zeros(4,14);
left_leg=zeros(4,14);
waist=zeros(4,4);
h=30*cos(18*pi/180);
left_joint_angles=zeros(6);%from top to bottom%
temp_left_joint_angles=zeros(3);
right_joint_angles=zeros(6);
temp_right_joint_angles=zeros(3);
centre_pelvis=zeros(4);
theta=0;
no_of_steps=2;
right_hand_angles=zeros(4,1);
left_hand_angles=zeros(4,1);
right_arm=zeros(4,5);
left_arm=zeros(4,5);
time=0.1;
pause(5)
    for t=1:25       %start
        if (t>-1) && (t<6)
            centre_pelvis(1)=3;
            centre_pelvis(2)=3*t/5+5;
            xa=3;
            height_ankle = 0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
            right_hand_angles(1)= -3*pi/180;
            right_hand_angles(3)= 16*pi/180;
            left_hand_angles(1)= -3*pi/180;
            left_hand_angles(3)= 16*pi/180;
        elseif (t>5) && (t<11)
            centre_pelvis(1)=3;
            centre_pelvis(2)=8;
            xa=3;
            height_ankle = (t-5)/5*(4.14);
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(t-5);
        elseif (t>10) && (t<21)
            centre_pelvis(1) =  t/10+2;
            x=centre_pelvis(1);
            centre_pelvis(2) = 8;
            xa = (3/5)*(t+10) - 9;
            height_ankle = -0.005*(xa+20)*(xa+3)*(xa-9);
            centre_pelvis(3)=1 - 0.1*(x-4)*(x-2)*(x-1.2) + h*cos(atan(5/h));
            right_hand_angles(1)= -3*pi/180-9*(t-10)/10*pi/180;
            right_hand_angles(3)= 16*pi/180-2*(t-10)/10*pi/180;
            left_hand_angles(1)= -3*pi/180+9*(t-10)/10*pi/180;
            left_hand_angles(3)= 16*pi/180+2*(t-10)/10*pi/180;
        else
            centre_pelvis(1)=2*t/5-4;
            centre_pelvis(2)= 8-3*(t-20)/10;
            xa=9;
            height_ankle=0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        end

        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);

        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,theta);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,theta);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);
        right_arm=find_arm(centre_pelvis,right_hand_angles,1);
        left_arm=find_arm(centre_pelvis,left_hand_angles,0);
        plot2_final(left_leg,right_leg,waist,right_arm,left_arm);

        pause(time);

    end   
%{
     for t=1:25       %start
        if (t>-1) && (t<6)
            centre_pelvis(1)=3;
            centre_pelvis(2)=-t+5;
            xa=3;
            height_ankle = 0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        elseif (t>5) && (t<11)
            centre_pelvis(1)=3;
            centre_pelvis(2)=0;
            xa=3;
            height_ankle = (t-5)/5*(4.14);
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(t-5);
        elseif (t>10) && (t<21)
            centre_pelvis(1) =  t/10+2;
            x=centre_pelvis(1);
            centre_pelvis(2) = 0;
            xa = (3/5)*(t+10) - 9;
            height_ankle = -0.005*(xa+20)*(xa+3)*(xa-9);
            centre_pelvis(3)=1 - 0.1*(x-4)*(x-2)*(x-1.2) + h*cos(atan(5/h));
        else
            centre_pelvis(1)=2*t/5-4;
            centre_pelvis(2)= 20-t;
            xa=9;
            height_ankle=0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        end

        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);

        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,theta);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,theta);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);

        plot_final(left_leg,right_leg,waist);

        pause(time);

    end   
  
%}
for m=1:no_of_steps
    for t=1:40    %left leg as swing one
        if (t>-1) && (t<11)       %dsp1
            centre_pelvis(1) = t/5
            centre_pelvis(2) = -3*(t)/10+5;
            xa = -3;
            height_ankle = 0;
            centre_pelvis(3) =h*cos(atan((centre_pelvis(2)-5)/h))+1;
        elseif (t>10) && (t<31)   %ssp
            centre_pelvis(1) = 1 + t/10;
            x=centre_pelvis(1);
            centre_pelvis(2) = 2;
            xa = (3/5)*t - 9;
            height_ankle = -0.005*(xa+20)*(xa+3)*(xa-9);
            centre_pelvis(3)=1 - 0.1*(x-4)*(x-2)*(x-1.2) + h*cos(atan((centre_pelvis(2)-5)/h));
            right_hand_angles(1)= -12*pi/180+18*(t-10)/20*pi/180;
            right_hand_angles(3)= 14*pi/180+4*(t-10)/20*pi/180;
            left_hand_angles(1)= 6*pi/180-18*(t-10)/20*pi/180;
            left_hand_angles(3)= 18*pi/180-4*(t-10)/20*pi/180;
        else                       %dsp2
            centre_pelvis(1) = t/5 -2;
            centre_pelvis(2) = 2+3*(t-30)/10;
            xa = 9;
            height_ankle = 0;
            centre_pelvis(3)=1+h*cos(atan((centre_pelvis(2)-5)/h));
        end
        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);
        
        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,theta);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,theta);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);
        right_arm=find_arm(centre_pelvis,right_hand_angles,1);
        left_arm=find_arm(centre_pelvis,left_hand_angles,0);
        plot2_final(left_leg,right_leg,waist,right_arm,left_arm);
        
        pause(time);
    
    end
    
    for t=1:40                     %swing leg as right leg
        if (t>-1) && (t<11)        
            centre_pelvis(1) = t/5
            centre_pelvis(2) =3*(t)/10+5;
            xa = -3;
            height_ankle = 0;
            centre_pelvis(3) =h*cos(atan((centre_pelvis(2)-5)/h))+1;
        elseif (t>10) && (t<31)
            centre_pelvis(1) = 1 + t/10;
            x=centre_pelvis(1);
            centre_pelvis(2) = 8;
            xa = (3/5)*t - 9;
            height_ankle = -0.005*(xa+20)*(xa+3)*(xa-9);
            centre_pelvis(3)= -0.1*(x-4)*(x-2)*(x-1.2) + h*cos(atan((centre_pelvis(2)-5)/h))+1;
            right_hand_angles(1)= 6*pi/180-18*(t-10)/20*pi/180;
            right_hand_angles(3)= 18*pi/180-4*(t-10)/20*pi/180;
            left_hand_angles(1)= -12*pi/180+18*(t-10)/20*pi/180;
            left_hand_angles(3)= 14*pi/180+4*(t-10)/20*pi/180;
        else
            centre_pelvis(1) = t/5 -2;
            centre_pelvis(2) = 8-3*(t-30)/10;
            xa = 9;
            height_ankle = 0;
            centre_pelvis(3)=h*cos(atan((centre_pelvis(2)-5)/h))+1;
        end
        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);
        
        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,theta);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,theta);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);
        right_arm=find_arm(centre_pelvis,right_hand_angles,1);
        left_arm=find_arm(centre_pelvis,left_hand_angles,0);
        plot2_final(left_leg,right_leg,waist,right_arm,left_arm);
        
        pause(time);
    
    end
end
   