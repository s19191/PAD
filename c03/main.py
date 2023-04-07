import pandas as pd

file = pd.read_csv('PAD_03.csv', sep=';')
print(file)

empty = file.isna().any(axis=1)
ids = file[empty]['ID'].to_numpy()
print(ids)

owns_cols = file.filter(like='owns')
file['owned_goods'] = owns_cols.sum(axis=1)
print(file)

avg_by_gender = file.groupby('gender')['owned_goods'].mean().round(2)
print(avg_by_gender)

avg_by_country = file.groupby('Country')["owned_goods"].mean()
min_age = file.groupby('Country')['Age'].min()
new_dataFrame = pd.DataFrame({'Country': avg_by_country.index, 'AvgOwnedGoods': avg_by_country, 'MinAge': min_age})
print(new_dataFrame)

file.to_csv('newFile.csv', index=False)
