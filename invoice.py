from enumerations import InvoiceStatus
from order import Order
from customer import Customer
from enumerations import PaymentMethodsTypes
import string
import random


class Invoice:
    ID: str = ''.join(random.choice(string.digits) for _ in range(10))
    orders: list[Order]
    status: InvoiceStatus
    client: Customer
    tax: float
    price: float
    discount: float
    payment_method: PaymentMethodsTypes

    def __init__(self, order: Order, status: InvoiceStatus, client: Customer, tax: float, price: float, discount: float, payment_method: PaymentMethodsTypes) -> None:
        self.orders.append(order)
        self.status = status
        self.client = client
        self.tax = tax
        self.price = price
        self.discount = discount
        self.payment_method = payment_method

    def get_id(self) -> str:
        return self.ID
    
    def get_orders(self) -> list[Order]:
        return self.orders

    def set_orders(self, order: Order) -> None:
        self.orders.append(order)

    def get_status(self) -> InvoiceStatus:
        return self.status

    def set_status(self, status: InvoiceStatus) -> None:
        self.status = status

    def get_client(self) -> Customer:
        return self.client

    def set_client(self, client: Customer) -> None:
        self.status = client

    def get_tax(self) -> float:
        return self.tax

    def set_tax(self, tax: float) -> None:
        self.tax = tax

    def get_price(self) -> float:
        return self.price

    def set_price(self, price: float) -> None:
        self.status = price

    def get_discount(self) -> float:
        return self.discount

    def set_discount(self, discount: float) -> None:
        self.discount = discount

    def get_payment_method(self) -> PaymentMethodsTypes:
        return self.payment_method

    def set_payment_method(self, payment_method: PaymentMethodsTypes) -> None:
        self.discount = payment_method

    def to_string(self) -> str:
        return f"ID: {self.ID}, status: {self.status}, Client: {self.client.name} {self.client.last_name}, Price: {self.price}, Tax: {self.tax}, Discount: {self.discount}, Payment method: {self.payment_method}"
    


