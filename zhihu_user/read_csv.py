import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

file = pd.read_csv('zhihu_user.csv')
print(file)
print(file.columns)
print(file[:3])