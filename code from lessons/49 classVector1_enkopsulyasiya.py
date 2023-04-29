# getter - get
# setter - set



class Vector:
    def __init__(self, data):
        self.__data = data
        self.len = len(data)

    
    def add(self, v2):
        if isinstance(v2, Vector):
            if not len(self.__data) == len(v2.__data):
                raise ValueError('Length dissmatch...')
            else:
                res = []
                for i in range(len(self.__data)):
                    res.append(self.__data[i] + v2.__data[i])

                vector_result = Vector(res)
                return vector_result
        elif isinstance(v2, (int, float)):
            res = [] 
            for i in self.__data:
               res.append(i + v2)

            v = Vector(res)
            return v




    def subtract(self, v2):
        if isinstance(v2, Vector):
            if not len(self.__data) == len(v2.__data):
                raise ValueError('Length dissmatch...')
            else:
                res = []
                for i in range(len(self.__data)):
                    res.append(self.__data[i] - v2.__data[i])

                vector_result = Vector(res)
                return vector_result
            
        elif isinstance(v2, (int, float)):
            res = [] 
            for i in self.__data:
               res.append(i - v2)

            v = Vector(res)
            return v
        

    def get_data(self):
        return self.__data.copy()
    

    def set_data(self, data2):
        self.__data = data2
        self.len = len(data2)

        

    def __str__(self):
        return f"Vector: {self.__data}"






v = Vector([1,2,3])
v2 = Vector([1,1,1])


v3 = v.add(v2)

print(v3)



len()



