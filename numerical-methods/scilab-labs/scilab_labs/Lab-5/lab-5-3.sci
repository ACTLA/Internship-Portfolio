// Задание 3
deff('[y]=f(x)', 'y=cos(x)-0.2*x')
x = -2*%pi:0.1:2*%pi;
fsolve(1, f)  
plot(x, cos(x)-0.2*x)
xgrid()
