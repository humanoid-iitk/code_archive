arm=zeros(2,3);
line=zeros(2,2);
line(:,1)=[0;20];
line(:,2)=[10,10];
for i=0:100
    x=i*0.1;
    y=20-x;
    arm(:,3)=[x;y];
    arm(:,2)=find_point(x,y);
    plot(arm(1,:),arm(2,:),'r -o',line(1,:),line(2,:));
    hold off;
    pause(0.001);
end