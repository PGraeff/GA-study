import numpy as np

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vectorobj = [x, y, z]    


    # function to add vectors (acording to GA-Analitica)
    def add(self, other):
        self.addedvector = []
        for i, t in self.vectorobj, other:
            elem =  t * i
            self.addedvector.append(elem)
        return self.addedvector


a = Vector(2, 3, 4)
b = Vector(7, 6, 5)