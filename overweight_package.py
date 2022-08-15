from package import Package


class OverweightPackage(Package):
    OVERWEIGHT_GRAM_PRICE: float = 24.5

    def calculate(self) -> float:
        WEIGHT_PRICE: float = super().calculate()
        OVERWEIGHT_VALUE = self.weight - 2.0 if self.weight > 2.0 else 0.0
        return WEIGHT_PRICE + (OVERWEIGHT_VALUE * self.OVERWEIGHT_GRAM_PRICE)