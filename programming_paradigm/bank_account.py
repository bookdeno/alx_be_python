class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        rnside vi ---
        # locate the display_balance method and change it to:
        # def display_balance(self):
        #     print(f"Current Balance: ${self.account_balance:.2f}")
        # Then save and exit: ESC, :wq, ENTER

        # Stage all changes
        git add .

        # Commit with a clear message
        git commit -m "v1: display_balance prints two decimal places for ALX check"

        # Push to GitHub
        git push origin main

        # Optional: test the display output
        python3 main-0.py display
        eturn False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

