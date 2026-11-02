
import json
import random
import string
import hashlib
from pathlib import Path


class Bank:

    DATABASE = Path(__file__).resolve().parent / "data.json"
    data = []

    # Load database
    @classmethod
    def load_data(cls):
        try:
            if cls.DATABASE.exists():
                with open(cls.DATABASE, "r", encoding="utf-8") as file:
                    cls.data = json.load(file)
            else:
                cls.data = []

        except (json.JSONDecodeError, OSError):
            cls.data = []

    # Save database
    @classmethod
    def update(cls):
        with open(cls.DATABASE, "w", encoding="utf-8") as file:
            json.dump(cls.data, file, indent=4)

    # Generate unique account number
    @classmethod
    def account_generate(cls):
        while True:
            account_no = "".join(
                random.choices(string.digits, k=10)
            )

            if not any(
                user["accountNo"] == account_no
                for user in cls.data
            ):
                return account_no

    # Hash PIN
    # @staticmethod
    # def hash_pin(account_no, pin):
    #     return hashlib.sha256(
    #         f"{account_no}-{pin}".encode()
    #     ).hexdigest()

    # Authenticate user

    @classmethod
    def authenticate(cls, account_no, pin):
    
        account_no = str(account_no)
        pin = str(pin)
    
        for user in cls.data:
    
            if (
                user["accountNo"] == account_no
                and str(user["pin"]) == pin
            ):
                return user
    
        return None

    # Create account
    @classmethod
    def create_account(cls, name, age, email, pin):

        account_no = cls.account_generate()

        info = {
            "name": name,
            "age": age,
            "email": email,
            "accountNo": account_no,
            "pin": str(pin),
            "balance": 0
        }

        cls.data.append(info)
        cls.update()

        return account_no

    # Deposit money
    @classmethod
    def deposit(cls, account, amount):

        if amount <= 0:
            return False, "Amount must be greater than 0"

        if amount > 15000:
            return False, "Maximum deposit limit is ₹15000"

        account["balance"] += amount

        cls.update()

        return True, "Deposit successful"

    # Withdraw money
    @classmethod
    def withdraw(cls, account, amount):

        if amount <= 0:
            return False, "Amount must be greater than 0"

        if amount > 10000:
            return False, "Maximum withdrawal limit is ₹10000"

        if amount > account["balance"]:
            return False, "Insufficient balance"

        account["balance"] -= amount

        cls.update()

        return True, "Withdrawal successful"

    # Check account details
    @classmethod
    def check_details(cls, account):
        return account

    # Update account details
    @classmethod
    def update_details(cls, account, name, email, new_pin):

        if name:
            account["name"] = name

        if email:
            account["email"] = email

        if new_pin:
            account["pin"] = str(new_pin)

        cls.update()

    # Delete account
    @classmethod
    def delete_account(cls, account):

        if account["balance"] > 0:
            return False, "Withdraw balance before deleting account"

        cls.data.remove(account)
        cls.update()

        return True, "Account deleted successfully"


# Load data when module starts
Bank.load_data()
