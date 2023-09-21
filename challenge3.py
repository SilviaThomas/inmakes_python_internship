def calculate_final_price(x, y):
    final_price = x / y ** 2
    return final_price
price_x = float(input("Enter the price of X: "))
price_y = float(input("Enter the price of Y: "))
result = calculate_final_price(price_x, price_y)
print("Final_price:", result)
