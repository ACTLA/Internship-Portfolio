// 3) f1 = 10sin²t, f2 = 10cos²t, f3 = sin(10t)
t = 0:0.01:%pi;
f1 = 10*sin(t).^2;
f2 = 10*cos(t).^2;
f3 = sin(10*t);

plot(t, f1, 'r-', t, f2, 'b--', t, f3, 'g:');
xgrid();
xtitle('Функции от t', 't', 'y');
legend('10sin(t)^2', '10cos(t)^2', 'sin(10t)', 1);
