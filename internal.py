from person import Person
from enumerations import Role, DocumentType, PersonType
from bank_account import BankAccount


class Internal(Person):
    role: Role
    account: BankAccount

    def __init__(self, national_id: DocumentType, id_type: DocumentType, name: str, last_name: str, person_type: PersonType, email: str, role: Role, account: BankAccount) -> None:
        super().__init__(national_id, id_type, name, last_name, person_type, email)
        self.role = role
        self.account = account

    def get_role(self) -> Role:
        return self.role

    def set_role (self, role: Role) -> None:
        self.role = role

    def get_account(self) -> BankAccount:
        return self.role

    def set_account (self, account: BankAccount) -> None:
        self.account = account
