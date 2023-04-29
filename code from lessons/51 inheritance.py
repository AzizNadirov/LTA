# inheraitance - vərəsəlik

class Person:
    def __init__(self, name, surname, by):
        self.name = name
        self.sname = surname
        self.birth_year = by

    def get_age(self):
        current_year = 2023
        return current_year - int(self.birth_year)
    

    def create_email(self):
        return f"{self.name.lower()}_{self.sname}@gmail.com"
    



class Student(Person):
    def __init__(self, name, surname, birth_year, uni, fac, gp):
        super().__init__(name, surname, birth_year)
        self.ini = uni
        self.faculity = fac
        self.group = gp



    def create_email(self):
        return f"{self.name.lower()}_{self.sname}@edu.com"




p = Person('Anar', 'Qubadli', 2000)

s = Student('Anar', 'Qubadli', 2000, 'azi', 'cs', '101')


print(p.create_email())

print(s.get_age())

