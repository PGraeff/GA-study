import numpy as np
import math as mt

class Vector():
    def __init__(self, x, y, z):
        self.vectorobj = [x, y, z]    

    # Vector addition, returns a new vector that is the some of the object and an external vector
    def add(self, others):
        self.other = [others]
        self.vector_dict = {i :vector for i, vector in zip(range(len(self.other)), self.other)}
        for vector in self.vector_dict.values():
            self.added_vector = [(elem1 + elem2) for elem1, elem2 in zip(vector, self.vectorobj)]
        return self.added_vector

    # function to add vectors (acording to GA-Analitica)
    def scalar_product(self, other):
        self.otherobj = [other]
        self.scalar_value = np.dot(self.vectorobj, other)
        return self.scalar_value
 
    # gets the norm of the vector
    def get_norm(self): 
        self.temp = []
        for element in self.vectorobj:
            self.temp.append(element ** 2)
        self.norm = mt.sqrt(sum(self.temp))
        return  self.norm


a = Vector(2, 3, 4)
b = Vector(7, 6, 5)

print(a.add(b.vectorobj))
print(a.get_norm())