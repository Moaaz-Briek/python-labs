class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def __str__(self):
        return f"Engine: {self.fuel_type} FT, {self.horsepower} HP"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def __str__(self):
        return f"Car: {self.make} {self.model}, {self.engine}"

engine = Engine(fuel_type="petrol", horsepower=150)
car = Car(make="Toyota", model="Corolla", engine=engine)
print(car)
