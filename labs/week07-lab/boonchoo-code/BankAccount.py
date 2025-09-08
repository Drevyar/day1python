class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Method to deposit money"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        """Method to withdraw money"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds"
        else:
            return "Withdrawal amount must be positive"
    
    def get_balance(self):
        """Method to check balance"""
        return f"Current balance: ${self.balance}"
    
    def get_transaction_history(self):
        """Method to get transaction history"""
        if self.transaction_history:
            return "\n".join(self.transaction_history)
        else:
            return "No transactions yet"

# Example usage
account = BankAccount("John Doe", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print("\nTransaction History:")
print(account.get_transaction_history())