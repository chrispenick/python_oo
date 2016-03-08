class Account:
    def __init__(self, acct_num, balance):
        self._acct_num = acct_num
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        output = 'Account: {0} Balance: {1:.2f}'.format(self._acct_num
                                                        ,self.balance)
        return output
     
    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance

class Savings(Account):
    def __init__(self, acct_num, rate, balance = 100):
        super().__init__(acct_num, balance)
        self._rate = rate

    def add_interest(self):
        self._balance *= (1 + self._rate)
        
class Checking(Account):
    def __init__(self, acct_num, balance = 0):
        super().__init__(acct_num, balance)


        

        
