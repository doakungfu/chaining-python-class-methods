

from typing import ChainMap


class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

# For this assignment, we'll add some functionality to the User class:
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
guido.make_withdrawal(150)
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
print(guido.account_balance)
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance



# CHAINed below




# Create a file with the User class, including the __init__ and make_deposit methods
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
    	self.account_balance += amount
        return self
# Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
# Add a display_user_balance method to the User class
    def display_user_balance(self):
       print("User: {}, Balance: ${}".format(self.name, self.account_balance))
       return self
# BONUS: Add a transfer_money method
    def make_transfer(self, other_user, amount):
        other_user.make_deposit(amount) # could also say other_user.account_balance += amount, like I first did, but this is way better!
        self.make_withdrawal(amount) # could also say self.account_balance -= amount
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
knight = User("The Black Knight", "justascratch@python.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
guido.make_deposit(1000).make_deposit(200).make_deposit(50).make_withdrawal(75).display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
monty.make_deposit(500).make_withdrawal(30).make_withdrawal(60).make_withdrawal(90).display_user_balance()

# Have the third user make 1 deposit and 3 withdrawals and then display their balance
knight.make_deposit(30).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).display_user_balance()

# BONUS: With transfer_money method; have the first user transfer money to the third user and then print both users' balances
guido.make_transfer(knight,420).display_user_balance()
knight.display_user_balance()

