class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_specs(self):
        return "Brand: " + self.brand + ", Model: " + self.model

    def display_specs(self):
        print(self.get_specs())
class Car(Vehicle):
    def __init__(self, brand, model, num_wheels):
        super().__init__(brand, model)
        self.num_wheels = num_wheels

    def get_specs(self):
        return "Car: " + super().get_specs() + ", Wheels: " + str(self.num_wheels)

#
class Bike(Vehicle):
    def __init__(self, brand, model, mark):
        super().__init__(brand, model)
        self.mark = mark

    def get_specs(self):
        return "Bike: " + super().get_specs() + ", Mark: " + self.mark
car_brand = input("Enter Car Brand: ")
car_model = input("Enter Car Model: ")
car_wheels = int(input("Enter Number of Car Wheels: "))
my_car = Car(car_brand, car_model, car_wheels)

bike_brand = input("Enter Bike Brand: ")
bike_model = input("Enter Bike Model: ")
bike_mark = input("Enter Bike Mark: ")
my_bike = Bike(bike_brand, bike_model, bike_mark)

print("\nCar Specifications:")
print("Vehicle Brand:", my_car.brand)
print("Vehicle Model:", my_car.model)
my_car.display_specs()

print("\nBike Specifications:")
print("Vehicle Brand:", my_bike.brand)
print("Vehicle Model:", my_bike.model)
my_bike.display_specs()
