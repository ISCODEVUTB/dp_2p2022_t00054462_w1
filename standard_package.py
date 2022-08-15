from package import Package


class StandarPackage(Package):
    FLAT_PRICE: float = 4500.0

    def calculate(self) -> float:
        WEIGHT_PRICE: float = super().calculate()
        return WEIGHT_PRICE + self.FLAT_PRICE