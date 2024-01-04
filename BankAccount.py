# Create a program that manages a simple bank account 
# Program allows user to deposit, withdraw, and check balance
# Error handling for invalid inputs (like withdrawing over the limit or depositing negative amounts)
# Logs every transaction and allows user to view the transaction history 
# Simple interest calculator that updates the balance on a monthly basis based on an annual interest rate

class BankAccount:
    # This class function will have account holder name, balance, and transaction history 
    def __init__(self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        '''
        This function handles the deposit amount, which must be a positive number 
        '''
        if amount <= 0:
            return "Invalid deposit amount. Please enter a positive number."
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        return f"Deposited {amount}. New balance: {self.balance}"
    
    def withdraw(self, amount):
        '''
        This function handles the withdrawal amount, which must be a positive number and user must have sufficient balance 
        '''
        if amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive number."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: {amount}")
        return f"Withdraw {amount}. New balance: {self.balance}"
    
    def get_balance(self):
        return f"Current balance: {self.balance}"
        
    def show_transaction_history(self):
        return "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."
    
def main():
    name = input("Enter the account holder's name: ")
    account = BankAccount(name)
    
    while True: 
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == '3':
            print(account.get_balance())
        elif choice == '4':
            print(account.show_transaction_history())
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose a valid action.")

if __name__ == "__main__":
    main()