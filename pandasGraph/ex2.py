# Использовать 2-3 точечных графика
# Применить доп измерение hue, size, stile
# Использовать PairGrid
# Изобразить Heatmap
# 2-3 гистограммы
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

print(df.columns)

sns.scatterplot(data=df, x='bill_depth_mm', y='bill_length_mm', hue='sex', size=5)
plt.show()

sns.scatterplot(data=df, x='body_mass_g', y='flipper_length_mm',hue='sex', size=5)
plt.show()

sns.scatterplot(data=df, x='island', y='body_mass_g', hue='sex', size=5)
plt.show()

list = ['species', 'island', 'bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex']

g = sns.PairGrid(df[list])
g.map(sns.scatterplot)
plt.show()



numerical_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
correlation_matrix = df[numerical_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()



sns.histplot(data=df, x='bill_length_mm')
plt.show()

sns.histplot(data=df, x='body_mass_g')
plt.show()