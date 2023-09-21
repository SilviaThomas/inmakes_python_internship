def calculate_final_price(price_x, price_y):
    final_price = price_x / (price_y ** 2)
    return final_price

# Input prices of X and Y from the user
price_x = float(input("Enter the price of X: "))
price_y = float(input("Enter the price of Y: "))

# Calculate the final price using the function
result = calculate_final_price(price_x, price_y)

# Display the result
print("Final Price (FP):", result)
