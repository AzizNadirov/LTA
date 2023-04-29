# magic/dunder methods




class Vector:
    def __init__(self, data):
        self.data = data
        self.len = len(data)

    
    def add(self, v2):
        if not len(self.data) == len(v2.data):
            raise ValueError('Length dissmatch...')
        else:
            res = []
            for i in range(len(self.data)):
                res.append(self.data[i] + v2.data[i])

            vector_result = Vector(res)
            return vector_result
        

    def subtract(self, v2):
        if not len(self.data) == len(v2.data):
            raise ValueError('Length dissmatch...')
        else:
            res = []
            for i in range(len(self.data)):
                res.append(self.data[i] - v2.data[i])

            vector_result = Vector(res)
            return vector_result
        
    # magic methods

    def __eq__(self, other_value):
        print("is equal works...")
        if isinstance(other_value, Vector):
            return self.data == other_value.data
        

    def __neg__(self):
        print("Neating...")
        res = []
        for i in self.data:
            res.append(-i)
        return Vector(res)



    def __add__(self, other):
        print("adding..")
        res = []
        if isinstance(other, Vector):
            for i in range(len(self.data)):
                res.append(self.data[i] + v2.data[i])

            vector_result = Vector(res)
            return vector_result
        
        elif isinstance(other, (int, float)):
            res = []
            for i in self.data:
                res.append(i+other)

            return Vector(res)



    def __sub__(self, other):
        print("subtracting..")
        res = []
        if isinstance(other, Vector):
            for i in range(len(self.data)):
                res.append(self.data[i] - v2.data[i])

            vector_result = Vector(res)
            return vector_result
        


    def __pow__(self, other):
        print("Powing...")
        res = []
        if isinstance(other, (int, float)):
            for i in self.data:
                res.append(i ** other)
            return Vector(res)
        



    def __radd__(self, other):
        print("adding..")
        res = []
        if isinstance(other, Vector):
            for i in range(len(self.data)):
                res.append(self.data[i] + v2.data[i])

            vector_result = Vector(res)
            return vector_result
        
        elif isinstance(other, (int, float)):
            res = []
            for i in self.data:
                res.append(i+other)

            return Vector(res)
        


    def __len__(self):
        return len(self.data)


        
        


    def __str__(self):
        return f"Vector: {self.data}"
    


v = Vector([4,16,100])
v2 = Vector([1,2,3,4,4,4,4,4,4])


print(len(v2))
