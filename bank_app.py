
import json

class InsufficientBalanceError(Exception):
    """Jab balance se zyada paise nikalne ki koshish ho."""
    pass


class BankAccount():

    def __init__(self , owner , balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount sahi nahi hai")
    
        self.balance = self.balance + amount


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount sahi nahi hai")
        if  amount > self.balance:
            raise InsufficientBalanceError("balance kam hai")
        self.balance = self.balance - amount

    def __str__(self):
        return f"{self.owner}: Rs {self.balance}"

def save_account(acc , filename):
    data = {
        "owner" : acc.owner,
        "balance": acc.balance 
    }

    with open (filename , "w") as file:
        json.dump(data , file)

    print("account successfully saved")

def load_account(filename):
    try:

        with open(filename,"r") as file:
            data = json.load(file)

        acc = BankAccount(
            data["owner"],
            data["balance"]
        )

        return acc 
    except FileNotFoundError:
        print("file nahi hai")

        return None


def main():
    acc = load_account("account.json")
    if acc is None:
        name = input("apna naam likho: ",)
        acc = BankAccount(name , 0)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance dekho")
        print("4. Save aur Exit")
        choice = input("Option chuno: ")
        if choice == "1":
            try:
                amount = float(input("amount: "))
                acc.deposit(amount)
                print("deposite")
            except ValueError:
                print("amount sahi nahi hai")

        elif choice == "2":
            try:
                amount = float(input("amount: "))
                acc.withdraw(amount)
                print("withdrwa succesfull")
            except InsufficientBalanceError:
                print("pese nahi hai")
            except ValueError:
                print("amount sahi daloo")
        elif choice == "3":
            print(acc)
        elif choice == "4":
            save_account(acc , "account.json")
            break
        else:
            print("Galat option")

main()
