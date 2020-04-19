# Console Student application
# 1. Add, 2. Show, 3. Delete
print("======= Welcome to Student application =======")
def accept_input():    
    print("1. Add \n2. Show \n3. Delete")
    operation = int(input("Please select the operation you want to perform: "))
    if operation == 1:
        print("Please enter student details")
        name = input("Please enter student name: ")
        roll_number = input("Please enter student roll number: ")
        mark = input("Please enter student mark: ")
        print(name, roll_number, mark)
    more = input("Do you want to do more operations y/n?")
    if more == 'y':
        accept_input()
    else:
        print("Student Application has exited")    
accept_input()
