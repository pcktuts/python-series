# Object oriented Programming 
# Inheritance
class Person:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
	def print_name(self):
		print("First name is", self.fname, "Lastname is ", self.lname)

class Student(Person):
	def __init__(self, fname, lname, age):
		super().__init__(fname, lname)
		self.age = age
	def display_age(self):
		print(self.age)
s = Student("Joseph", "Peter", 25)
s.print_name()
s.display_age()
