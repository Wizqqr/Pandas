import pandas as pd

df = pd.read_csv('california_housing_train.csv')

print(df.head())

# print(df.tail())
#
# print(df.shape)

# print(df.isnull().sum())
#
# print(df.columns)

# print(df['latitude'])

# print(df[['latitude', 'population']])

# print(df[(df['housingMedianAge'] < 20) & (df['housingMedianAge'] > 10)][['totalRooms', 'housingMedianAgex`']])

# print(df['population'].max())
# print(df['population'].min())
# print(df['population'].mean())
# print(df['population'].sum())

# print(df.describe())