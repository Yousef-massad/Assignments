class User:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def make_deposits(self,amount):
        self.balance+=amount

    def make_withdrawal(self,amount):
        self.balance-=amount

    def transfer_money(self, other_user, amount):
        self.balance-=amount
        other_user.balance+=amount

    def display_user_balance(self):
        print(f"{self.name}, Balance:{self.balance}")   



first_user = User("Guido van Rossum",150)
second_user =User("yousef", 1000)
third_user = User("Bashar",1)

first_user.display_user_balance()
first_user.make_deposits(30)
first_user.make_deposits(20)
first_user.make_deposits(10)
first_user.display_user_balance()
first_user.make_withdrawal(10)
first_user.display_user_balance()


second_user.display_user_balance()
second_user.make_deposits(150)
second_user.make_deposits(200)
second_user.display_user_balance()
second_user.make_withdrawal(100)
second_user.make_withdrawal(100)
second_user.display_user_balance()



third_user.display_user_balance()
third_user.make_deposits(150)
third_user.display_user_balance()
third_user.make_withdrawal(100)
third_user.make_withdrawal(100)
third_user.make_withdrawal(100)
third_user.display_user_balance()



first_user.transfer_money(third_user,50)
first_user.display_user_balance()
third_user.display_user_balance()