// Задание 6
function y = f(x)
    y(1) = x(1)^2 + 3*x(2) - 2
    y(2) = x(1)^3 - 2*x(2) - 1
endfunction

x0 = [1; 0]
fsolve(x0, f)
