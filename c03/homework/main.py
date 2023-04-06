import pandas as pd
import numpy as np

file = np.genfromtxt('PAD_03.csv',
                     dtype=[('ID', float), ('Country', 'U1'), ('owns_car', float), ('owns_TV', float), ('owns_house', float), ('owns_Phone', float), ('gender', 'U1'), ('Age', float)],
                     # names='a, b, c, d, e, f, g, h',
                     encoding=None,
                     delimiter=';',
                     # missing_values={0: -1, 1: "", 2: -1, 3: -1, 4: -1, 5: -1, 6: '', 7: -1},
                     # filling_values={0: np.NaN, 1: None, 2: np.NaN, 3: np.NaN, 4: np.NaN, 5: np.NaN, 6: None, 7: np.NaN},
                     skip_header=1
                     )
# print(file)
print(file.dtype)
for line in file:
    print(line)

