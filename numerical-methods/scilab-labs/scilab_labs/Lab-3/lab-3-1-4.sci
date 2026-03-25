x = -2*%pi:0.2:2*%pi;
y = -2*%pi:0.2:2*%pi;
[X, Y] = ndgrid(x, y);
Z = X .* cos(Y) + Y .* sin(X);
plot3d(x, y, Z);
