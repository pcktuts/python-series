# Python file handling - Write a file
# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist

# X mode
# f = open("myfile-new.txt", "x")
# f.write("Some contents")
# f.close()
# a - append mode
# f = open("myfile-new.txt", "a")
# f.write("Some more content")
# f.close()
# w - Write mode
try :
  f = open("myfile-for-writing.txt", "w")
  f.write("new content for writing")
except:
  print("Failed")
finally:
  f.close()
