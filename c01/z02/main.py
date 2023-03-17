import datetime

from worker import Worker

myList = [
    Worker(1, "Adam", 1983, 1500),
    Worker(2, "Anna", 1981, 1700),
    Worker(3, "Błażej", 1990, 1800),
    Worker(4, "Beata", 1992, 1600),
    Worker(5, "Czesław", 1980, 2000),
    Worker(6, "Cecylia", 1983, 2100),
    Worker(7, "Daniel", 1976, 1900)
]


def avgSal(workers):
    sal = 0
    companySize = len(workers)

    for worker in workers:
        sal += worker.salary

    print(f'AVG sal: {sal / companySize}')


def avgSalWithAge(workers, age):
    salYounger = 0
    counterYounger = 0
    salOlder = 0
    counterOlder = 0

    for worker in workers:
        if datetime.datetime.now().year - worker.age[0] < age:
            salYounger += worker.salary
            counterYounger += 1
        else:
            salOlder += worker.salary
            counterOlder += 1
    print(f'Workers younger than {age} years old AVG salary: { 0 if salYounger == 0 or counterYounger == 0 else salYounger / counterYounger}\n'
          f'Workers older (or equal) than {age} years old AVG salary: { 0 if salOlder == 0 or counterOlder == 0 else salOlder / counterOlder}')


avgSal(myList)
avgSalWithAge(myList, 30)
