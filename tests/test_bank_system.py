import unittest
from src.bank_system import Customer, BankAccount

class TestBankSystem(unittest.TestCase):

    def test_customer_creation(self):
        customer = Customer("John Doe", "01/01/1990", "12345678901", "123 Main St - Downtown - City/State")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.cpf, "12345678901")

    def test_bank_account_creation(self):
        customer = Customer("Jane Doe", "02/02/1985", "09876543210", "456 Oak St - Uptown - City/State")
        account = BankAccount(customer)
        self.assertEqual(account.customer, customer)
        self.assertEqual(account.agency, '0001')

    def test_deposit(self):
        customer = Customer("John Doe", "01/01/1990", "12345678901", "123 Main St - Downtown - City/State")
        account = BankAccount(customer)
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        customer = Customer("John Doe", "01/01/1990", "12345678901", "123 Main St - Downtown - City/State")
        account = BankAccount(customer)
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

if __name__ == '__main__':
    unittest.main()
import unittest
from src.bank_system import Customer, BankAccount

class TestBankSystem(unittest.TestCase):

    def test_customer_creation(self):
        customer = Customer("John Doe", "01/01/1990", "12345678901", "123 Main St - Downtown - City/State")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.cpf, "12345678901")

    def test_bank_account_creation(self):
        customer = Customer("Jane Doe", "02/02/1985", "09876543210", "456 Oak St - Uptown - City/State")
        account = BankAccount(customer)
        self.assertEqual(account.customer, customer)
        self.assertEqual(account.agency, '0001')

    def test_deposit(self):
        customer = Customer("John Doe", "01/01/1990", "12345678901", "123 Main St - Downtown - City/State")
        account = BankAccount(customer)
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        customer = Customer("John Doe", "01/01/1990", "12345678901", "123 Main St - Downtown - City/State")
        account = BankAccount(customer)
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

if __name__ == '__main__':
    unittest.main()
