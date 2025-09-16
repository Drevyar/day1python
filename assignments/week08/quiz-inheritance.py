""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f'Vehicle : {self.brand}, {self.model}, {self.year}'
    
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year,)
        self.number_of_doors = number_of_doors
    
    def get_info(self):
        return f'Car : {self.brand}, {self.model}, {self.year}, {self.number_of_doors}'

v1 = Vehicle('Benz', 'c220d', 2025)
print(v1.get_info())

c1 = Car('Civic', 'fk', 2025, 4)
print(c1.get_info())