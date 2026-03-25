// Задание 1 - Метод трапеций
x = -5:0.001:3;
y = 6*x.^3 - 4*x.^2;
inttrap(x, y)

// Задание 2 - Квадратура
integrate('3*exp(x) - sin(x)', 'x', 0, 5)

// Задание 3 - Непрерывные функции
function y = f(x)
    y = x.^3 + 4*x;
endfunction
intg(5, 10, f)

// Задание 4 - Интеграл Коши
function y = g(x)
    y = x.^4 + 4*x - 9;
endfunction
intc(3, 8, g)

// Задание 5 - Дифференцирование
x = 1:0.1:2;
y = x.^2 + 3*x + 1;
dy = diff(y);
dx = diff(x);
derivative = dy./dx;
derivative
