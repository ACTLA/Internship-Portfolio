// 2) r = a*cos(φ) + b - улитка Паскаля
a = 2; b = 3;
phi = 0:0.01:2*%pi;
r = a*cos(phi) + b;
polarplot(phi, r);
