import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head()