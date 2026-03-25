// -------------------------------------------------
// ЗАДАНИЕ 2. Интегрирование по квадратуре (integrate)
// -------------------------------------------------

// 1) ∫[0,5] (3eˣ - sin(x)) dx
result1 = integrate('3*exp(x) - sin(x)', 'x', 0, 5);
disp("1) ∫(3eˣ-sin(x))dx = " + string(result1));

// 2) ∫[-1,4] x²/√(x²+4) dx
result2 = integrate('x^2/sqrt(x^2+4)', 'x', -1, 4);
disp("2) ∫x²/√(x²+4)dx = " + string(result2));

// 3) ∫[2,8] 5/(x√(9+x²)) dx
result3 = integrate('5/(x*sqrt(9+x^2))', 'x', 2, 8);
disp("3) ∫5/(x√(9+x²))dx = " + string(result3));

// 4) ∫[7,10] (2x²-4x+5)/√(x²+2x) dx
result4 = integrate('(2*x^2-4*x+5)/sqrt(x^2+2*x)', 'x', 7, 10);
disp("4) ∫(2x²-4x+5)/√(x²+2x)dx = " + string(result4));

// 5) ∫[π,2π] cos⁵(x) dx
result5 = integrate('cos(x)^5', 'x', %pi, 2*%pi);
disp("5) ∫cos⁵(x)dx = " + string(result5));

// 6) ∫[1,2π] 5/cos(x) dx
result6 = integrate('5/cos(x)', 'x', 1, 2*%pi);
disp("6) ∫5/cos(x)dx = " + string(result6));
