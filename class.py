# RESEARCH THE CONCEPTS:

# 1) SNAKECASE is a stlye of writing in which each case space is replaced by an underscore character, and the first ltter of each word is written in lowercase. it is a commonly used naming convention in computing, for example, variables and filenames carry the snakecase.
# 2) CAMEL CASE is the practice of writing phrases without spaces or punctuations. it indicates the separation of words with a single capitalized letter, and the first word stratingg with either case.
# 3) PASCALCASE this is similar to camelCase, except the first letter in PascalCase is always capitalized.



# 2) using the structure we explained during the course of the week's sessions 
#create a BankAccount class

class BankAccount:

    def __init__(self, name, number, balance = 0):
        self.name = name
        self.number = number
        self.balance = balance 
        print('Hello!!! Welcome to ABD Bank')

    def fullname(self):
        return '{} {}'.format(self.name, self.number) 

    def deposit(self, amount):
        self.balance += amount
        print('\nYou deposited', amount)

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print('\nYou withdrew:', amount)
        else:
            print('\nInsufficient balance')
    def availableBalance(self):
        print('\nAvailable balance:', self.balance)

cus_1 = BankAccount('Tina uyateide', number=2958763412)
cus_2 = BankAccount('Mary James', number=2967845623)

print(cus_1.fullname())
cus_1.deposit(50000)
cus_1.withdraw(60000)
cus_1.availableBalance()
