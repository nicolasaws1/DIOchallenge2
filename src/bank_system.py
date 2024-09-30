import datetime
import re

# Class to represent a customer
class Customer:
    def __init__(self, name, birth_date, cpf, address):
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
        self.address = address

# List of registered customers
customers = []

# List of registered bank accounts
accounts = []
account_number_sequential = 1  # Sequential account number counter

# Check if CPF already exists
def cpf_exists(cpf):
    """Check if a CPF is already registered in the customer list."""
    for customer in customers:
        if customer.cpf == cpf:
            return True
    return False

# CPF validation
def validate_cpf(cpf):
    """Check if the CPF consists of 11 digits and no duplicates."""
    if not re.fullmatch(r'\d{11}', cpf):
        print("Error: CPF must contain 11 digits.")
        return False
    return True

# Date validation
def validate_date(date_str):
    """Validate the date format (dd/mm/yyyy)."""
    try:
        datetime.datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        print("Error: Invalid date. The correct format is dd/mm/yyyy.")
        return False

# Class to represent a bank account
class BankAccount:
    def __init__(self, customer, agency='0001'):
        global account_number_sequential
        self.customer = customer
        self.agency = agency
        self.account_number = account_number_sequential
        account_number_sequential += 1
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount, /):
        """Perform a deposit and add a transaction to the statement."""
        if amount > 0:
            self.balance += amount
            transaction = {'type': 'Deposit', 'amount': amount, 'timestamp': datetime.datetime.utcnow()}
            self.transactions.append(transaction)
            print(f"Deposit of ${amount:.2f} successfully made!")
        else:
            print("Error: Invalid amount for deposit.")

    def withdraw(self, amount):
        """Perform a withdrawal if there is sufficient balance."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            transaction = {'type': 'Withdrawal', 'amount': amount, 'timestamp': datetime.datetime.utcnow()}
            self.transactions.append(transaction)
            print(f"Withdrawal of ${amount:.2f} successfully made!")
        else:
            print("Error: Insufficient balance or invalid amount.")

    def show_statement(self, /, *, detailed=False):
        """Display the account statement, with an option for detailed view."""
        if detailed:
            print("\nDetailed Statement:")
        else:
            print("\nSimple Statement:")

        if self.transactions:
            for transaction in self.transactions:
                timestamp = transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S UTC')
                print(f"{timestamp} - {transaction['type']}: ${transaction['amount']:.2f}")
        else:
            print("No transactions performed.")
        print(f"Current balance: ${self.balance:.2f}\n")

# Function to register a new customer
def register_customer():
    """Register a new customer, validating CPF and data."""
    name = input("Enter the customer's name: ")
    birth_date = input("Enter the birth date (dd/mm/yyyy): ")

    if not validate_date(birth_date):
        return None

    cpf = input("Enter the CPF (numbers only): ")
    if not validate_cpf(cpf) or cpf_exists(cpf):
        print("Error: This CPF is already registered or the CPF is invalid.")
        return None
    
    address = input("Enter the address (format: street, number - neighborhood - city/state): ")

    customer = Customer(name, birth_date, cpf, address)
    customers.append(customer)
    print(f"Customer {customer.name} successfully registered!")
    return customer

# Function to register a bank account
def register_account(customer):
    """Create a new bank account for an existing customer."""
    account = BankAccount(customer)
    accounts.append(account)
    print(f"Account {account.account_number} of agency {account.agency} successfully created for customer {customer.name}!")
    return account

# Function to list registered customers
def list_customers():
    """Display all registered customers."""
    if not customers:
        print("No customers registered.")
    else:
        print("\nRegistered customers:")
        for i, customer in enumerate(customers, 1):
            print(f"{i}. {customer.name} - CPF: {customer.cpf}")

# Function to select a customer
def select_customer():
    """Allow the user to select a customer by index."""
    list_customers()
    if customers:
        try:
            index = int(input("Select the customer number: ")) - 1
            if 0 <= index < len(customers):
                return customers[index]
            else:
                print("Error: Customer not found.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
    return None

# Function to list registered accounts of a customer
def list_accounts(customer):
    """Display the accounts registered for a customer."""
    customer_accounts = [account for account in accounts if account.customer == customer]
    if customer_accounts:
        print(f"\nAccounts of {customer.name}:")
        for account in customer_accounts:
            print(f"Account {account.account_number} - Agency {account.agency} - Balance: ${account.balance:.2f}")
        return customer_accounts
    else:
        print(f"{customer.name} has no registered accounts.")
        return []

# Main function of the bank menu
def menu():
    customer = None
    account = None

    while True:
        print("\n=== Bank Menu ===")
        print("1. Register Customer")
        print("2. Register Bank Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Show Statement")
        print("6. List Customers")
        print("7. Exit")
        option = input("Choose an option: ")

        if option == '1':
            customer = register_customer()

        elif option == '2':
            customer = select_customer()
            if customer:
                register_account(customer)

        elif option == '3':
            customer = select_customer()
            if customer:
                customer_accounts = list_accounts(customer)
                if customer_accounts:
                    account = customer_accounts[0]  # Select the first account of the customer
                    amount = float(input("Enter the amount to deposit: $"))
                    account.deposit(amount)

        elif option == '4':
            customer = select_customer()
            if customer:
                customer_accounts = list_accounts(customer)
                if customer_accounts:
                    account = customer_accounts[0]  # Select the first account of the customer
                    amount = float(input("Enter the amount to withdraw: $"))
                    account.withdraw(amount)

        elif option == '5':
            customer = select_customer()
            if customer:
                customer_accounts = list_accounts(customer)
                if customer_accounts:
                    account = customer_accounts[0]  # Select the first account of the customer
                    detailed = input("Do you want to see the detailed statement? (y/n): ").lower() == 'y'
                    account.show_statement(detailed=detailed)

        elif option == '6':
            list_customers()

        elif option == '7':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
