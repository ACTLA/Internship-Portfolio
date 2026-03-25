// Задание 7
function dy = f(t, y)
    dy(1) = -3*y(1) + 12
    dy(2) = 2.5*y(1) - 1.25*y(2)
endfunction
y0 = [0; 3]
t0 = 0
t = 0:1:5
solution = ode(y0, t0, t, f)
plot(t, solution)
