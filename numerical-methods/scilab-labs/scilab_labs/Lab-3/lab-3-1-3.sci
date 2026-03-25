x = -3:0.1:3;
y = -3:0.1:3;
[X, Y] = ndgrid(x, y);
Z = X.^2 + Y.^2;
plot3d(x, y, Z);
