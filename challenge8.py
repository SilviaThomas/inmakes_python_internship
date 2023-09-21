def discount(price):
    stud_discount = 0.10
    discount_price = price * (1 - stud_discount)
    return discount_price
def add_discount(price):
    ad_discount= 0.05
    discount_price = price * (1 - ad_discount)
    return discount_price
price = int(input("Enter the price:"))
studis = discount(price)
final = add_discount(studis)
print("discounted price:",final)
