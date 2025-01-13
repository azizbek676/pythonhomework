def check_password():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password is too short.")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")

if __name__ == "__main__":
    check_password()