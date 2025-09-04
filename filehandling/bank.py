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

# Create 2 accounts
acc1 = BankAccount("001", 1000)
acc2 = BankAccount("002", 500)

# Loop menu
while True:
    print("\n--- Menu ---")
    print("1. Deposit to Account 1")
    print("2. Withdraw from Account 1")
    print("3. Transfer from Account 1 to Account 2")
    print("4. Check balances")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        acc1.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter withdrawal amount: "))
        acc1.withdraw(amt)
    elif choice == "3":
        amt = float(input("Enter transfer amount: "))
        acc1.transfer(acc2, amt)
    elif choice == "4":
        acc1.check_balance()
        acc2.check_balance()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
