// 1) x = 8(cos(t)-cos(4t)/4), y = 8(sin(t)-sin(4t)/4)
t = 0:0.01:2*%pi;
x = 8*(cos(t) - cos(4*t)/4);
y = 8*(sin(t) - sin(4*t)/4);
plot(x, y, 'r-');
xgrid();
xtitle('Параметрический график 1', 'x', 'y');
scf()
// 2) x = 16sin(t)³, y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)
x = 16*sin(t).^3;
y = 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t);
plot(x, y, 'b-');
xtitle('Параметрический график 2', 'x', 'y');
