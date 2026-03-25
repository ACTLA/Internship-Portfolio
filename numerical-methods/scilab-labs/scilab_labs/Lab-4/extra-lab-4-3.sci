// -------------------------------------------------
// ЗАДАНИЕ 3. Интегрирование для непрерывной функции (intg)
// -------------------------------------------------

// 1) ∫[0,1] (x^(2+x)*x/(x+2) + x^x) dx
function y = f1(x)
    y = (x.^(2+x) .* x)./(x+2) + x.^x;
endfunction
result1 = intg(0, 1, f1);
disp("1) ∫(x^(2+x)*x/(x+2) + x^x)dx = " + string(result1));

// 2) ∫[0,1] (tan(x^(2+x))*x/(x+2) + x dx
function y = f2(x)
    y = tan(x.^(2+x)) .* x./(x+2) + x;
endfunction
result2 = intg(0, 1, f2);
disp("2) ∫(tan(x^(2+x))*x/(x+2) + x)dx = " + string(result2));

// 3) ∫[5,10] (x³ + 4x) dx
function y = f3(x)
    y = x.^3 + 4*x;
endfunction
result3 = intg(5, 10, f3);
disp("3) ∫(x³+4x)dx = " + string(result3));

// 4) ∫[-π,π] sin(x) dx
function y = f4(x)
    y = sin(x);
endfunction
result4 = intg(-%pi, %pi, f4);
disp("4) ∫sin(x)dx = " + string(result4));

// 5) ∫[1,10] (3x³ + 5x - 7) dx
function y = f5(x)
    y = 3*x.^3 + 5*x - 7;
endfunction
result5 = intg(1, 10, f5);
disp("5) ∫(3x³+5x-7)dx = " + string(result5));

// 6) ∫[1,π] sin(12x)·cos(6x) dx
function y = f6(x)
    y = sin(12*x) .* cos(6*x);
endfunction
result6 = intg(1, %pi, f6);
disp("6) ∫sin(12x)·cos(6x)dx = " + string(result6));
