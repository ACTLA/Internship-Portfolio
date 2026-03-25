x = [2, 2.13, 2.25, 2.38, 2.5, 2.63, 2.75, 2.88, 3.12];
Y = [12.57, 16.43, 19, 22.86, 26.71, 31.86, 37.0, 43.43, 49.86];

deff('e = G(p, z)', 'e = z(2) - p(1)*z(1)^4 - p(2)*z(1)^3 - p(3)');

Z = [x; Y];
p0 = [1; 1; 1];

[p, err] = datafit(G, Z, p0);

disp("Параметры модели:");
disp("A = " + string(p(1)));
disp("B = " + string(p(2)));
disp("K = " + string(p(3)));
disp("Ошибка: " + string(err));

x_fit = 2:0.05:3.12;
Y_fit = p(1)*x_fit.^4 + p(2)*x_fit.^3 + p(3);

scf();
plot(x, Y, 'ro', 'markersize', 8);
plot(x_fit, Y_fit, 'b-', 'linewidth', 2);
xtitle('Аппроксимация datafit (задание 8.1)');
xlabel('x'); ylabel('Y');
legend('Экспериментальные данные', 'Аппроксимация Y(x)=A·x⁴+B·x³+K', 2);
xgrid();
