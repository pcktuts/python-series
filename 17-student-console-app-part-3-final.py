# Console Student application
# 1. Add, 2. Show, 3. Delete
student_data = []
def add_to_student_data(name, roll_number, mark):
    student_data.append(
        {
            "name": name,
            "roll_number": roll_number,
            "mark": mark
        }
    )
def show_student_data():
    print("Sno\tName\tRollNo\tMark")
    for x,y in enumerate(student_data):
        print(str(x + 1) + "\t" + y["name"] + "\t" + y["roll_number"] + "\t" + y["mark"])
 
print("======= Welcome to Student application =======")
def accept_input():    
    print("1. Add \n2. Show \n3. Delete")
    operation = int(input("Please select the operation you want to perform: "))
    if operation == 1:
        print("Please enter student details")
        name = input("Please enter student name: ")
        roll_number = input("Please enter student roll number: ")
        mark = input("Please enter student mark: ")
        add_to_student_data(name, roll_number, mark)
        # print(student_data)
    elif operation == 2:
        show_student_data()
    elif operation == 3:
        print("Select the item you want to delete")
        show_student_data()
        item_to_delete = input("Enter the Sno to delete: ")
        del student_data[int(item_to_delete) - 1]
        show_student_data()
        print("Item has been deleted")

    more = input("Do you want to do more operations y/n?")
    

    if more == 'y':
        accept_input()
    else:
        print("Student Application has exited")    
accept_input()
