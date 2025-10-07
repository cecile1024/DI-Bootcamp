class Person():
    def __init__(self,name, age):
        # print("A new person has been initialize!")
        # print(f"This person is {name} and is {age} years old.")
        self.name=name
        self.age=age
    def show_details(self):
        print("Hello my name is " + self.name)

first_person=Person("Cecile",47)
first_person.show_details()
second_person=Person("My_futur_lover","any age")

print(first_person.age)

##########################Manque la fonction INIT
# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()

# Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")

class BankAccount:
#trouver un moyen de mettre un message d'erreur si le numerode compte n'est pas donné
    def __init__(self, account_number=0, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

my_account=BankAccount()
my_account_two=BankAccount()
print(my_account.account_number)
print(my_account_two.account_number)
my_account.balance=20000
my_account.deposit(3000)
my_account.view_transactions()