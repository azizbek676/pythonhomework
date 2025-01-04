def check_credentials(username, password):
    if username and password:
        return "Ikkalasi ham kiritilgan."
    else:
        return "Isim yoki kod kiritilmagan."
username = input("Foydalanuuvchi nomini kiriting: ")
password = input("Parolni kiriting: ")
result = check_credentials(username, password)
print(result)
