from cat import Cat
from dog import Dog

dogM = Dog("Male")
dogF = Dog()

print(dogM.woof())

catM = Cat("Male")
catF = Cat()

print(catM.purr())

newDog = dogF.breed(dogM)
print(newDog)

newCat = catF.breed(catM)
print(newCat)

newHybrid = dogF.breed(catM)
