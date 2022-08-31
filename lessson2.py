# this program contains a class of Cars, its attributes and methods !!!!!!
class Cars():
    
    def __init__ (self, make, model, color, mileage, price):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage
        self.price = price 

    def drive(self, distance):
        self.mileage = self.mileage + distance 

    def paint(self, color):
        self.color = color

    def name(self):
        return '{} {}'.format(self.make, self.model)

    def increase_price(self, value):
        self.price = self.price + value

    def sell(self):
        return 'This car is for sale'



# inputting different Cars their make, model,color, mileage and price !!!!!
first_car = Cars(make='Toyota', model='Camry 2010', color='black', mileage= 0, price=4500000)
# second_car = Cars(make='Hyundai', model='2020 SUV', color='blue', mileage='0', price=3500000)
# third_car = Cars(make='Honda', model='2003 civic', color='grey', mileage='0', price=5000000)
# fourth_car = Cars(make='Dodge', model='2016 Charger', color='red', mileage='0', price=10600000)
# fifth_car = Cars(make='Ford', model='Edge 2022', color='white', mileage='0', price='25000000)

first_car.drive(50)
first_car.paint('Red')
first_car.increase_price(1000000)


print(first_car.sell())
print(first_car.name())
print(first_car.make)
print(first_car.model)
print(first_car.color)
print(first_car.mileage)
print(first_car.price)

