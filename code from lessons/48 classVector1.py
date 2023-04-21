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
        


    def __str__(self):
        return f"Vector: {self.data}"






v = Vector([1,2,3])
v2 = Vector([1,1,1])


v3 = v.subtract(v2)
print(v3.len)



