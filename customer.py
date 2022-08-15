from invoice import Invoice
from credit_card import CreditCard
from location import Location
from person import Person
from enumerations import  DocumentType, PersonType


class Customer(Person):
    invoices: list[Invoice]
    credit_cards: list[CreditCard]
    shippings: list[Location]

    def __init__(self, national_id: DocumentType, id_type: DocumentType, name: str, last_name: str, person_type: PersonType, email: str, invoice: Invoice, credit_card: CreditCard, shipping: Location) -> None:
        super().__init__(national_id, id_type, name, last_name, person_type, email)
        self.invoices.append(invoice)
        self.credit_cards.append(credit_card)
        self.shippings.append(shipping)

    def get_invoices(self) -> list[Invoice]:
        return self.invoices

    def set_invoices(self, invoice: Invoice) -> None:
        self.invoices.append(invoice)

    def get_credit_cards(self) -> list[CreditCard]:
        return self.credit_cards

    def set_credit_cards(self, credit_card: CreditCard) -> None:
        self.credit_cards.append(credit_card)

    def get_shippings(self) -> list[Location]:
        return self.shippings

    def set_shippings(self, shipping: Location) -> None:
        self.shippings.append(shipping)

