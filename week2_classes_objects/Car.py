# Car Class Example
class Car:
    def __init__(self, make, model, year, mileage, original_price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.original_price = original_price
        
    def current_value(self, current_year):
        return self.original_price * (.90 ** (current_year - self.year))
        
        
andys_car = Car("Toyota", "Sequoia", 2001, 275000, 45000)

print("andys_car value:", andys_car.current_value(2023))

# AntiqueCar Class Example
class AntiqueCar(Car):
    def current_value(self, current_year):
        return self.original_price * (1.03 ** (current_year - self.year))
        
        
gregs_car = AntiqueCar("Cadillac", "DeVille", 1976, 100000, 18000)

print("gregs_car value: ", gregs_car.current_value(2023))

#Polymorphism

johnnys_car = Car("Ford", "F150", 2015, 55000, 45000)
jennys_car = Car("Toyota", "Rav1", 2006, 125000, 20000)

car_lot = [andys_car, johnnys_car, jennys_car, gregs_car]

total_value = 0.0

for car in car_lot:
    total_value += car.current_value(2023)
    print(type(car))
    
print("all cars value: ", total_value)

