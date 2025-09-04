class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        print(f"Deposited ₹{amount}. Current balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Current balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Account {self.acc_no} balance: ₹{self.balance}")

    def transfer(self, other, amount):
        if amount > self.balance:
            print("Insufficient balance to transfer!")
        else:
            self.balance -= amount
            other.balance += amount
            print(f"Transferred ₹{amount} to account {other.acc_no}")
            print(f"Your current balance: ₹{self.balance}")


# Create 3 accounts
acc1 = BankAccount("001", 1000)
acc2 = BankAccount("002", 500)
acc3 = BankAccount("003", 700)

accounts = {"001": acc1, "002": acc2, "003": acc3}

# Loop menu
while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check balances")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        acc_no = input("Enter account number: ")
        amt = float(input("Enter deposit amount: "))
        accounts[acc_no].deposit(amt)

    elif choice == "2":
        acc_no = input("Enter account number: ")
        amt = float(input("Enter withdrawal amount: "))
        accounts[acc_no].withdraw(amt)

    elif choice == "3":
        from_acc = input("Enter sender account number: ")
        to_acc = input("Enter receiver account number: ")
        amt = float(input("Enter transfer amount: "))
        accounts[from_acc].transfer(accounts[to_acc], amt)

    elif choice == "4":
        for acc in accounts.values():
            acc.check_balance()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
