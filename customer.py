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
        """Retorna todas las facturas asociadas al cliente.

        Parameters
        ----------
        None

        Returns
        -------
        invoices : list[Invoice]
            Lista de facturas.
        """
        return self.invoices

    def set_invoices(self, invoice: Invoice) -> None:
        """Guarda una nueva factura asociada al cliente.

        Parameters
        ----------
        invoice : Invoice
            Una nueva factura de envio o envios.

        Returns
        -------
        None
        """
        self.invoices.append(invoice)

    def get_credit_cards(self) -> list[CreditCard]:
        """Retorna todas las tarjetas de credito asociadas al cliente.

        Parameters
        ----------
        None

        Returns
        -------
        credit_cards : list[CreditCard]
            Lista de tarjetas de credito.
        """
        return self.credit_cards

    def set_credit_cards(self, credit_card: CreditCard) -> None:
        """Guarda una tarjeta asociada al cliente.

        Parameters
        ----------
        credit_card : CreditCard
            Una tarjeta de credito.

        Returns
        -------
        None
        """
        self.credit_cards.append(credit_card)

    def get_shippings(self) -> list[Location]:
        """Retorna todas las direcciones de entrega asociadas al cliente.

        Parameters
        ----------
        None

        Returns
        -------
        shippings : list[Location]
            Lista de direcciones de entrega.
        """
        return self.shippings

    def set_shippings(self, shipping: Location) -> None:
        """Guarda una direccion de entrega asociadas al cliente.

        Parameters
        ----------
        shipping : Location
            Direccion de entrega.

        Returns
        -------
        None
        """
        self.shippings.append(shipping)

