# Pythonda OYP - Konstruktor, class və nüsxə dəyişənlər(class and instance variables)



class Person:
    leg_count = 2                       # class variable
    def __init__(self, ad, soy_ad):
        self.name = ad                  # instance variables
        self.surname = soy_ad           # .


    def get_email(self):
        email = f"{self.name}_{self.surname}@myservice.com"
        return email.lower()



    




anar = Person("Anar", 'Mammadli')
arzu = Person("Arzu", "Haciyeva")

print(f"Leg count for Anar: {anar.leg_count}")
print(f"Leg count for Arzu: {arzu.leg_count}")

# print(Person.leg_count)
print(Person.name)
