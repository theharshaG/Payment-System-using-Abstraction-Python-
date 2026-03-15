from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card")


class Wallet(Payment):

    def __init__(self, balance):
        self.__balance = balance

    def pay(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Paid", amount, "from Wallet")
            print("Remaining balance:", self.__balance)

        else:
            print("Insufficient Wallet Balance")


print("Select Payment Method")
print("1 UPI")
print("2 Card")
print("3 Wallet")

choice = input("Enter choice: ")

amount = int(input("Enter amount: "))


if choice == "1":
    p = UPI()

elif choice == "2":
    p = Card()

elif choice == "3":
    p = Wallet(1000)

else:
    print("Invalid option")
    exit()

p.pay(amount)
