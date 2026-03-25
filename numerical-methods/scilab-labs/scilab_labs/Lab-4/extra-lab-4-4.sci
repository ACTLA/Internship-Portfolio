// -------------------------------------------------
// ЗАДАНИЕ 4. Интеграл Коши (формально через intg)
// -------------------------------------------------

// 1) ∫[1,5] √(x²-2x)/x³ dx
function y = f1(x)
    y = sqrt(x.^2 - 2*x)./x.^3;
endfunction
result1 = intc(1, 5, f1);
disp("1) ∫√(x²-2x)/x³dx = " + string(result1));

// 2) ∫[1,π] dx/sin³(3x)
function y = f2(x)
    y = 1./(sin(3*x).^3);
endfunction
result2 = intc(1, %pi, f2);
disp("2) ∫dx/sin³(3x) = " + string(result2));

// 3) ∫[3,8] (x⁴ + 4x - 9) dx
function y = f3(x)
    y = x.^4 + 4*x - 9;
endfunction
result3 = intc(3, 8, f3);
disp("3) ∫(x⁴+4x-9)dx = " + string(result3));

// 4) ∫[-2π,2π] sin⁵(x)·cos²(x) dx
function y = f4(x)
    y = sin(x).^5 .* cos(x).^2;
endfunction
result4 = intc(-2*%pi, 2*%pi, f4);
disp("4) ∫sin⁵(x)·cos²(x)dx = " + string(result4));

// 5) ∫[-1,1] (x²*x/(x+2) + x⁵) dx
function y = f5(x)
    y = (x.^2 .* x)./(x+2) + x.^5;
endfunction
result5 = intc(-1, 1, f5);
disp("5) ∫(x²*x/(x+2) + x⁵)dx = " + string(result5));

// 6) ∫[1,5] (8x³ - 2) dx
function y = f6(x)
    y = 8*x.^3 - 2;
endfunction
result6 = intc(1, 5, f6);
//disp("6) ∫(8x³-2)dx = " + string(result6));
