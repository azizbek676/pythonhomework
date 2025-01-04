def check_sum_greater_than_50_8(num1, num2):
    if num1 + num2 > 50.8:
        return "The sum of the two numbers is greater than 50.8."
    else:
        return "The sum of the two numbers is not greater than 50.8."
        
def check_number_between_10_and_20(number):
    if 10 <= number <= 20:
        return "The number is between 10 and 20 (inclusive)."
    else:
        return "The number is not between 10 and 20 (inclusive)."
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result_sum = check_sum_greater_than_50_8(num1, num2)
print(result_sum)
number = float(input("Enter a number: "))
result_range = check_number_between_10_and_20(number)
print(result_range)