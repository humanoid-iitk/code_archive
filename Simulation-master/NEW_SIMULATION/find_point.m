function [ arm ] = find_point( x,y )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

syms a b;
answ=solve(10*cos(a)+10*cos(b)==x,10*sin(a)+10*sin(b)==y,a>0,a<=pi/2,a,b);
m=answ.a;
arm=[10*cos(m);10*sin(m)];

end

