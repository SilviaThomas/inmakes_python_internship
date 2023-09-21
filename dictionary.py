a={"char":500,"table":300,12:"python"}
print(a)

print(a["char"])

print(len(a))

a["veg"]=120
print(a)

a.update({12:"django"})
print(a)

for i in a:
    print(i)#print only keys

for i in a.values():
    print(i)#pprint only values
for i in a.items():
     print(i)#print key and values