class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(balance = 0, intrest_rate= 0.02)

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def make_deposit(self, amount):
        self.account.deposite(amount)
        return self
    
    def display_user_blance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

    def transfer_money(self, reciever, amount):
        self.account.balance -= amount
        reciever.account.balance += amount
        print(f"You have sent an amount of ${amount}")
        print(f"Your balance is: ${self.account.balance}, reciever balance is: ${reciever.account.balance}")
        return self


class BankAccount:
    def __init__(self, balance, intrest_rate ):
        self.balance = balance
        self.intrest_rate = intrest_rate
        self.amount = 0

    def deposite(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.intrest_rate
        return self

sajeda = User("Sajeda Salim")
sajeda.make_deposit(100).make_deposit(50).make_withdrawal(30).display_user_blance()