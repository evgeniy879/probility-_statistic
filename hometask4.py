# Задание №1
# Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.

M_x = (200 + 800) / 2
D_x = ((800 - 200) ** 2) / 12

print(f'Среднее значение составляет {M_x}')
# Среднее значение составляет 500
print(f'Дисперсия D_x составляет {D_x}')
# Дисперсия D_x составляет 30000

# Задание №2
# О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5? Если да, найдите ее.
# Подставим в уравнение данные, кторые у нас есть и получим следующее:
# 0,2 = (x - 0,5) ** 2 / 12
# избавимся от квадрата путем возведения обе части уравнения в квадрат
# 0,2 ** 1/2 = (x-0.5)/ 12 ** 1/2
# умножим на корень из 12 обе части уравнения
# 2,4 ** 1/2 = x-0.5
# 1.5+0.5 = x

# Правая граница равняется 2
# среднее значение (0.5 + 2) / 2 = 1.2


# Задание №3
# Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2*pi))) * (exp(-((x+2)**2) / 32))
# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)

# M(x) = -2
# D(x) = 16
# Std(x) = 4

# Задание №4
# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.

# больше 182 см
# 182 -174 / 8 = 0,84%
# 1 - 0,84 = 16%
# больше 190 см
# 190 -174 / 8 = 0,977
# 1 - 0,977 = 2.3%
# от 166 см до 190 см
# 166 -174 / 8 = 0,16
# 190 -174 / 8 = 0,977
# 97% - 16%= 82%
# от 166 см до 182 см
# 166 -174 / 8 = 0,16
# 182 -174 / 8 = 0,84%
# 84% - 16% = 68%
# от 158 см до 190 см
# 158 -174 / 8 = 0,02%
# 190 -174 / 8 = 0,977
# 97% - 2% = 95%
# не выше 150 см = 0.14% или не ниже 190 см
# 150 -174 / 8 = 0,0014%
# 190 -174 / 8 = 0,977%
# 1 - 0,977= 2.3%
# не выше 150 см или не ниже 198 см
# 150 -174 / 8 = 0,0014%
# 198 -174 / 8 = 0,0014%
# ниже 166 см
# 166 -174 / 8 = 0,16%

# Задание №5
# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см,
# от математического ожидания роста в популяции, в которой $M(X)$ = 178 см и $D(X)$ = 25 кв.см?
# 178 - 190 / 5 = 2.4 сигмы