import numpy as np
import pandas as pd

task2 = np.genfromtxt('Task_2.csv', delimiter=';')
for line in task2:
    print(line)

task3 = pd.read_csv('Task_3.csv', sep=';')
print(task3)

df2 = pd.DataFrame(task3.groupby(['Date', 'DoctorID', 'Type', 'City'], as_index=False).first())