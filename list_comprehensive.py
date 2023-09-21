# result=[i for i in "inmakes"]
# print(result)


#to print a nest list with words starting with 'p'
# result=["python","django","people","flask"]
# new=[]
# for i in result:
#     if 'p' in i:
#         new.append(i)
# print(new)

#using comprehensive
result=["python","django","people","flask"]
new=[i for i in result if 'p' in i]
print(new)

new=[i for i in range(10)]
print(new)

new=["inmakes" for i in result]
print(new)

new=[i.upper() for i in result]
print(new)

num=[1,2,3,4]
new=[i*i for i in num]
print(new)

