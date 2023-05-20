from flask import Flask, render_template, request
from bank import Bank

app = Flask(__name__)
storage_file = "bank_accounts.json"
bank = Bank(storage_file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        account_number = request.form["account_number"]
        initial_balance = float(request.form["initial_balance"])
        bank.create_account(account_number, initial_balance)
        return render_template("message.html", message="Account created successfully!")
    return render_template("create_account.html")

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        account_number = request.form["account_number"]
        amount = float(request.form["amount"])
        bank.deposit(account_number, amount)
        return render_template("message.html", message="Deposit successful!")
    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        account_number = request.form["account_number"]
        amount = float(request.form["amount"])
        tag = request.form["tag"]
        bank.withdraw(account_number, amount, tag=tag)
        return render_template("message.html", message="Withdrawal successful!")
    return render_template("withdraw.html")

@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    if request.method == "POST":
        sender_account = request.form["sender_account"]
        receiver_account = request.form["receiver_account"]
        amount = float(request.form["amount"])
        bank.transfer(sender_account, receiver_account, amount)
        return render_template("message.html", message="Transfer successful!")
    return render_template("transfer.html")

@app.route("/lend", methods=["GET", "POST"])
def lend():
    if request.method == "POST":
        lender_account = request.form["lender_account"]
        borrower_account = request.form["borrower_account"]
        amount = float(request.form["amount"])
        interest_rate = float(request.form["interest_rate"])
        bank.lend(lender_account, borrower_account, amount, interest_rate)
        return render_template("message.html", message="Loan successful!")
    return render_template("lend.html")

@app.route("/get_balance", methods=["GET", "POST"])
def get_balance():
    if request.method == "POST":
        account_number = request.form["account_number"]
        balance = bank.get_balance(account_number)
        if balance is not None:
            return render_template("message.html", message=f"Account balance: {balance}")
        else:
            return render_template("message.html", message="Invalid account number.")
    return render_template("get_balance.html")

@app.route("/print_transactions")
def print_transactions():
    transactions = bank.get_transactions()
    return render_template("transactions.html", transactions=transactions)

@app.route("/exit")
def exit_app():
    return render_template("message.html", message="Exiting the program...")

if __name__ == "__main__":
    app.run(debug=True)
