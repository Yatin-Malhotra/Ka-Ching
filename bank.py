import time
from block import Block
from blockchain import Blockchain
from wallet import Wallet

class Bank:
    def __init__(self, storage_file):
        self.blockchain = Blockchain()
        self.wallet = Wallet(storage_file)
        self.wallet.load_from_storage()  # Load accounts from storage during initialization

    def create_account(self, account_number, initial_balance=0):
        self.wallet.create_account(account_number, initial_balance)

    def deposit(self, account_number, amount):
        if self.is_valid_account(account_number) and amount > 0:
            self.wallet.deposit(account_number, amount)
            self.add_transaction("Deposit", account_number, amount)

    def withdraw(self, account_number, amount, tag=None):
        if self.is_valid_account(account_number) and amount > 0 and self.wallet.get_balance(account_number) >= amount:
            self.wallet.withdraw(account_number, amount)
            self.add_transaction("Withdrawal", account_number, amount, tag=tag)

    def transfer(self, sender_account, receiver_account, amount, tag=None):
        if self.is_valid_account(sender_account) and self.is_valid_account(receiver_account) and amount > 0 and self.wallet.get_balance(sender_account) >= amount:
            self.wallet.transfer(sender_account, receiver_account, amount, tag)

    def lend(self, lender_account, borrower_account, amount, interest_rate, tag=None):
        if self.is_valid_account(lender_account) and self.is_valid_account(borrower_account) and amount > 0 and self.wallet.get_balance(lender_account) >= amount:
            self.wallet.lend(lender_account, borrower_account, amount, interest_rate, tag)

    def is_valid_account(self, account_number):
        if self.wallet.get_balance(account_number) is not None:
            return True
        else:
            print("Invalid account number.")
            return False

    def add_transaction(self, transaction_type, account_number, amount, receiver_account=None, tag=None, interest_rate=None):
        if self.is_valid_account(account_number):
            transaction_data = {"type": transaction_type, "account_number": account_number, "amount": amount, "tag": tag}
            if receiver_account:
                if not self.is_valid_account(receiver_account):
                    return
                transaction_data["receiver_account"] = receiver_account
            if interest_rate:
                transaction_data["interest_rate"] = interest_rate
            new_block = Block(len(self.blockchain.chain), time.time(), transaction_data, self.blockchain.get_latest_block().hash)
            self.blockchain.add_block(new_block)

    def get_balance(self, account_number):
        if self.is_valid_account(account_number):
            return self.wallet.get_balance(account_number)

    def print_transactions(self):
        for block in self.blockchain.chain:
            print(f"Block #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("--------------")
