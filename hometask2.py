from math import factorial
from math import e

# Задание №1
# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

# Это Биноминальное распределение.
probility_1 = int(factorial(100)/(factorial(85) * (factorial(100-85)))) * 0.8**85 * 0.2**15
print(f'вероятность того, что стрелок попадет в цель ровно 85 раз составляет {probility_1}')

# Задание №2
# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?

# Это распределение Пуассона
# Находим Лямбду
lambda_ = 0.0004 * 5000
print(f'Значение Лямбды составило {lambda_}')

probility_2 = (lambda_ ** 0 / int(factorial(0))) * e**-lambda_
print(f'Значение вероятности того, что ни одна из лампочек не перегорит в первый день составило {probility_2}')

probility_2_1 = (lambda_ ** 2 / int(factorial(2))) * e**-lambda_
print(f'Значение вероятности того,  что перегорят ровно две лампочки составило {probility_2_1}')


# Задание №3
# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
# Это Биноминальное распределение.
probility_3 = int(factorial(144)/(factorial(70) * (factorial(144-70)))) * 0.5**70 * 0.5**74
print(f'вероятность того, что орел выпадет ровно 70 раз {probility_3}')

# Задание №4
# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?

# Для начала надем вероятность того, что все мячи белые
probility_4 = 7/10 * 6/9 * 9/11 * 8/10
print(f'вероятность того, что все мячи белые составляет {probility_4}')

# Находим вероятность того, что ровно два мяча белые
# Первый вариант: из одного ящика достаем 1 белый и 1 черный, из другого также 1 белый и 1 черный
probility_1_white_1_black = int((factorial(7)/(factorial(1)*factorial(7-1)))
                                *(factorial(3)/(factorial(1)*factorial(3-1))))/(factorial(10)/(factorial(2)*factorial(10-2)))* \
                                    int((factorial(9)/(factorial(1)*factorial(9-1)))
                                *(factorial(2)/(factorial(1)*factorial(2-1))))/(factorial(11)/(factorial(2)*factorial(11-2)))

# Второй вариант: из первого ящика достаем только черные шары, из второго ящика только белые
probility_0_white_2_white = factorial(3)/(factorial(2)*factorial(3-2)) / (factorial(10)/(factorial(2)*factorial(10-2))) \
                            * factorial(9)/(factorial(2)*factorial(9-2)) / (factorial(11)/(factorial(2)*factorial(11-2)))

# Третий вариант: из первого ящика достаем два белых шара, из второго ящика 2 черных
probility_2_white_0_black = factorial(7)/(factorial(2)*factorial(7-2)) / (factorial(10)/(factorial(2)*factorial(10-2))) \
                            * factorial(2)/(factorial(2)*factorial(2-2)) / (factorial(11)/(factorial(2)*factorial(11-2)))

total_probility = probility_1_white_1_black + probility_0_white_2_white + probility_2_white_0_black
print(f'Вероятность того, что ровно два мяча белые {total_probility:.3f}')


# Находим вероятность того, что хотя бы один мяч белый?
#
# Нам нужна сумма всех вероятностей следующих комбинаций:
#
# Комбинация 1 - 1 ящик: 2 черных, 2 ящик: 1 белый и 1 черный
# Комбинация 2 - 1 ящик: 2 черных, 2 ящик: 2 белых
# Комбинация 3 - 1 ящик: 1 белый и 1 черный, 2 ящик: 1 белый и 1 черный
# Комбинация 4 - 1 ящик: 1 белый и 1 черный, 2 ящик: 2 белых
# Комбинация 5 - 1 ящик: 1 белый и 1 черный, 2 ящик: 2 черных
# Комбинация 6 - 1 ящик: 2 белых, 2 ящик: 2 черных
# Комбинация 7 - 1 ящик: 2 белых, 2 ящик: 1 белый и 1 черный
# Комбинация 8 - 1 ящик: 2 белых, 2 ящик: 2 белых


probility_com1 = factorial(3)/(factorial(2)*factorial(3-2)) / (factorial(10)/(factorial(2)*factorial(10-2))) *\
                    int((factorial(9)/(factorial(1)*factorial(9-1)))
                                *(factorial(2)/(factorial(1)*factorial(2-1))))/(factorial(11)/(factorial(2)*factorial(11-2)))
probility_com2 = factorial(3)/(factorial(2)*factorial(3-2)) / (factorial(10)/(factorial(2)*factorial(10-2))) *\
                    factorial(9)/(factorial(2)*factorial(9-2)) / (factorial(11)/(factorial(2)*factorial(11-2)))
probility_com3 =int((factorial(7)/(factorial(1)*factorial(7-1)))
                                *(factorial(3)/(factorial(1)*factorial(3-1))))/(factorial(10)/(factorial(2)*factorial(10-2)))* \
                                    int((factorial(9)/(factorial(1)*factorial(9-1)))
                                *(factorial(2)/(factorial(1)*factorial(2-1))))/(factorial(11)/(factorial(2)*factorial(11-2)))
probility_com4 = int((factorial(7)/(factorial(1)*factorial(7-1)))
                                *(factorial(3)/(factorial(1)*factorial(3-1))))/(factorial(10)/(factorial(2)*factorial(10-2)))* \
                                 factorial(9)/(factorial(2)*factorial(9-2)) / (factorial(11)/(factorial(2)*factorial(11-2)))
probility_com5 = int((factorial(7)/(factorial(1)*factorial(7-1)))
                                *(factorial(3)/(factorial(1)*factorial(3-1))))/(factorial(10)/(factorial(2)*factorial(10-2)))* \
                                factorial(2)/(factorial(2)*factorial(2-2)) / (factorial(11)/(factorial(2)*factorial(11-2)))
probility_com6 = factorial(7)/(factorial(2)*factorial(7-2)) / (factorial(10)/(factorial(2)*factorial(10-2))) * \
                    factorial(2)/(factorial(2)*factorial(2-2)) / (factorial(11)/(factorial(2)*factorial(11-2)))
probility_com7 = factorial(7)/(factorial(2)*factorial(7-2)) / (factorial(10)/(factorial(2)*factorial(10-2))) * \
                    int((factorial(9)/(factorial(1)*factorial(9-1)))
                                *(factorial(2)/(factorial(1)*factorial(2-1))))/(factorial(11)/(factorial(2)*factorial(11-2)))
probility_com8 = factorial(7)/(factorial(2)*factorial(7-2)) / (factorial(10)/(factorial(2)*factorial(10-2))) * \
                factorial(9)/(factorial(2)*factorial(9-2)) / (factorial(11)/(factorial(2)*factorial(11-2)))
probility_total_com = probility_com1 + probility_com2 + probility_com3 + probility_com4 + probility_com5 + \
                        probility_com6 + probility_com7 + probility_com8
print(f'вероятность того, что хотя бы один мяч белый {probility_total_com:.3f}')
