import numpy as np
from scipy import stats

# Задание №1
# Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weight = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
football_hockey_weight = np.concatenate([football, hockey, weight])

total_mean = np.mean(football_hockey_weight)
football_mean = np.mean(football)
hockey_mean = np.mean(hockey)
weight_mean = np.mean(weight)

SSW = sum((football - football_mean)**2) + sum((hockey - hockey_mean)**2) + sum((weight - weight_mean)**2)
SSW_df = len(football) + len(hockey) + len(weight) - 3

SSB = len(football) * ((football_mean - total_mean)**2) + len(hockey) * ((hockey_mean - total_mean)**2) + len(weight) * ((weight_mean - total_mean)**2)
SSB_df = 3 - 1

F_obs = (SSB / SSB_df) / (SSW / SSW_df)
print(f'F-расчетный составляет {F_obs}')
# F-расчетный составляет 5.500053450812599

# F_таб равняется  3.39
# Принимает гипотезу H1 о неравестве средних значений.

stats.f_oneway(football, hockey, weight)
print(f'F-расчетный составляет {stats.f_oneway(football, hockey, weight)[0]}')
# F-расчетный составляет 5.500053450812596

print(f'pvalue составляет {stats.f_oneway(football, hockey, weight)[1]}')
# pvalue составляет 0.010482206918698694

# 0.05 > pvalue (0.01)
# Принимает гипотезу H1 о неравестве средних значений.