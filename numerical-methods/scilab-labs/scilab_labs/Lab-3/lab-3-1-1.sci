x = -2:0.1:2;          
y = -2:0.1:2;          
[X, Y] = ndgrid(x, y); 
Z = X.^2 .* Y.^2 + 3;  
plot3d(x, y, Z);       
