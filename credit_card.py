class CreditCard:
    cvs: int
    expiry_day: int
    expiry_month: int
    expiry_year: int
    card_number: int
    zip_code: int

    def __init__(self, cvs: int, expiry_day: int, expiry_year: int, expiry_month: int, card_number: int, zip_code: int) -> None:
        self.cvs = cvs
        self.expiry_day = expiry_day
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.card_number = card_number
        self.zip_code = zip_code

    def get_cvs(self) -> int:
        return self.cvs

    def set_cvs(self, cvs) -> None:
        self.cvs = cvs

    def get_expiry_day(self) -> int:
        return self.expiry_day

    def set_expiry_day(self, expiry_day: int) -> None:
        self.expiry_day = expiry_day

    def get_expiry_month(self) -> int:
        return self.expiry_month

    def set_expiry_month(self, expiry_month: int) -> None:
        self.expiry_month = expiry_month

    def get_expiry_year(self) -> int:
        return self.expiry_myear

    def set_expiry_year(self, expiry_year: int) -> None:
        self.expiry_year = expiry_year

    def get_card_number(self) -> int:
        return self.ecard_number

    def set_card_number(self, card_number: int) -> None:
        self.card_number = card_number

    def get_zip_code(self) -> int:
        return self.ezip_code

    def set_zip_code(self, zip_code: int) -> None:
        self.zip_code = zip_code

    def validate_Card(self) -> bool:
        return True

    def toString(self) -> str:
        return f"Card number: {self.card_number}, Expiry date: {self.expiry_day}/{self.expiry_month}/{self.expiry_year}, CVS: {self.csv}, Zip code: {self.zip_code}"