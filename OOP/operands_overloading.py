class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
# here it is overriding the in built __str__ method and by that instead of returning the objects
    def __str__(self):
        return f'{self.name} :{self.balance}'

    def __add__(self,other):
        return Account('combined',self.balance+other.balance)

    def __gt__(self, other):
        return self.balance > other.balance

user1=Account('vamshi',10000)
user2=Account('nani',2000)


# here we cant add two objects but by overriding the __add__ method it behaves different
combined=user1+user2
print(user1)
print(user2)
print(combined)

# here based on the operands passed in balances it behaves different
if user1 > user2:
    print('Vamshi pays')
else:
    print('nani pays')
    