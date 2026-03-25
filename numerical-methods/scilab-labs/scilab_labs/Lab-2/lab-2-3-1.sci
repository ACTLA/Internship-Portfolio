// 1) r = a*cos(4φ) - роза
a = 2;
phi = 0:0.01:2*%pi;
r = a*cos(4*phi);
polarplot(phi, r);
