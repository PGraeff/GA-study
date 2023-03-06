import numpy as np

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

    #checks for linear dependencies between the vectors, if 
    # there are more than two vectors, then it expects a list containing two vectors
    def linear_dependecy(self, others):
        self.others = others    
        if len(others) > 1:
            self.vector_dict = {i :vector for i, vector in zip((len(others)), others)}

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

print(a.add(b.vectorobj))