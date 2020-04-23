# Object oriented Programming 
# Encapsulation 
class Person:
	def __init__(self):
		self.__age = 22
	def age(self):
		print("Age is: ", self.__age)
	def setAge(self, age):
		self.__age = age 

p = Person()
p.age()
p.__age = 25
p.age()
p.setAge(25)
p.age()
