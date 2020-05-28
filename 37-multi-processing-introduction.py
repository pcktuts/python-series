# Multi Processing 
import time
import multiprocessing 
print_data = []
def print_hello(users):
    global print_data
    print("printing hello user")
    for user in users:
        time.sleep(1)
        print("Hello " + user)
        print_data.append("Hello " + user)
    print(print_data)
def print_hi(users):
    print("printing hi user")
    for user in users:
        time.sleep(1)
        print("Hi " + user)
users = ["Kevin", "Peter", "Arjun", "Mohan"]
start_time = time.time()

process1 = multiprocessing.Process(target=print_hello, args=(users,))
process2 = multiprocessing.Process(target=print_hi, args=(users,))

process1.start()
process2.start()
# print_hello(users)
# print_hi(users)

process1.join()
process2.join()
print(print_data)
print("Total time taken", time.time()- start_time)

