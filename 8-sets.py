#Sets
# unorderd
set1 = {"a", "b", "c"}

set1.add("d")
set1.update(["e", "f", "g"])
set1.discard("a")
set2 = {"aa", "bb", "c"}
set3 = set1 | set2
set4 = set1 & set2

print(set4)
