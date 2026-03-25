// 3) r = 2*sin(6φ)
phi = 0:0.01:2*%pi;
r = 2*sin(6*phi);
polarplot(phi, r);
