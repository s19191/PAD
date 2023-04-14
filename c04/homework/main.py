import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

task2 = np.genfromtxt('Task_2.csv', delimiter=';')

print('Eigenvectors, and eigenvalues for the matrix')
print(np.linalg.eig(task2))
print(np.linalg.eigvals(task2))
print('The inverse of the matrix')
print(np.linalg.inv(task2))

df = pd.read_csv('Task_3.csv', delimiter=";")
df = df.iloc[:, :-4]
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date'] = pd.to_datetime(df['DateTime'].dt.date)
print(df)
df2 = pd.DataFrame(df.groupby(['Date', 'DoctorID', 'Type', 'City'], as_index=False).first())

print(df2)

df2 = df2.iloc[:, 1:]
df2['HowLong'] = df.groupby(['Date', 'DoctorID', 'Type', 'City'], as_index=False).count()['DateTime']
df2['HowLong'] = pd.to_timedelta(df2['HowLong'], unit='m')
df2['hour'] = df2['DateTime'] + df2['HowLong']
df2['hour'] = df2['hour'].dt.time
df2['DateTime'] = df2['DateTime'].astype(str) + ' - ' + df2['hour'].astype(str)
df2 = df2.iloc[:, :-2]
col = df2.pop('DateTime')
df2.insert(0, col.name, col)
df2.to_csv('out.csv', index=False)
# print(df2)

