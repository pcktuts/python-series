# Scope
# variable/function 
x = 10 # global scope
print(x)
def say_hi():
    y = "hi" # functional scope
    global z 
    z = "Value of z"
    print(x)
say_hi()
print(z)

def func_a():
    print("inside func a")
    def inner_func():
        print("inner func")
    inner_func()
func_a()
inner_func()
