from abc import abstractmethod, ABC
import string
import random
from customer import Customer


class Package(ABC):
    ID: str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    GRAMS_PRICE: float = 20.4
    code: int
    description: str
    weight: float
    customer: Customer

    def __init__(self, code: int, description: str, weight: float, customer: Customer) -> None:
        self.code = code
        self.description = description
        self.weight = weight
        self.customer = customer

    def get_id(self) -> str:
        return self.ID

    def get_grams_price(self) -> float:
        return self.GRAMS_PRICE

    def get_code(self) -> int:
        return self.code

    def set_code(self, code: int) -> None:
        self.code = code
    
    def get_description(self) -> str:
        return self.description

    def set_description(self, description: str) -> None:
        self.description = description

    def get_weight(self) -> float:
        return self.weight

    def set_weight(self, weight: float) -> None:
        self.weight = weight

    def get_customer(self) -> Customer:
        return self.customer

    def set_customer(self, customer: Customer) -> None:
        self.customer = customer

    @abstractmethod
    def calculate(self) -> float:
        return (self.weight / 1000) * self.GRAMS_PRICE
    
    @abstractmethod
    def toString(self) -> str:
        return f"Id: {self.ID}, Code: {self.code}, Weight: {self.weight}, Description: {self.description}, Customer: {self.customer}"
