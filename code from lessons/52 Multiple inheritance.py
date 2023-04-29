# çox vərəsəlilik - multiple inheritance


class Vehicle:
    can_do = 'moving'
    def __init__(self, fueltype, capacity, passenger_count, max_speed, year):
        self.fueltype = fueltype
        self.capacity = capacity
        self.passenger_count = passenger_count
        self.max_speed = max_speed
        self.year = year


    def get_age(self):
        return 2023 - int(self.year)



class Car(Vehicle):
    can_do = 'drivng'
    def __init__(self, fueltype, capacity, passenger_count, max_speed, year, body_type):
        super().__init__(fueltype, capacity, passenger_count, max_speed, year)
        self.body_type = body_type




class Boat:
    # can_do = 'sailing'
    def __init__(self, has_sail):
        self.body_type = has_sail



class SuperBoat(Boat, Vehicle):
    # can_do = 'super sailing'
    def __init__(self, has_sail, fueltype, capacity, passenger_count, max_speed, year, model):
        Boat.__init__(self, has_sail)
        Vehicle.__init__(self, fueltype, capacity, passenger_count, max_speed, year)
        self.model = model



sq = SuperBoat(has_sail=True, fueltype='elect', capacity=5000, passenger_count=10, max_speed=180, year=2020, model='megaboat')

print(sq.get_age())







