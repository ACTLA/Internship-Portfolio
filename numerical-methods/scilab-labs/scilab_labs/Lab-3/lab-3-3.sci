// Первая поверхность
x = -10:0.5:10; y = -10:0.5:10;
[X, Y] = ndgrid(x, y);
Z1 = X.^2 + Y + X .* Y.^2;

// Вторая поверхность
t = -%pi:0.1:%pi;
Z2 = sin(t)' * cos(t);
x2 = t; y2 = t;

// Объединяем
[xx1, yy1, zz1] = genfac3d(x, y, Z1);
[xx2, yy2, zz2] = genfac3d(x2, y2, Z2);

plot3d([xx1 xx2], [yy1 yy2], [zz1 zz2], theta=50, alpha=60, flag=[2,2,4]);
