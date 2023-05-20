from bank import Bank

def print_menu():
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Lend")
    print("6. Get Balance")
    print("7. Print Transactions")
    print("8. Exit")

storage_file = "bank_accounts.json"
bank = Bank(storage_file)

while True:
    print("\n==== Banking App ====")
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.create_account(account_number, initial_balance)
        print("Account created successfully!")

    elif choice == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(account_number, amount)
        print("Deposit successful!")

    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        tag = input("Enter withdrawal purpose: ")
        bank.withdraw(account_number, amount, tag=tag)
        print("Withdrawal successful!")

    elif choice == "4":
        sender_account = input("Enter sender account number: ")
        receiver_account = input("Enter receiver account number: ")
        amount = float(input("Enter transfer amount: "))
        bank.transfer(sender_account, receiver_account, amount)
        print("Transfer successful!")

    elif choice == "5":
        lender_account = input("Enter lender account number: ")
        borrower_account = input("Enter borrower account number: ")
        amount = float(input("Enter loan amount: "))
        interest_rate = float(input("Enter interest rate: "))
        bank.lend(lender_account, borrower_account, amount, interest_rate)
        print("Loan successful!")

    elif choice == "6":
        account_number = input("Enter account number: ")
        balance = bank.get_balance(account_number)
        if balance is not None:
            print(f"Account balance: {balance}")
        else:
            print("Invalid account number.")

    elif choice == "7":
        bank.print_transactions()

    elif choice == "8":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")

