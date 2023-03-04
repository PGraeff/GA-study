import numpy as np

class Vector():
    def __init__(self, x, y, z):
        self.vectorobj = [x, y, z]    

    # function to add vectors (acording to GA-Analitica)
    def scalar_product(self, other):
        self.otherobj = [other]
        self.addedvector = np.dot(self.vectorobj, other)
        return self.addedvector

    #checks for linear dependencies between the vectors, if 
    # there are more than two vectors, then it expects a list containing two vectors
    def linear_dependecy(self, others):
        self.others = others    
        if len(others) > 1:
            self.others = others
            vector_dict = {i :vector for i, vector in zip(len(others), others)}

        # for vector in self.others:
        


        pass 
    
    # multiply two vectors 
    def vector_multiplication(self, other):
        pass    

    # gets the norm of the vector
    def get_norm(self): 
        pass


a = Vector(2, 3, 4)
b = Vector(7, 6, 5)
# print(a.vectorobj.shape())