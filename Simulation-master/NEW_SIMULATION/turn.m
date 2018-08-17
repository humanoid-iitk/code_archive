function [ ] = turn(theta)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
right_leg=zeros(4,14);
left_leg=zeros(4,14);
waist=zeros(4,4);
h=30*cos(18*pi/180);
left_joint_angles=zeros(6);%from top to bottom%
temp_left_joint_angles=zeros(3);
right_joint_angles=zeros(6);
temp_right_joint_angles=zeros(3);
centre_pelvis=zeros(4);
time=0.5;
pause(5);
    for t=1:20       %start
        if (t>-1) && (t<6)
            centre_pelvis(1)=3;
            centre_pelvis(2)=t+5;
            phi=0;
            xa=3;
            height_ankle = 0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        elseif (t>5) && (t<11)
            centre_pelvis(1)=3;
            centre_pelvis(2)=10;
            if(t>5) && (t<8)
                phi=0;
            else
                phi=theta/6*(t-7);
            end
            xa=3;
            height_ankle = (t-5)/5*(2);
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(t-5);
        elseif (t>10) && (t<16)
            centre_pelvis(1) =  3;
            if(t>10) && (t<14)
                phi= theta/2 + (theta)/6*(t-10);
            else
                phi=theta;
            end
            centre_pelvis(2) = 10;
            xa = 3;
            height_ankle = (15-t)/5*(2);
            centre_pelvis(3)=h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(15-t);
        else
            centre_pelvis(1)=3;
            phi=(theta);
            centre_pelvis(2)= 25-t;
            xa=3;
            height_ankle=0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        end

        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);

        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,0);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,phi);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);

        plot_final(left_leg,right_leg,waist);

        pause(time);

    end
    
    for t=1:10
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
            height_ankle = (t-5)/5*(2);
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(t-5);
        end

        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);

        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,0);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,theta);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);

        plot_final(left_leg,right_leg,waist);

        pause(time);

    end
    for t=1:2
        phi=theta/2*t;
        t1= [1 0 0 right_leg(1,1);0 1 0 right_leg(2,1);0 0 1 right_leg(3,1);0 0 0 1]*[0 1 0 0;-1 0 0 0;0 0 1 0;0 0 0 1]*Rz(-phi);
        centre_pelvis = t1*[-5;0;0;1];
        t2=t1*[1 0 0 -10;0 1 0 0;0 0 1 0;0 0 0 1];
        left_leg(:,1)=t2*[0;0;0;1];
        t2_gnd = t2*[0 1 0 0;0 0 -1 0;-1 0 0 -1;0 0 0 1];
        left_leg(:,2) = t2_gnd*[0;0;0;1];
        t3_gnd= t2_gnd*Rz(temp_left_joint_angles(1))*[1 0 0 0;0 0 1 0;0 -1 0 0;0 0 0 1]*Rz(-temp_left_joint_angles(3))*[1 0 0 15;0 1 0 0;0 0 1 0;0 0 0 1];
        left_leg(:,4) = t3_gnd*[0;0;0;1];
        t4_gnd = t3_gnd*Rz(temp_left_joint_angles(3)-temp_left_joint_angles(2))*[1 0 0 15;0 1 0 0;0 0 1 0;0 0 0 1];
        left_leg(:,5)=t4_gnd*[0;0;0;1];
        t5_gnd = t4_gnd*Rz(temp_left_joint_angles(2))*[1 0 0 0;0 0 -1 0;0 1 0 0;0 0 0 1];
        left_leg(:,6)=t5_gnd*[0;0;4.5;1];
        left_leg(:,3)=left_leg(:,2);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);

        plot_final(left_leg,right_leg,waist);

        pause(time);
    end
  
    for t=11:20
        if (t>10) && (t<16)
            centre_pelvis(1) =  3;
            centre_pelvis(2) = 0;
            xa = 3;
            height_ankle = (15-t)/5*(2);
            centre_pelvis(3)=h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(15-t);
        else
            centre_pelvis(1)=3;
            centre_pelvis(2)= -15+t;
            xa=3;
            height_ankle=0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        end

        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);

       
        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,0);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,0);
        
        
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);

        plot_final(left_leg,right_leg,waist);

        pause(time);
    end 

    %for(t=
        
    
    %{
else
    for t=1:20
        if (t>-1) && (t<6)
            centre_pelvis(1)=3;
            centre_pelvis(2)=-t+5;
            phi=0;
            xa=3;
            height_ankle = 0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        elseif (t>5) && (t<11)
            centre_pelvis(1)=3;
            centre_pelvis(2)=0;
            if(t>5) && (t<8)
                phi=0;
            else
                phi=theta/6*(t-7);
            end
            xa=3;
            height_ankle = (t-5)/5*(4.14);
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(t-5);
        elseif (t>10) && (t<15)
            centre_pelvis(1) =  3;
            if(t>10) && (t<14)
                phi= theta/2 + (theta)/6*(t-10);
            else
                phi=theta;
            end
            centre_pelvis(2) = 0;
            xa = 3;
            height_ankle = (15-t)/5*(4.14);
            centre_pelvis(3)=h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(15-t);
        else
            centre_pelvis(1)=3;
            phi=theta;
            centre_pelvis(2)= -15+t;
            xa=3;
            height_ankle=0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        end

        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);

        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,phi);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,0);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);

        plot_final(left_leg,right_leg,waist);

        pause(time);

    end
    
    for t=1:20       %start
        if (t>-1) && (t<6)
            centre_pelvis(1)=3;
            centre_pelvis(2)=t+5;
            phi=0;
            xa=3;
            height_ankle = 0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        elseif (t>5) && (t<11)
            centre_pelvis(1)=3;
            centre_pelvis(2)=10;
            if(t>5) && (t<8)
                phi=0;
            else
                phi=theta/6*(t-7);
            end
            xa=3;
            height_ankle = (t-5)/5*(4.14);
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(t-5);
        elseif (t>10) && (t<16)
            centre_pelvis(1) =  3;
            if(t>10) && (t<14)
                phi= theta/2 + (theta)/6*(t-10);
            else
                phi=theta;
            end
            centre_pelvis(2) = 10;
            xa = 3;
            height_ankle = (15-t)/5*(4.14);
            centre_pelvis(3)=h*cos(atan((centre_pelvis(2)-5)/h))+1+(0.18/5)*(15-t);
        else
            centre_pelvis(1)=3;
            phi=(theta);
            centre_pelvis(2)= 25-t;
            xa=3;
            height_ankle=0;
            centre_pelvis(3)= h*cos(atan((centre_pelvis(2)-5)/h))+1;
        end

        temp_left_joint_angles(1)=atan((centre_pelvis(2)-5)/h);
        [temp_left_joint_angles(2),temp_left_joint_angles(3)]=find_angles(centre_pelvis(1),3,centre_pelvis(3),0);
        temp_right_joint_angles(1)=temp_left_joint_angles(1);
        [temp_right_joint_angles(2),temp_right_joint_angles(3)]=find_angles(centre_pelvis(1),xa,centre_pelvis(3),height_ankle);

        left_leg=find_left_leg(centre_pelvis,temp_left_joint_angles,theta);
        right_leg=find_right_leg(centre_pelvis,temp_right_joint_angles,phi);
        waist(:,3)=left_leg(:,1);
        waist(:,4)=right_leg(:,1);
        waist(:,2)=[centre_pelvis(1);centre_pelvis(2);centre_pelvis(3);1];
        waist(:,1)=waist(:,2);
        waist(3,1)= 25 + waist(3,1);

        plot_final(left_leg,right_leg,waist);

        pause(time);

    end
    
    
end
    %}
end

