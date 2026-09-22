#Design a BankAccount class that allows users to deposit, withdraw,
#  and check their account balance.
class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.__account_holder = account_holder
        self.__balance = initial_balance

    def get_account_holder(self) -> str:
        return self.__account_holder

    def set_account_holder(self, new_name: str) -> None:
        self.__account_holder = new_name

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def display_account_info(self) -> None:
        print(f"Account Holder: {self.__account_holder}")
        print(f"Current Balance: ${self.__balance:.2f}")

    def calculate_interest(self, rate: float = 0.02) -> float:
        if rate < 0:
            raise ValueError("Interest rate can't be negative.")
        return self.__balance * rate


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        super().__init__(account_holder, initial_balance)
        
    def calculate_interest(self, rate: float = 0.03) -> float:
        """Calculate interest at the savings-account rate."""
        if rate < 0:
            raise ValueError("Interest rate can't be negative.")
        return self.get_balance() * rate
    



accounts = [
    BankAccount("Alan Turing", 500.00),
    SavingsAccount("John Luther", 600.00),
    BankAccount("Anna Bella", 1000.00),
    SavingsAccount("Mary Vincent", 1500.00),
    BankAccount("Vincent Gomas", 2000.00),
]


def menu(account: BankAccount):
    while True:
        print("\nBANK ACCOUNT MENU")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. intrest")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print(f"Deposit successful. New balance: ${account.get_balance():.2f}")

            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                print(f"Withdrawal successful. New balance: ${account.get_balance():.2f}")

            elif choice == "3":
                print(f"Current balance: ${account.get_balance():.2f}")

            elif choice == "4":
                interest = account.calculate_interest()
                print(f"interest : ${interest :.2f}")

            elif choice == "5":
                print("Thank you for using the bank service.")
                break

            else:
                print("Invalid option. Please choose 1, 2, 3, or 4.")

        except ValueError as e:
            print(f"Error: {e}")



name = input("Enter your account holder name: ").strip()
account = next((acc for acc in accounts if acc.get_account_holder().lower() == name.lower()), None)

if account is None:
    account = BankAccount(name, 0.0)
    print(f"Account not found. New account created for {account.get_account_holder()}.")
else:
    print(f"Welcome, {account.get_account_holder()}!")

menu(account)