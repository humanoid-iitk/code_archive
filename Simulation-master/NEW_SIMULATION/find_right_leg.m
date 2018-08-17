function [ leg ] = find_right_leg( point,angles,theta )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
    tpoint_gnd = [1 0 0 point(1);0 1 0 point(2);0 0 1 point(3);0 0 0 1];
    t1_gnd = tpoint_gnd*[0 1 0 0;-1 0 0 -5;0 0 1 0;0 0 0 1];
    leg(:,1) = t1_gnd*[0;0;0;1];
    t2_gnd = t1_gnd*Rz(-theta)*[0 1 0 0;0 0 -1 0;-1 0 0 -1;0 0 0 1];
    leg(:,2) = t2_gnd*[0;0;0;1];
    t3_gnd= t2_gnd*Rz(angles(1))*[1 0 0 0;0 0 1 0;0 -1 0 0;0 0 0 1]*Rz(-angles(3))*[1 0 0 15;0 1 0 0;0 0 1 0;0 0 0 1];
    leg(:,4) = t3_gnd*[0;0;0;1];
    t4_gnd = t3_gnd*Rz(angles(3)-angles(2))*[1 0 0 15;0 1 0 0;0 0 1 0;0 0 0 1];
    leg(:,5)=t4_gnd*[0;0;0;1];
    t5_gnd = t4_gnd*Rz(angles(2))*[1 0 0 0;0 0 -1 0;0 1 0 0;0 0 0 1];
    leg(:,6)=leg(:,5);
    leg(1,6)=leg(1,6)+4.5;
    leg(:,7)=leg(:,6);
    leg(2,7)=leg(2,7)+2;
    leg(:,8)=leg(:,7);
    leg(1,8)=leg(1,8)-9;
    leg(:,9)=t5_gnd*[0;0;4.5;1];
    leg(:,10)=leg(:,9);
    leg(2,10)=leg(2,10)-2;
    leg(:,11)=leg(:,10);
    leg(1,11)=leg(1,11)+9;
    leg(:,12)=leg(:,11);
    leg(2,12)=leg(2,12)+2;
    leg(:,13)=leg(:,6);
    leg(:,14)=leg(:,9);
    leg(:,3)=leg(:,2);
 

end

