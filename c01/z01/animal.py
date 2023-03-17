import random

from z01.gender import Gender


class Animal:

    def __init__(self, genus, gender=Gender.FEMALE):
        self.isAlive = True
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        if self.gender == Gender.FEMALE and partner.gender == Gender.MALE and self.genus == partner.genus:
            return Animal(self.genus, Gender.MALE if random.randint(1, 10) > 5 else Gender.FEMALE)
        else:
            raise Exception("Attribute not found")

    def __str__(self):
        return f'Is alive: {self.isAlive}\n' \
               f'Gender: {self.gender}\n' \
               f'Genus: {self.genus}'
