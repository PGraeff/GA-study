import numpy as np

class Vector():
    def __init__(self, x, y, z):
        self.vectorobj = [x, y, z]    


    # function to add vectors (acording to GA-Analitica)
    def scalar_product(self, other):
        self.otherobj = [other]
        self.addedvector = np.dot(self.vectorobj, other)
        return self.addedvector
    
    



a = Vector(2, 3, 4)
b = Vector(7, 6, 5)
