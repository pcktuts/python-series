# Threading 
import time
import threading 
def print_hello(users):
    print("printing hello user")
    for user in users:
        time.sleep(1)
        print("Hello " + user)

def print_hi(users):
    print("printing hi user")
    for user in users:
        time.sleep(1)
        print("Hi " + user)
users = ["Kevin", "Peter", "Arjun", "Mohan"]
start_time = time.time()

thread1 = threading.Thread(target=print_hello, args=(users,))
thread2 = threading.Thread(target=print_hi, args=(users,))

thread1.start()
thread2.start()
# print_hello(users)
# print_hi(users)

thread1.join()
thread2.join()
print("Total time taken", time.time()- start_time)

# main.py -> task1 print_hello() -> task2 print_hi() -> end

# main.py
# task1 --------------- 4second #task2----------------4 second --- 8.444
# main.py
    # task1 ------------------ 4 second
    # task2 ------------------ 4 second
    # 4.454545
