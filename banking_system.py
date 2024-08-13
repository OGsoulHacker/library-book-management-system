# Initialize the banking system with a dictionary to store account details
#We start with an empty dictionary called banking_system . This dictionary will store account
#details where the keys are account numbers and the values are dictionaries containing account
#holder information and balance.
banking_system = {}

# Function to create a new account
#function checks if the account number already exists in the banking_system dictionary. If it
#does, it prints an error message. If not, it creates a new entry in the dictionary with the account
#holder's name and an initial balance of 0.
def create_account(account_number, account_holder):
    if account_number in banking_system:
        print("Account number already exists.")
    else:
        banking_system[account_number] = {
            'account_holder': account_holder,
            'balance': 0
        }
        print(f"Account for {account_holder} created successfully.")

# Function to deposit money into an account
#function checks if the account number exists. If it does, it adds the deposit amount to the
#current balance and prints the new balance. If the account number is not found, it prints an error message.
def deposit(account_number, amount):
    if account_number in banking_system:
        banking_system[account_number]['balance'] += amount
        print(f"Deposited {amount} to account {account_number}. New balance: {banking_system[account_number]['balance']}")
    else:
        print("Account number not found.")

# Function to withdraw money from an account
#function checks if the account number exists and if there is sufficient balance for the
#withdrawal. If both conditions are met, it deducts the amount from the balance and prints the new
#balance. If there is insufficient balance or the account number is not found, it prints an error message.
def withdraw(account_number, amount):
    if account_number in banking_system:
        if banking_system[account_number]['balance'] >= amount:
            banking_system[account_number]['balance'] -= amount
            print(f"Withdrew {amount} from account {account_number}. New balance: {banking_system[account_number]['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Account number not found.")

# Function to check the balance of an account
#This function checks if the account number exists and prints the current balance. If the account
#number is not found, it prints an error message.
def check_balance(account_number):
    if account_number in banking_system:
        print(f"Account {account_number} balance: {banking_system[account_number]['balance']}")
    else:
        print("Account number not found.")

# Testing the banking system
create_account('12345', 'John Doe')
deposit('12345', 500)
withdraw('12345', 200)
check_balance('12345')