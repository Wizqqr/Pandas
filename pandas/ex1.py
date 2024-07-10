# УПР 1
# Step 1.Прочесть с помощью pandas csv файл
# Step 2.Посмореть сколько в нем столбцов и строк
# Step 3.Определить какой тип данных имеют столбцы
import pandas as pd

# Step 1.
df = pd.read_csv('../california_housing_train.csv')

print(df.head())

# Step 2.
print(df.shape)
# Step 3.
print(df.dtypes)