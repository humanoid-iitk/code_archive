function [ arm ] = find_arm( point,angles,m )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
tpoint_gnd=[1 0 0 point(1);0 1 0 point(2);0 0 1 point(3)+20;0 0 0 1];
arm(:,1)=tpoint_gnd*[0;0;0;1];
if(m==1)
    t1_gnd=tpoint_gnd*[1 0 0 0;0 0 -1 -5;0 1 0 0;0 0 0 1];
else
    t1_gnd=tpoint_gnd*[1 0 0 0;0 0 -1 5;0 1 0 0;0 0 0 1];
end
arm(:,2)=t1_gnd*[0;0;0;1];
if(m==1)
    t2_gnd=t1_gnd*Rz(angles(1))*[0 0 -1 0;-1 0 0 0;0 1 0 5;0 0 0 1];
else
    t2_gnd=t1_gnd*Rz(angles(1))*[0 0 -1 0;-1 0 0 0;0 1 0 -5;0 0 0 1];
end
arm(:,3)=t2_gnd*[0;0;0;1];
t3_gnd=t2_gnd*Rz(angles(2))*[1 0 0 10;0 0 1 0;0 -1 0 0;0 0 0 1];
arm(:,4)=t3_gnd*[0;0;0;1];
arm(:,5)=t3_gnd*Rz(angles(3))*[10;0;0;1];
end

