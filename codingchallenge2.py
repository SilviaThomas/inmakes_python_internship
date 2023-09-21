def simple_interest(p,n,r):
    s_interest=(p*n*r)/100
    return s_interest
p = int(input("enter the amount:"))
n = int(input("enter the no of years:"))
r = int(input("enter the rate of interest:"))
interest = simple_interest(p,n,r)
print("simple interest is:",interest)
