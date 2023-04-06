# import pandas as pd
import numpy as np

file = np.genfromtxt('PAD_03.csv',
                     dtype=[('ID', float),
                            ('Country', "U10"),
                            ('owns_car', float),
                            ('owns_TV', float),
                            ('owns_house', float),
                            ('owns_Phone', float),
                            ('gender', "U10"),
                            ('Age', float)],
                     # names='a, b, c, d, e, f, g, h',
                     encoding='UTF-8',
                     delimiter=';',
                     # missing_values={0: -1, 1: "", 2: 0.0, 3: -1, 4: -1, 5: -1, 6: '--', 7: -1},
                     # filling_values={0: np.NaN, 1: None, 2: np.NaN, 3: np.NaN, 4: np.NaN, 5: np.NaN, 6: 'H', 7: np.NaN},
                     # missing_values={1: str(), 6: 'M'},
                     # filling_values={1: None, 6: 'H'},
                     usemask=True,
                     skip_header=1,

                     )
# print(file)
np.ma.masked_print_option.set_display('None')
print(file.mask)
file.data[]
# print(file.dtype)
for line in file:
    print(line)

