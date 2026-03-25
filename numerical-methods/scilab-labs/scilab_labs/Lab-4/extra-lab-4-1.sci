// -------------------------------------------------
// ЗАДАНИЕ 1. Интегрирование по методу трапеции (inttrap)
// -------------------------------------------------

// 1) ∫[-1,1] √(x² - 2x) dx
x = -1:0.001:1;
y = sqrt(x.^2 - 2*x);
result1 = inttrap(x, y);
disp("1) ∫√(x²-2x)dx = " + string(result1));

// 2) ∫[π,2π] cos(x) dx
x = %pi:0.001:2*%pi;
y = cos(x);
result2 = inttrap(x, y);
disp("2) ∫cos(x)dx = " + string(result2));

// 3) ∫[0,π] √(1+cos(2x))/sin(x) dx
x = 0.001:0.001:%pi-0.001; // избегаем 0 и π
y = sqrt(1+cos(2*x))./sin(x);
result3 = inttrap(x, y);
disp("3) ∫√(1+cos(2x))/sin(x)dx = " + string(result3));

// 4) ∫[-5,3] (6x³ - 4x²) dx
x = -5:0.001:3;
y = 6*x.^3 - 4*x.^2;
result4 = inttrap(x, y);
disp("4) ∫(6x³-4x²)dx = " + string(result4));

// 5) ∫[0,1] (e⁴ˣ + x) dx
x = 0:0.001:1;
y = exp(4*x) + x;
result5 = inttrap(x, y);
disp("5) ∫(e⁴ˣ+x)dx = " + string(result5));

// 6) ∫[-7,14] (x³-x²+9)/(x⁴-5) dx
x = -7:0.001:14;
y = (x.^3 - x.^2 + 9)./(x.^4 - 5);
result6 = inttrap(x, y);
disp("6) ∫(x³-x²+9)/(x⁴-5)dx = " + string(result6));
