from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract promotion class that serves as the basis for specific promotion types.
    """
    def __init__(self, name: str):
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Abstract method that implements the promotion logic.
        Must be overridden by derived classes.
        :param product: The product to which the promotion is applied.
        :param quantity: The quantity to purchase.
        :return: The price charged after the promotion is applied.
        """
        pass

class PercentDiscount(Promotion):
    """
    Procentual Discount-Promotion (e.g. 30% discount).
    """
    def __str__(self):
        return f"{self.name} ({self.percent}% off)"


    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.name = name
        self.percent = percent


    def apply_promotion(self, product, quantity: int) -> float:
        #print("30% check")
        discount = product.price * (self.percent / 100)
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """
    Calculate without remaining quantity divided by 2, which is then calculated as half the price.
    """
    def __init__(self, name: str):
        super().__init__(name)


    def apply_promotion(self, product, quantity: int) -> float:
        #print("Check the half price!")
        full_price_items = (quantity + 1) // 2
        half_price_items = quantity - full_price_items
        return full_price_items * product.price + half_price_items * (product.price / 2)


class ThirdOneFree(Promotion):
    """
    Calculate without remaining quantity divided by 3, which is then calculated without a price.
    """
    def __init__(self, name: str):
        super().__init__(name)


    def apply_promotion(self, product, quantity: int) -> float:
        #print("Check the third gratis!")
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price



def main():
    pass


if __name__ == "__main__":
    main()