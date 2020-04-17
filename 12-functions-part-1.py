# Functions
def full_name(fname, lname):
    full_name = fname + " " + lname
    return full_name
full_name = full_name("Joseph", "Thomas")
print(full_name)
# Function without arguments
def test_func():
    x = "Hi"
    return x

print(test_func())
# N number of arguments
def n_args(*args):
    print(args[3])

n_args("a", "b", "c", "d")
# Named arguements
def hi(hi, hello):
    print(hi + " " + hello)

hi(hi="Hi", hello= "Hello world")
