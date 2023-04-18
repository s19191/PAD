import pandas as pd

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

orders = pd.read_csv('orders.csv', delimiter=",")

print('Describe')
print(orders.describe())
print('Info')
print(orders.info())
print('Head')
print(orders.head())

orders['order_date'] = pd.to_datetime(orders['order_date'], format='%Y/%m/%d')
print('Check of data type')
print(orders.info())

print('Size of tshirt_category')
print(orders['tshirt_category'].size)
print('Unique values of tshirt_category')
print(orders['tshirt_category'].unique())

orders['tshirt_category'] = orders['tshirt_category'].apply(lambda x: x.replace('Wh ', 'White '))
orders['tshirt_category'] = orders['tshirt_category'].apply(lambda x: x.replace('Bl ', 'Black '))
orders['tshirt_category'] = orders['tshirt_category'].apply(lambda x: x.replace('Tshirt ', 'T-Shirt '))

print('Unique values of tshirt_category after standardization')
print(orders['tshirt_category'].unique())


def extract_tshirt_type(type_):
    for i in type_:
        if i in ['T-Shirt', 'Hoodie', 'Tennis Shirt']:
            return i
    return 'No data'


def extract_tshirt_size(size_):
    for i in size_:
        if i in ['M', 'F']:
            return i
    return 'No data'


def extract_tshirt_colour(colour_):
    for i in colour_:
        if i in ['White', 'Black']:
            return i
    return 'No data'


orders['tshirt_type'] = orders['tshirt_category'].str.split().apply(lambda x: extract_tshirt_type(x))
orders['tshirt_size'] = orders['tshirt_category'].str.split().apply(lambda x: extract_tshirt_size(x))
orders['tshirt_colour'] = orders['tshirt_category'].str.split().apply(lambda x: extract_tshirt_colour(x))
orders.drop('tshirt_category', inplace=True, axis=1)
print('After extraction of data from tshirt_category')
print(orders.info())
print(orders['tshirt_type'].unique())
print(orders['tshirt_size'].unique())
print(orders['tshirt_colour'].unique())

print('Dates between 31.12.2014 and 02.08.2016')
print(orders[orders.order_date.between('2014-12-31', '2016-08-02')])

# ******************************************* Homework *******************************************

customers = pd.read_csv('customers.csv', delimiter=",")

print('Whole dataframe of customers.csv')
print(customers)

print('Comparison of customers and orders')
print("customers ", customers.shape, "orders ", orders.shape)

customers.rename(columns={'customerID': 'customer_id'}, inplace=True)
print('After rename of column')
print(customers.info())

result = pd.merge(customers, orders, on='customer_id', how='inner')
# Metoda merge
# Typ inner join
# Zignorowani zostaną kliencie bez zamówień oraz oraz w dróga stronę, czyli zamówień bez klienta

result.to_csv('connectedFrames.csv', index=False)
