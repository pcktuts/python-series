# Date and time in python
# 1970 jan 12AM - Unix epoch time
import time, datetime, calendar 
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))  

# sleep time
for i in range(0, 10):
    print(i)
    time.sleep(0)

print(datetime.datetime.now())
print(datetime.datetime(2020, 12, 10))

# calendar
cal = calendar.month(2020, 12)
print(cal)
calendar.prcal(2020)
