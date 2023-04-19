"""
Create a class called BankAccount that has the following attributes:

account_number: A string representing the account number.
balance: A float representing the account balance.
The class should have the following methods:

deposit(amount): A method that accepts a float amount and adds it to the account balance.
withdraw(amount): A method that accepts a float amount and subtracts it from the account balance.
get_balance(): A method that returns the current account balance.

"""
class BankAccount():

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def get_acc(self):
        return self.account_number

    def get_balance(self):
        return self.balance


def main():
    account1 = BankAccount("1234567890", 1000.00)
    account2 = BankAccount("0987654321", 500.00)

    account1.deposit(500.00)
    account1.withdraw(200.00)

    account2.deposit(1000.00)
    account2.withdraw(250.00)

    print(f"{account1.get_acc()}: {account1.get_balance()}") # Expected output: 1300.00
    print(f"{account2.get_acc()}: {account2.get_balance()}") # Expected output: 1250.00

main()