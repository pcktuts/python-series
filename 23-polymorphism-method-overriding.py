# Object oriented Programming 
# Polymorphism - Having multiple forms

# Operator

a = 10
b = 20
print( a + b) # arthimatic sum
a = "Hello"
b = "World"
print( a + b ) # string concatenation 

# Functions 
x = "Hello" # len() - no of characters in string
y = [1, 2, 3, 4 ,5 ,6, 7] # len() - no of items in the list
z = {"a":1, "b": 2, "c": 3} # len() - no of keys in the dict
print(len(x), len(y), len(z))

# Class
class India:
	def speak(self):
		print("Generally most people speak Hindi but some do not")
class Kerala(India):
	pass
	# def speak(self):
	# 	print("We speak malayalam")

class Tamilnadu(India):
	def speak(self):
		print("We speak tamil")

kerala = Kerala()
kerala.speak()
tamil = Tamilnadu()
tamil.speak()
# function overriding
