list1=[10,20,30,40]
list1[1]=200
print(list1)

fru=["apple","orange","grapes","kiwi"]
fru.append("mango")
print(fru)

fru.insert(1,"watermelon")
print(fru)

print (len(fru))

print (fru.index("apple"))
print(fru)

fru.remove("orange")
print(fru)

fru.pop(1)
print (fru)

del fru[1]
print (fru)
fru.clear()
print(fru)