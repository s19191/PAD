# import pandas as pd
import numpy as np

# file = np.genfromtxt('PAD_03.csv',
#                      dtype=[('ID', float),
#                             ('Country', "U10"),
#                             ('owns_car', float),
#                             ('owns_TV', float),
#                             ('owns_house', float),
#                             ('owns_Phone', float),
#                             ('gender', "U10"),
#                             ('Age', float)],
#                      # names='a, b, c, d, e, f, g, h',
#                      encoding='UTF-8',
#                      delimiter=';',
#                      # missing_values={0: -1, 1: "", 2: 0.0, 3: -1, 4: -1, 5: -1, 6: '--', 7: -1},
#                      # filling_values={0: np.NaN, 1: None, 2: np.NaN, 3: np.NaN, 4: np.NaN, 5: np.NaN, 6: 'H', 7: np.NaN},
#                      # missing_values={1: str(), 6: 'M'},
#                      # filling_values={1: None, 6: 'H'},
#                      usemask=True,
#                      skip_header=1,
#                      )

file = np.genfromtxt('PAD_03.csv', delimiter=';', usemask=True, dtype=None, encoding="utf-8", names=True)
# print(file)
np.ma.masked_print_option.set_display('None')
print(file.mask)
# file.data[]
print(file.dtype)
for line in file:
    print(line)


emptyRows = []
for line in range(file.size):
    for col in range(8):
        if file.mask[line][col]:
            emptyRows.append(file.data[line][0])
print(emptyRows)

data = file.data
countries = np.unique(data['Country'])
country_avgs = []
country_mins = []
for country in countries:
    country_avg = round(np.mean(data[data['Country'] == country]['owns_car']), 2)
    country_min = round(np.min(data[data['Country'] == country]['Age']), 2)
    country_avgs.append(country_avg)
    country_mins.append(country_min)
array = np.core.records.fromarrays([countries, country_avgs, country_mins], names='Country, OwnedGoodsAvg, MinAge')
print(array)

np.savetxt('newFile.csv', array, delimiter='  ', header='string', comments='', fmt='%s')
