from bank import Bank

# Testing the dApp
storage_file = "bank_accounts.json"
bank = Bank(storage_file)
bank.create_account("1234567890", initial_balance=1000)
bank.deposit("1234567890", 500)
bank.withdraw("1234567890", 200)
bank.transfer("1234567890", "9876543210", 300, tag="Expense")
bank.lend("1234567890", "8765432109", 1000, 0.05, tag="Loan")
print(bank.get_balance("1234567890"))
print(bank.get_balance("9876543210"))
print(bank.get_balance("8765432109"))
print(bank.blockchain.is_chain_valid())
bank.print_transactions()
