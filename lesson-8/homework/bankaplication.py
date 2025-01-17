import os
import random

class Account:
    def __init__(self, account_number, name, initial_deposit=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds for this withdrawal.")

    def view_account(self):
        """View account details."""
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def generate_account_number(self):
        """Generate a unique account number."""
        return random.randint(1000, 9999)

    def create_account(self, name, initial_deposit=0):
        """Create a new bank account."""
        account_number = self.generate_account_number()
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        print(f"Account created! Account Number: {account_number}")
        self.save_to_file()

    def view_account(self, account_number):
        """View account details."""
        account = self.accounts.get(account_number)
        if account:
            print(account.view_account())
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        """Deposit money into an account."""
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from an account."""
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        """Save all account details to a file."""
        with open('accounts.txt', 'w') as f:
            for account in self.accounts.values():
                f.write(f"{account.account_number},{account.name},{account.balance}\n")

    def load_from_file(self):
        """Load account details from a file."""
        if os.path.exists('accounts.txt'):
            with open('accounts.txt', 'r') as f:
                for line in f:
                    account_number, name, balance = line.strip().split(',')
                    self.accounts[int(account_number)] = Account(int(account_number), name, float(balance))
        else:
            print("No previous account data found. Starting fresh.")
def display_menu():
    print("\nWelcome to the Bank Application")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

def run_bank_app():
    bank = Bank()

    while True:
        display_menu()
        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(name, initial_deposit)

        elif choice == '2':
            account_number = int(input("Enter account number to view: "))
            bank.view_account(account_number)

        elif choice == '3':
            account_number = int(input("Enter account number to deposit into: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == '4':
            account_number = int(input("Enter account number to withdraw from: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == '5':
            print("Thank you for using the Bank Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    run_bank_app()
