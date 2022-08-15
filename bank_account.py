class BankAccount:
    account_id: str
    bank_name: str
    bank_id: str

    def __init__(self, account_id: str, bank_name: str, bank_id: str) -> None:
        self.account_id = account_id
        self.bank_name = bank_name
        self.bank_id = bank_id

    def get_account_id(self) -> str:
        return self.account_id

    def set_account_id(self, account_id: str) -> None:
        self.account_id = account_id

    def get_bank_name(self) -> str:
        return self.bank_name

    def set_bank_name(self, bank_name: str) -> None:
        self.bank_name = bank_name

    def get_bank_id(self) -> str:
        return self.bank_id

    def set_bank_id(self, bank_id: str) -> None:
        self.bank_id = bank_id

    def deposit(self, amount: float) -> bool:
        return True

    def toString(self) -> str:
        return f"Account id: {self.account_id}, Bank name: {self.bank_name}, Bank id: {self.bank_id}"