from account import *

class Test:

    def setup_method(self):
        self.acc1 = Account('Emily')

    def teardown_method(self):
        del self.acc1

    def test_init(self):
        assert self.acc1.get_name() == 'Emily'
        assert self.acc1.get_balance() == 0

    def test_deposit(self):
        #amount <= 0
        assert self.acc1.deposit(0) == False
        assert self.acc1.deposit(0.0) == False
        assert self.acc1.deposit(-10) == False
        assert self.acc1.deposit(-10.5) == False

        #amount > 0
        assert self.acc1.deposit(10) == True
        assert self.acc1.deposit(100.5) == True

    def test_withdraw(self):
        #amount <= 0
        assert self.acc1.withdraw(0) == False
        assert self.acc1.withdraw(0.0) == False #float
        assert self.acc1.withdraw(-10) == False
        assert self.acc1.withdraw(-10.5) == False #float

        #not enough in balance
        assert self.acc1.withdraw(10) == False
        assert self.acc1.withdraw(100.5) == False #float
        assert self.acc1.deposit(10) == True
        assert self.acc1.withdraw(100) == False

        #enough in balance
        assert self.acc1.deposit(10) == True
        assert self.acc1.withdraw(10) == True


    def test_get_balance(self):
        self.acc1.deposit(10)
        assert self.acc1.get_balance() == 10

        self.acc1.withdraw(10)
        assert self.acc1.get_balance() == 0

    def test_get_name(self):
        assert self.acc1.get_name() == 'Emily'

