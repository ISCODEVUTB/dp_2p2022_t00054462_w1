class BankAccount:
    account_id: str
    bank_name: str
    bank_id: str

    def __init__(self, account_id: str, bank_name: str, bank_id: str) -> None:
        self.account_id = account_id
        self.bank_name = bank_name
        self.bank_id = bank_id

    def get_account_id(self) -> str:
        """Retorna el id de la cuenta de banco.

        Parameters
        ----------
        None

        Returns
        -------
        account_id : str
            Id de la cuenta de banco
        """
        return self.account_id

    def set_account_id(self, account_id: str) -> None:
        """Guarda el id de la cuenta de banco.

        Parameters
        ----------
        account_id : str
            Id de la cuenta de banco

        Returns
        -------
        None
        """
        self.account_id = account_id

    def get_bank_name(self) -> str:
        """Retorna el nombre del banco al que pertece la cuenta.

        Parameters
        ----------
        None

        Returns
        -------
        bank_name : str
            Nombre del banco al que pertenece la cuenta
        """
        return self.bank_name

    def set_bank_name(self, bank_name: str) -> None:
        """Guarda el nombre del banco al que pertenece la cuenta.

        Parameters
        ----------
        bank_name : str
            Nombre del banco al que pertence la cuenta

        Returns
        -------
        None
        """
        self.bank_name = bank_name

    def get_bank_id(self) -> str:
        """Retorna el id del banco.

        Parameters
        ----------
        None

        Returns
        -------
        bank_id : str
            Id del banco
        """
        return self.bank_id

    def set_bank_id(self, bank_id: str) -> None:
        """Guarda el id del banco.

        Parameters
        ----------
        bank_id : str
            Nombre del banco al que pertence la cuenta

        Returns
        -------
        None
        """
        self.bank_id = bank_id

    def deposit(self, amount: float) -> bool:
        """Deposita una cantidad de dinero en una cuenta

        Parameters
        ----------
        amount : float
            Cantidad que se desea depositar

        Returns
        -------
        status : bool
            Resultado de la operacion de deposito

        """
        return True

    def to_string(self) -> str:
        """Devuelvo un string de todos los atributos de la clase con sus respectivos valores

        Parameters
        ----------
        None

        Returns
        -------
        bank_account : str
            Representacion en string de un objeto de la clase BankAccount
        """
        return f"Account id: {self.account_id}, Bank name: {self.bank_name}, Bank id: {self.bank_id}"
