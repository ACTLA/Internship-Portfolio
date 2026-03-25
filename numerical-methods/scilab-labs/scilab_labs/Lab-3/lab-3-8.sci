t = -%pi:0.01:%pi;           
m = 5 * sin(t)' * cos(t).^3; 
grayplot(t, t, m);           
