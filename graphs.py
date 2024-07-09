import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_train.csv')

# print(sns.scatterplot(data=df, x='longitude', y='latitude'))

# print(sns.scatterplot(data=df, x='households', y='population',
# hue='totalRooms', size=10))

# cols = ['population', 'medianIncome', 'housingMedianAge',
#         'medianHouseValue']
# g = sns.PairGrid(df[cols])
#
# print(g.map(sns.scatterplot))


# ТО ЧТО СВЕРХУ ИЗОБРАЖЕНИЕ СТАТИСТИЧЕСКИХ ОТНОШЕНИЙ

# print(sns.relplot(x='latitude', y='medianHouseValue', kind='line', data=df))

# print(sns.scatterplot(data=df, x='latitude', y='longitude', hue='medianHouseValue'))

# print(sns.histplot(data=df, x='medianIncome'))

# print(sns.histplot(data=df, x='housingMedianAge'))



# df['medianIncome'] = df['medianIncome'] * 1000
#
# # Фильтрация данных для medianIncome в диапазоне от 0 до 15 000 долларов
# filtered_df = df[df['medianIncome'].between(0, 15000)]
#
# # Выводим результат
# print(filtered_df)



# df.loc[df['housingMedianAge'] <= 20, 'age_group'] = 'Young'
# df.loc[(df['housingMedianAge'] > 20) & (df['housingMedianAge'] <= 50), 'age_group'] = 'Middle-aged'
# df.loc[df['housingMedianAge'] > 50, 'age_group'] = 'Old'
#
# df.groupby('age_group')['medianIncome'].mean().plot(kind='bar')




df.loc[df['medianIncome'] > 6, 'income_group'] = 'rich'
df.loc[df['medianIncome'] <= 6, 'income_group'] = 'poor'

print(sns.histplot(data=df, x='medianHouseValue', hue='income_group'))

plt.show()
