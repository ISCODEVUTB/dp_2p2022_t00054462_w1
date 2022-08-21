from abc import ABC, abstractmethod
from enumerations import DocumentType, PersonType
from location import Location
import string
import random


class Person(ABC):
    ID: str = ''.join(random.choice(string.digits) for _ in range(8))
    national_id: str
    id_type: DocumentType
    name: str
    last_name: str
    person_type: PersonType
    email: str

    def __init__(self, national_id: DocumentType, id_type: DocumentType, name: str, last_name: str, person_type: PersonType, email: str) -> None:
        self.national_id = national_id
        self.id_type = id_type
        self.name = name
        self.last_name = last_name
        self.person_type = person_type
        self.email = email

    def get_id(self) -> str:
        return self.ID

    def get_national_id(self) -> str:
        return self.national_id

    def set_national_id(self, national_id: str) -> None:
        self.national_id = national_id

    def get_id_type(self) -> DocumentType:
        return self.id_type

    def set_id_type(self, id_type: DocumentType) -> None:
        self.id_type = id_type

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_last_name(self) -> str:
        return self.last_name

    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name

    def get_person_type(self) -> PersonType:
        return self.person_type

    def set_person_type(self, person_type: PersonType) -> None:
        self.person_type = person_type

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str) -> None:
        self.email = email

    @abstractmethod
    def biometric_validation(self):
        return ("User identity is valid")

    @abstractmethod
    def to_string(self) -> str:
        return f"Id: {self.ID}, Name: {self.name}, Last name: {self.last_name}, Email: {self.email}, Document type: {self.document_type}, National id: {self.national_id}, Person type: {self.person_type}"
