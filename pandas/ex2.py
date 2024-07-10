# УПР 2
# Проверить есть ли в файле пустые значения
# Показать medianHouseValue где mediaIncome < 2
# Показать данные в первых 2 столбцах
# Выбрать данные где housingMedianAge < 20 и medianHouseValue > 70000

import pandas as pd

df = pd.read_csv('../california_housing_train.csv')

# Проверка на пустые значения
print(df.isnull().sum())

# Показать medianHouseValue где mediaIncome < 2
print(df[df['medianIncome'] < 2]['medianHouseValue'])

# Показать данные в первых 2 столбцах
for i in df.columns[:2]:
    print(df[i])


# Выбрать данные где housingMedianAge < 20 и medianHouseValue > 70000
# первые 5
# только население
print(df[(df['housingMedianAge'] < 20) & (df['medianHouseValue'] > 70000)])
print(df[(df['housingMedianAge'] < 20) & (df['medianHouseValue'] > 70000)].head(5))
print(df[(df['housingMedianAge'] < 20) & (df['medianHouseValue'] > 70000)]['population'])