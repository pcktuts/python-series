# Dict
# unorderd, changable
mydict = { "name": "rahul", "age": 24, "gender": "male"}
mydict["age"] = 29
print(mydict.get("age"))

for x in mydict:
    print(x)

for x in mydict:
    print(mydict[x])

# To print key and value
for x, y in mydict.items():
    print(x , y)

mydict.pop("age")
print(mydict)
