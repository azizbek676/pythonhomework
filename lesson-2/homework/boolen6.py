def check_divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Son 3ga ham 5ga ham bo'linadi."
    else:
        return   "Son 3ga ham 5ga ham bo'linmaydi."
number = int(input("Raqmni yozing:"))
result = check_divisible_by_3_and_5(number)
print(result)