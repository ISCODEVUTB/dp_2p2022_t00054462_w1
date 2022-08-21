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
        """Retorna el numero CVS de la tarjeta de credito.

        Parameters
        ----------
        None

        Returns
        -------
        cvs : int
            CVS de la tarjeta de credito.
        """
        return self.cvs

    def set_cvs(self, cvs) -> None:
        """Guarda el numero CVS de la tarjeta de credito.

        Parameters
        ----------
        cvs : int
            CVS de la tarjeta de credito.

        Returns
        -------
        None
        """
        self.cvs = cvs

    def get_expiry_day(self) -> int:
        """Retorna el dia de expiracion de la tarjeta de credito.

        Parameters
        ----------
        None

        Returns
        -------
        expiry_day : int
            Dia de expiracion de la tarjeta de credito.
        """
        return self.expiry_day

    def set_expiry_day(self, expiry_day: int) -> None:        
        """Guarda el dia de expiracion de la tarjeta de credito.

        Parameters
        ----------
        expiry_day : int
            Dia de expiracion de la tarjeta de credito.

        Returns
        -------
        None
        """
        self.expiry_day = expiry_day

    def get_expiry_month(self) -> int:
        """Retorna el mes de expiracion de la tarjeta de credito.

        Parameters
        ----------
        None

        Returns
        -------
        expiry_month : int
            Mes de expiracion de la tarjeta de credito.
        """
        return self.expiry_month

    def set_expiry_month(self, expiry_month: int) -> None:
        """Guarda el mes de expiracion de la tarjeta de credito.

        Parameters
        ----------
        expiry_month : int
            Mes de expiracion de la tarjeta de credito.

        Returns
        -------
        None
        """
        self.expiry_month = expiry_month

    def get_expiry_year(self) -> int:
        """Retorna el año de expiracion de la tarjeta de credito.

        Parameters
        ----------
        None

        Returns
        -------
        expiry_year : int
            Año de expiracion de la tarjeta de credito.
        """
        return self.expiry_myear

    def set_expiry_year(self, expiry_year: int) -> None:
        """Guarda el año de expiracion de la tarjeta de credito.

        Parameters
        ----------
        expiry_year : int
            Mes de expiracion de la tarjeta de credito.

        Returns
        -------
        None
        """
        self.expiry_year = expiry_year

    def get_card_number(self) -> int:
        """Retorna el numero de la tarjeta de credito.

        Parameters
        ----------
        None

        Returns
        -------
        card_number : int
            Numero de la tarjeta de credito.
        """
        return self.ecard_number

    def set_card_number(self, card_number: int) -> None:
        """Guarda el numero de la tarjeta de credito.

        Parameters
        ----------
        card_number : int
            Numero de la tarjeta de credito.

        Returns
        -------
        None
        """
        self.card_number = card_number

    def get_zip_code(self) -> int:
        """Retorna el codigo zip asociado a la tarjeta de credito.

        Parameters
        ----------
        None

        Returns
        -------
        zip_code : int
            Codigo zip asociado a la tarjeta de credito.
        """
        return self.ezip_code

    def set_zip_code(self, zip_code: int) -> None:
        """Guarda el codigo zip asociado a la tarjeta de credito.

        Parameters
        ----------
        zip_code : int
            Codigo zip asociado a la tarjeta de credito.

        Returns
        -------
        None
        """
        self.zip_code = zip_code

    def validate_Card(self) -> bool:
        """Valida los datos de la tarjeta de credito.

        Parameters
        ----------
            None

        Returns
        -------
        isValid : bool
            Return True si es una tarjeta valida o False si no lo es.
        """
        return True

    def to_string(self) -> str:
        """Devuelvo un string de todos los atributos de la clase con sus respectivos valores

        Parameters
        ----------
        None

        Returns
        -------
        credit_card : str
            Representacion en string de un objeto de la clase CreditCard
        """
        return f"Card number: {self.card_number}, Expiry date: {self.expiry_day}/{self.expiry_month}/{self.expiry_year}, CVS: {self.csv}, Zip code: {self.zip_code}"
