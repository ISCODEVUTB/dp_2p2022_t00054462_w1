class Location:
    country: str
    state: str
    city: str
    address_line1: str
    address_line2: str
    zip_code: int

    def __init__(self, country: str, state: str, city: str, address_line1: str, address_line2: str, zip_code: int) -> None:
        self.country = country
        self.state = state
        self.city = city
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.zip_code = zip_code
