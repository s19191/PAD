list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = lambda x: x ** 2

cube = lambda x: x ** 3

print('Square or cube? Type 2 for square, 3 for cube.')
input = int(input())

if input == 2:
    for e in list:
        print(square(e))
elif input == 3:
    for e in list:
        print(cube(e))
