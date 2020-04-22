# Object oriented Programming introduction
class Car: 
  # Constructor
  def __init__(self, fuel, color, company):
    self.fuel = fuel # Every car has a fuel system
    self.color = color # Every car has a color
    self.company = company # every car has a make
    print("constructor created")
  def display_car_info(self):
    print ('This is a', self.color, self.company, self.fuel, 'car')

# Car a is petrol
# Car a is red in color
# Car a is made By Mahindra
car_a = Car('Petrol','Red', 'Mahindra') 
car_a.display_car_info() # Methods
car_b = Car('Petrol','Green', 'Maruthi') 
car_b.display_car_info() # Methods
print(car_b.fuel)
