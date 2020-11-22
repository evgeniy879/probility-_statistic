from math import factorial

# Задача №1
# Найти вероятность того, что все карты – крести
probility_cards = 13/52 * 12/51 * 11/50 * 10/49
print(f'Вероятность того, что все карты крести составляет {probility_cards}')

# Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
total = int(factorial(52)/(factorial(4)*factorial(52-4)))
print(f'Oбщее количество комбинаций из 4 карт {total} ')

ace_1 = int(factorial(4)/(factorial(1)*factorial(4-1))) * int(factorial(48)/(factorial(3)*factorial(48-3)))
print(f'Oбщее количество комбинаций состоящих из 1 туза и 3 карт "не туз"  {ace_1} ')

ace_2 = int(factorial(4)/(factorial(2)*factorial(4-2))) * int(factorial(48)/(factorial(2)*factorial(48-2)))
print(f'Oбщее количество комбинаций состоящих из 2 тузов и 2 карт "не туз"  {ace_2} ')

ace_3 = int(factorial(4)/(factorial(3)*factorial(4-3))) * int(factorial(48)/(factorial(1)*factorial(48-1)))
print(f'Oбщее количество комбинаций состоящих из 3 тузов и 1 карт "не туз"  {ace_3} ')

ace_4 = int(factorial(4)/(factorial(3)*factorial(4-3))) * int(factorial(48)/(factorial(1)*factorial(48-1)))
print(f'Oбщее количество комбинаций состоящих из 3 тузов и 1 карт "не туз"  {ace_3} ')

total_ace = ace_1 + ace_2 + ace_3 + ace_4
print(f'Oбщее количество комбинаций, в которых есть хотябы 1 туз  {total_ace} ')

probility = total_ace / total
print(f'Вероятность что среди 4-х карт окажется хотя бы один туз {probility} ')

# Задача №2
# На входной двери подъезда установлен кодовый замок,
# содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки

total_combination = int(factorial(10)/(factorial(3) * factorial(10-3)))
probility_lock = 1 / total_combination
print(f'Вероятность того, что откроется дверь с первой попытки {probility_lock} ')

# Задача №3
probility_15 = 9/15 * 8/14 * 7/13
print(f'Вероятность того, что все извлеченные детали окрашены {probility_15} ')

# Задача №4
probility_lotery = 2/100 * 1/99
print(f'Вероятность того,  2 приобретенных билета окажутся выигрышными {probility_lotery} ')



