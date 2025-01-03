def check_positive_and_even(number):
    if number > 0 and number % 2 == 0:
        return "The number is positive and even."
    else:
        return "The number is not positive and even."
number = int(input("Enter a number: "))
result = check_positive_and_even(number)
print(result)