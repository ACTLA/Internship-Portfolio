// Задание 4
function ydot = f(x, y)
    ydot = x + y
endfunction

y0 = 1; 
x0 = 0;
x = 0:0.1:2;  
solution = ode(y0, x0, x, f)

plot(x, solution)
xgrid()
xtitle('Решение ОДУ: dy/dx = x + y')
xlabel('x')
ylabel('y')
