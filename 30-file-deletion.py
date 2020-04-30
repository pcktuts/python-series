# Python file handling - Delete a file/dir
import os, shutil
# file deletion
# if os.path.exists("file.txt") is True:
#   os.remove("file.txt") or os.unlink()
# else:
#   print("File doesnt exists")

#os.rmdir('myfolder') # can remove only empty dir

try:
  shutil.rmtree("myfolder")
except:
  print("Remove failed")
