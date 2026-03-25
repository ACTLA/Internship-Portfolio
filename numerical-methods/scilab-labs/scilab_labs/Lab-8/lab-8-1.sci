// Данные
X = [2.56, 0.68, 0.98, 2.43, 4.34, 7.45, 0.98, 5.91, 3.87, 2.43, 2.56, 7.45, 0.98, 2.43, 5.91, 0.98];
Y = [10.56, 7.98, 8.56, 6.34, 4.98, 8.56, 10.56, 7.98, 8.56, 9.23, 6.34, 8.56, 8.56, 10.56, 7.98, 10.56];

// 1) Среднее значение
mean_X = mean(X)
mean_Y = mean(Y)

// 2) Медиана
median_X = median(X)
median_Y = median(Y)

// 3) Дисперсия
variance_X = variance(X)
variance_Y = variance(Y)

// 4) Частота появления значений
freq_X = tabul(X)
freq_Y = tabul(Y)

// 5) Стандартное отклонение
stdev_X = stdev(X)
stdev_Y = stdev(Y)

// Упорядочение данных
sorted_X = gsort(X, 'g', 'i')  // по возрастанию
sorted_Y = gsort(Y, 'g', 'i')  // по возрастанию

// Вывод результатов
disp("X - Среднее: " + string(mean_X) + ", Медиана: " + string(median_X) + ", Дисперсия: " + string(variance_X) + ", Станд.отклонение: " + string(stdev_X))
disp("Y - Среднее: " + string(mean_Y) + ", Медиана: " + string(median_Y) + ", Дисперсия: " + string(variance_Y) + ", Станд.отклонение: " + string(stdev_Y))
