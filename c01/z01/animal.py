import random


class Animal:

    def __init__(self, genus, gender="Female"):
        self.isAlive = True
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        if self.gender == "Female" and partner.gender == "Male" and self.genus == partner.genus:
            return Animal(self.genus, "Male" if random.randint(1, 10) > 5 else "Female")
        else:
            raise Exception("Attribute not found")

    def __str__(self):
        return f'Is alive: {self.isAlive}\n' \
               f'Gender: {self.gender}\n' \
               f'Genus: {self.genus}'
