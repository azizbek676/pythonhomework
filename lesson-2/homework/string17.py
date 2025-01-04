user_string = input("Iltimos matnni kiriting: ")
vowels = "aeiouAEIOU"
modified_string = ''.join('*' if char in vowels else char for char in user_string)
print("Matndagi unlilar '*'ga alishtirildi:", modified_string)