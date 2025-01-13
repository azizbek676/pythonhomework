def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b) 
    return wrapper
@check
def div(a, b):
    return a / b
numerator = float(input("Please enter the numerator (the first number): "))
denominator = float(input("Please enter the denominator (the second number): "))
result = div(numerator, denominator)
print(f"Result: {result}")
