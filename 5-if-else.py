mark = 80
pass_mark = 35
# this is mark checking
# another comment
if mark > pass_mark:
    print("Passed")
    if mark > 80:
        print("You have distinction")
    else:
        pass
elif mark == 35 :
    print("You just passed")
else:
    print("Faild")
print("i'm out side if")
