t = %pi:0.01:4*%pi;
x = t .* cos(t);
y = t .* sin(t);
z = t .* abs(t) / (50*%pi);
param3d(x, y, z);
