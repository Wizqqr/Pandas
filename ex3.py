import pandas as pd

df = pd.read_csv('california_housing_train.csv')

print(df['medianHouseValue'].min())
print(df['medianHouseValue'].max())

print(df[(df['medianIncome'] == 3.1250)]['medianHouseValue'].max())


minValue = df['medianHouseValue'].min()
print(df[(df['medianHouseValue'] == minValue)]['population'].max())