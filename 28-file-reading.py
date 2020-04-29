# Python file handling - Reading a file
try:
  f = open("myfile.txt", "r")
  print(f.read(5))
  # print(f.readline())
  # print(f.readline())
  # for line in f:
  #   print(line)
except:
  print("File reading failed")
finally:
  f.close()
