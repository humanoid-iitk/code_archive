function [ t1,t2 ] = find_angles( x,xa,h,ha )
    t1= 2*atan((60*(x - xa))/(h^2 - 2*h*ha + 30*h + ha^2 - 30*ha + x^2 - 2*x*xa + xa^2) + (30*xa - 30*x + (-(h^2 - 2*h*ha + ha^2 + x^2 - 2*x*xa + xa^2)*(h^2 - 2*h*ha + ha^2 + x^2 - 2*x*xa + xa^2 - 900))^(1/2))/(h^2 - 2*h*ha + 30*h + ha^2 - 30*ha + x^2 - 2*x*xa + xa^2));
    t2= -2*atan((30*xa - 30*x + (-(h^2 - 2*h*ha + ha^2 + x^2 - 2*x*xa + xa^2)*(h^2 - 2*h*ha + ha^2 + x^2 - 2*x*xa + xa^2 - 900))^(1/2))/(h^2 - 2*h*ha + 30*h + ha^2 - 30*ha + x^2 - 2*x*xa + xa^2));
end

