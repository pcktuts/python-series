# Functions
# 1. Arbitrary Keyword Arguments (kwargs)
# 2. Default param value
# 3. Pass lists as function arguments
# 4. `pass` on functions
#1. kwargs
def my_func(**args):
    full_name = args["fname"] + " " + args["lname"]
    return full_name
full_name = my_func(fname="Rahul", lname="VR")
full_name1 = my_func(fname="Peter", lname="VR")
# print(full_name1)
# print(full_name)
# 2. Default param value
def person_info(name, age = 18):
    person = name + " " + str(age)
    return person
# print(person_info(name="Joseph"))
# print(person_info(name="Navin", age= 25))
# 3. Pass lists as function arguments
mylist = ["a", "b", "c"]
def my_list_func(mylist):
    for x in mylist:
        print(x)
# my_list_func(mylist)
#4. Pass
def pass_test():
    pass
