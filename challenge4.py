def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero is not possible."
num1 = float(input("enter 1st number"))
num2 = float(input("enter 2nd number"))
result = divide_numbers(num1, num2)
print(result)
