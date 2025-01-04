def check_numbers_equal(num1, num2):
    if num1 == num2:
        return "Sonlar teng."
    else:
        return "Sonlar teng emas."
num1 = float(input("Birinchi raqamni kiriting: "))
num2 = float(input("Ikkinchi raqamni kiritng: "))
result = check_numbers_equal(num1, num2)
print(result)