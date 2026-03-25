// 1) f1 = sin(x)/x, f2 = cos(x), f3 = sin(x)³
x = 0:0.01:%pi;
f1 = sin(x)/x;
f2 = cos(x);
f3 = sin(x).^3;

plot(x, f1, 'r-', x, f2, 'b--', x, f3, 'g:');
xgrid();
xtitle('Тригонометрические функции', 'x', 'y');
legend('sin(x)/x', 'cos(x)', 'sin(x)^3', 1);
