# Изоброзите отношение households к population
# Визуалировать longitude по отношения к medianHouseValue использую Линейный график
# Предоставить гистограмму по housingMedianAge
# Изоброзить гистограмму по medianHouseValue с оттенком houseMedianAge
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_csv('../california_housing_train.csv')


# Визуализация отношения households к population
sb.scatterplot(data=df, x='households', y='population')
plt.show()



# Визуализация longitude по отношения к medianHouseValue
plt.figure(figsize=(10,6 ))
sb.scatterplot(data=df, x='longitude', y='medianHouseValue', alpha=0.5)
sb.relplot(data=df, x='longitude', y='medianHouseValue', kind='line')
plt.xlabel('Longitude')
plt.ylabel('Median House Value')
plt.title('House prices by Longitude')
plt.show()


# Визуализация latitude по отношения к medianHouseValue
sb.scatterplot(data=df, x='latitude', y='medianHouseValue')
sb.relplot(data=df, x='latitude', y='medianHouseValue', kind='line')
plt.show()


# Предоставить гистограмму по housingMedianAge
sb.histplot(data=df, x='housingMedianAge')
plt.show()


# Изоброзить гистограмму по medianHouseValue с оттенком houseMedianAge
sb.histplot(data=df, x='medianHouseValue', hue='housingMedianAge')
plt.show()

# Визуализация medianIncome в диапазоне от 0 до 15 000 долларов
filtered_df = df[df['medianIncome'].between(0, 15)]
sb.histplot(data=filtered_df, x='medianIncome')
plt.show()

# Визуализация medianIncome в диапазоне от 0 до 15 000 долларов с оттенком housingMedianAge
sb.histplot(data=filtered_df, x='medianIncome', hue='housingMedianAge')
plt.show()

# Визуализация medianIncome в диапазоне от 0 до 15 000 долларов с оттенком housingMedianAge и medianHouseValue
sb.histplot(data=filtered_df, x='medianIncome', hue='housingMedianAge', multiple='stack')
sb.histplot(data=filtered_df, x='medianHouseValue', hue='housingMedianAge', multiple='stack')
plt.show()




plt.show()