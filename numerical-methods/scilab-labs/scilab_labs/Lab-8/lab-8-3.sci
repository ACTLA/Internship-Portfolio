// 1) Первая матрица
x1 = [3.679, 4.675, %nan; 5.560, 7.953, 2.761; 3.762, 4.321, 8.562];
stdev1 = nanstdev(x1)
stdev1_rows = nanstdev(x1, 'r')  // по строкам
stdev1_cols = nanstdev(x1, 'c')  // по столбцам

// 2) Вторая матрица
f2 = [0.7642, 0.7302; 0.4531, %nan];
stdev2 = nanstdev(f2)

// 3) Третья матрица
y3 = [0.98654, %nan; 0.86531, 1.00541];
stdev3 = nanstdev(y3)

disp("Станд.отклонение 1: " + string(stdev1))
disp("Станд.отклонение 2: " + string(stdev2))
disp("Станд.отклонение 3: " + string(stdev3))
