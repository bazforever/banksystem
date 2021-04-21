
class User:
    def __init__(self, firstName, lastName,  age, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
    def showContacts(self):
        print("** Personnal Information **")
        print("First name:", self.firstName)
        print("Last name:", self.lastName)
        print("Age:", self.age)
        print("Gender:", self.gender)

class Bank(User):
    def __init__(self, firstName, lastName, age, gender, balance):

        super().__init__(firstName, lastName, age, gender)
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated: $", self.balance)
    def withdraw(self, amount):
        self.amount = amount
        if self.amount >self.balance:
             print("Insuficient funds | balance available $:", self.balance)
        else:
             self.balance = self.balance - self.amount
             print("Account balance has been update to : $", self.balance)
    def view_balance(self):
        self.showContacts()
        print("Account balance  $:", self.balance)

julian = Bank("Julian", "Charleroi", 32, "male", 1000)
print(julian.showContacts())
print(julian.deposit(500))









