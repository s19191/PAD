import math


class Cylinder:

    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius

    def get_surface_area(self):
        return (self.radius ** 2 * math.pi) * 2 + self.height * 2 * math.pi * self.radius

    def get_volume(self):
        return (self.radius ** 2 * math.pi) * self.height
