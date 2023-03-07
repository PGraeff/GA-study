import numpy as np
import math as mt

class Vector():
    def __init__(self, vector):
        self.vectorobj = vector   

    # this function performs vector addition, returns a new vector that is the some of the object and an external vector
    def add(self, others):
        self.other = [others]
        self.vector_dict = {i :vector for i, vector in zip(range(len(self.other)), self.other)}
        for vector in self.vector_dict.values():
            self.added_vector = [(elem1 + elem2) for elem1, elem2 in zip(vector, self.vectorobj)]
        return self.added_vector
 
    # this function gets the norm of the vector
    def get_norm(self): 
        self.temp = []
        for element in self.vectorobj:
            self.temp.append(element ** 2)
        self.norm = mt.sqrt(sum(self.temp))
        return  self.norm


    # this function gets the scalar product between two vectors (acording to GA-Analitica)
    # you can use either two vectors or the norms of both and the cosine between them list must be [norm of external object, cosine]
    def scalar_product(self, other):
        if isinstance(other, Vector):
            self.scalar_value = np.dot(self.vectorobj, other.vectorobj)
        elif isinstance(other, list):
            self.norm1 = self.get_norm()
            self.norm2 = other[0]
            self.cosine = other[1]
            self.scalar_value = self.norm1 * self.norm2 * self.cosine
        return self.scalar_value
    
    # this function gets the cosine of the angle of two vectors
    def get_cosine(self, other):
        
        self.scalar = self.scalar_product(other)
        self.norm1 = self.get_norm()
        self.norm2 = other.get_norm()
        self.theta_cosine = self.scalar / (self.norm1 * self.norm2) 
        return self.theta_cosine     

a = Vector([2, 3, 4])
b = Vector([7, 6, 5])

b_norm_cosine = [b.get_norm(), b.get_cosine(a)]

print(a.add(b.vectorobj))
print(a.get_norm())
print(a.get_cosine(b))

print(a.scalar_product(b_norm_cosine))
