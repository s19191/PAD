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

task3 = pd.read_csv('Task_3.csv', delimiter=";", usecols=['DateTime', 'DoctorID', 'Type', 'City'])
task3['DateTime'] = pd.to_datetime(task3['DateTime'])
task3['Date'] = pd.to_datetime(task3['DateTime'].dt.date)

groupedTask3 = pd.DataFrame(task3.groupby(['Date', 'DoctorID', 'Type', 'City'], as_index=False).first())

groupedTask3['HowLong'] = task3.groupby(['Date', 'DoctorID', 'Type', 'City'], as_index=False).count()['DateTime']
groupedTask3['HowLong'] = pd.to_timedelta(groupedTask3['HowLong'], unit='m')
groupedTask3['hour'] = groupedTask3['DateTime'] + groupedTask3['HowLong']
groupedTask3['hour'] = groupedTask3['hour'].dt.time
groupedTask3['DateTime'] = groupedTask3['DateTime'].astype(str) + ' - ' + groupedTask3['hour'].astype(str)
groupedTask3 = groupedTask3.iloc[:, :-2]

groupedTask3.to_csv('Task_3_output.csv', index=False)

print('Doctors availability')
print(groupedTask3)
