import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

task2 = np.genfromtxt('Task_2.csv', delimiter=';')

print('Eigenvectors, and eigenvalues for the matrix')
print(np.linalg.eig(task2))
print('The inverse of the matrix')
print(np.linalg.inv(task2))

task3 = pd.read_csv('Task_3.csv', sep=';')

df2 = task3.groupby('DateTime')['DoctorID'].mean()
# df2.sort_values('DateTime')

print(df2)
