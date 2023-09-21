# Function 1: Student Discount (10% off)
def apply_student_discount(price):
    discount = 0.10
    discounted_price = price * (1 - discount)
    return discounted_price
def apply_regular_buyer_discount(price):
    discount = 0.05  # 5% discount
    discounted_price = price * (1 - discount)
    return discounted_price
def apply_both_discounts(price):
    price_after_student_discount = apply_student_discount(price)

    # Then apply the additional discount for regular buyers
    price_after_both_discounts = apply_regular_buyer_discount(price_after_student_discount)

    return price_after_both_discounts
original_price = float(input("Enter the original price of the product: "))
final_discounted_price = apply_both_discounts(original_price)

print(f"The final discounted price is: ${final_discounted_price:.2f}")

