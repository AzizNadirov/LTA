# property





class Person:
    def __init__(self, name, surname, by):
        self.name = name
        self.sname = surname
        self.birth_year = by
        self.__email = f"{self.name}_{self.sname}@gmail.com".lower()
        self.__age = 2023 - int(self.birth_year)



    @property               # getter
    def email(self):
        print('getting email..')
        return self.__email
    


    @email.setter
    def email(self, value):
       print('setting email..')
       self.__email = value 






    @property
    def age(self):                              # getter of age
        return 2023 - int(self.birth_year)
    


    @age.setter                                 # setter of age
    def age(self, v):
        self.__age = v



    @age.deleter                                    # deleter
    def age(self):
        a = input("Are you sure that you want to delete ??")
        if a == 'y':
            del self.__age
        else:
            print("Cancelled!")
    



class Student(Person):
    def __init__(self, name, surname, birth_year, uni, fac, gp):
        super().__init__(name, surname, birth_year)
        self.ini = uni
        self.faculity = fac
        self.group = gp



    def create_email(self):
        return f"{self.name}_{self.sname}@edu.com".lower()




p = Person('Anar', 'Qubadli', 2000)
p.name = 'Veli'


p.email                          # getting

p.email = 'aaaa@gmail.com'      # setting



print(p.age)
del p.age

# self.age ---> self.__age
