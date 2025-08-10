class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute to follow encapsulation principle
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
