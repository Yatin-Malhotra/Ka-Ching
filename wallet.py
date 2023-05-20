import json

class Wallet:
    def __init__(self, storage_file):
        self.accounts = {}
        self.storage_file = storage_file

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            self.save_to_storage()  # Save accounts to storage after creation

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts and amount > 0:
            self.accounts[account_number] += amount
            self.save_to_storage()  # Save accounts to storage after deposit

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and amount > 0 and self.accounts[account_number] >= amount:
            self.accounts[account_number] -= amount
            self.save_to_storage()  # Save accounts to storage after withdrawal

    def transfer(self, sender_account, receiver_account, amount, tag=None):
        if sender_account in self.accounts and receiver_account in self.accounts and amount > 0 and self.accounts[sender_account] >= amount:
            self.accounts[sender_account] -= amount
            self.accounts[receiver_account] += amount
            self.save_to_storage()  # Save accounts to storage after transfer

    def lend(self, lender_account, borrower_account, amount, interest_rate, tag=None):
        if lender_account in self.accounts and borrower_account in self.accounts and amount > 0 and self.accounts[lender_account] >= amount:
            self.accounts[lender_account] -= amount
            self.accounts[borrower_account] += amount
            self.save_to_storage()  # Save accounts to storage after lending

    def save_to_storage(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.accounts, f)

    def load_from_storage(self):
        try:
            with open(self.storage_file, "r") as f:
                self.accounts = json.load(f)
        except FileNotFoundError:
            self.accounts = {}
