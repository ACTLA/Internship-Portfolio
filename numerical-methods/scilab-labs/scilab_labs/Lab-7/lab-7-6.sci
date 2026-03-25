// Генерация данных
x = 0:0.2:5;
y_clean = x .* cos(3*x);
noise = 0.3 * rand(1, length(x)) - 0.15;  // Белый шум [-0.15, 0.15]
y_noisy = y_clean + noise;

// Подгонка полиномом 4-й степени
deff('e = G(p, z)', 'e = z(2) - p(1) - p(2)*z(1) - p(3)*z(1)^2 - p(4)*z(1)^3 - p(5)*z(1)^4');

Z = [x; y_noisy];
p0 = [0; 0; 0; 0; 0];

[p, err] = datafit(G, Z, p0);

// Результаты
x_fit = 0:0.05:5;
y_fit = p(1) + p(2)*x_fit + p(3)*x_fit.^2 + p(4)*x_fit.^3 + p(5)*x_fit.^4;

scf();
plot(x, y_noisy, 'ro', 'markersize', 6);
plot(x, y_clean, 'g-', 'linewidth', 1);
plot(x_fit, y_fit, 'b-', 'linewidth', 2);
xtitle('Аппроксимация зашумленных данных (задание 6.1)');
xlabel('x'); ylabel('y');
legend('Зашумленные данные', 'Исходная функция y=x·cos(3x)', 'Аппроксимация полиномом 4-й степени', 2);
xgrid();
