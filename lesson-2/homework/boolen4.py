def check_all_different(num1, num2, num3):
    if num1 != num2 and num1 != num3 and num2 != num3:
        return "All numbers are different."
    else:
        return "Not all numbers are different."
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
result = check_all_different(num1, num2, num3)
print(result)