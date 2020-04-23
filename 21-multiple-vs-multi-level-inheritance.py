# Object oriented Programming 
# Multiple Inheritance vs Multi Level inheritance
# multiple inheritance
# class A:
# 	def hi(self):
# 		print("hi from class A")
# class B:
# 	def hi(self):
# 		print("Hello from class B")

# class C(B,A):
# 	pass 
# c_object = C()
# c_object.hi()

# Multi level inheritance
class A:
	def hello(self):
		print("hi from class A")
class B(A):
	def hi(self):
		print("Hello from class B")

class C(B):
	pass 
c_object = C()
c_object.hello()
c_object.hi()
