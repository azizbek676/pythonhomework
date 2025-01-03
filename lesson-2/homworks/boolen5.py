def check_same_length(str1, str2):
    if len(str1) == len(str2):
        return "Both strings have the same length."
    else:
        return "The strings do not have the same length."
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = check_same_length(str1, str2)
print(result)