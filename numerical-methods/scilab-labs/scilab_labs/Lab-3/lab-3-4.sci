u = 0:0.01:2*%pi;
v = 0:0.01:8*%pi;
X = (cos(u) .* u)' * (1 + cos(v)/2);
Y = (u/2)' * sin(v);
Z = (sin(u) .* u)' * (1 + cos(v)/2);
plot3d2(X, Y, Z);
