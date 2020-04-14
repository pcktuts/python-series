#Tuples
# Tuples are immutable
x = ("a", "b", "c") 
y = list(x)
y[0] = 12
x = tuple(y)

print(x)
if "b" in x:
    print("B exists in tuple")
# del x
print(x)

tup = ("a",)
print(type(tup))

tupe2 = ("b", "c")
print( tup + tupe2 )
