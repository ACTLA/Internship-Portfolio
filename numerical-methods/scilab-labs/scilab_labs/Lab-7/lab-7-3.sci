x = [0, 5, 15, 25, 30, 35, 40];
y = [0, 20, -10, 0, 20, 30, 40];

// Сглаживание
ptd = [x; y];
pt = smooth(ptd, 0.5);

scf();
plot(x, y, 'ro-', 'markersize', 8, 'linewidth', 1);
plot(pt(1,:), pt(2,:), 'b-', 'linewidth', 2);
xtitle('Сглаживание (задание 3.1)');
xlabel('F'); ylabel('S');
legend('Исходные данные', 'Сглаженные данные', 2);
xgrid();
