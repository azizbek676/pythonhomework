user_string = input("Matinni yozing: ")
contains_digits = any(char.isdigit() for char in user_string)
if contains_digits:
    print("Raqam bor.")
else:
    print("Raqam yo'q.")