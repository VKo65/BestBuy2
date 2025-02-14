from abc import ABC, abstractmethod
from itertools import product


class Product:


    def __init__(self, name: str, price: float, quantity: int):
        """Constructor for product attributes with type and value checks."""
        self._name = None
        self._price = None
        self._quantity = None
        self.promotion = None

        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        """returns the name"""
        return self._name

    @name.setter
    def name(self, value):
        """Set the name and should be not empty"""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("The name can't be empty")
        self._name = value

    @property
    def price(self):
        """returns the price"""
        return self._price

    @price.setter
    def price(self, value):
        """Set the price. It must be a positive value"""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a positive number.")
        self._price = value

    @property
    def quantity(self):
        """Gibt die verfügbare Menge zurück"""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Set quantity and must be positive"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Quantity must be positive.")
        self._quantity = value



    def set_promotion(self, promotion):
        """
        Set the promotion for the product
        """
        self.promotion = promotion


    @property
    def active(self):
        """Returns True if the product is active (quantity > 0)"""
        return self.quantity > 0


    def get_quantity(self: float):
        """Just output of instance quantity"""
        return self.quantity


    def set_quantity(self, quantity):
        """Function to be reduce quantity
        """
        self.quantity -= quantity
        if quantity < 1:
            self.deactivate()
        return


    def is_active(self):
        """Bool to check status of product"""
        return self.active


    @property
    def activate(self):
        """Function to activate product"""
        return self.quantity > 0


    def deactivate(self):
        """Function to deactivate product"""
        self.active = False
        return


    def show(self, product_number=None):
        """Function to print information of the object """
        promotion_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        if product_number is not None:  # Falls eine Nummer übergeben wurde
            print(f"{product_number}. {self.name}, ${self.price:.2f}, Stock: {self.quantity}{promotion_info}")
        else:
            print(f"{self.name}, ${self.price:.2f}, Stock: {self.quantity}{promotion_info}")


    def buy(self, quantity: int) -> float:
        """Allows buying a specified quantity with type and value checks."""
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if hasattr(self, "maximum") and quantity > self.maximum:
            raise ValueError(f"You can only order a maximum of {self.maximum} units of {self.name}.")
        if quantity > self.quantity:
            raise ValueError(f"There is not enough quantity in store. Available Quantity is: {self.quantity}")
        # Reduce stock by ordered quantity
        self.quantity -= quantity
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        return total_price

class NonStockedProduct(Product):

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=100000)


    @property
    def quantity(self):
        return self._quantity


    @quantity.setter
    def quantity(self, value):
        # quantity set to Default-value
        self._quantity = 1000000


    def show(self, product_number=None):
        #super().show()
        promotion_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        if product_number is not None:  # Falls eine Nummer übergeben wurde
            print(f"{product_number}. {self.name}, ${self.price:.2f}, Stock: {self.quantity}{promotion_info}")
        else:
            print(f"{self.name}, ${self.price:.2f}, Stock: {self.quantity}{promotion_info}")


class LimitedProduct(Product):

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """Initialize LimitedProduct with maximum purchase limit"""
        super().__init__(name, price, quantity)
        self.maximum = maximum  # new attribute for maximum order amount

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Maximum must be a positive integer.")
        self._maximum = value

    def show(self, product_number=None):
        promotion_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        if product_number is not None:  # Falls eine Nummer übergeben wurde
            print(f"{product_number}. {self.name}, ${self.price:.2f}, Stock: {self.quantity}{promotion_info}")
        else:
            print(f"{self.name}, ${self.price:.2f}, Stock: {self.quantity}{promotion_info}")



"""
********************
The following clases are not childs of Produkt
*************************
"""

class Promotion(ABC):
    """
    Abstract Promotion-class, as basis for Promotion-Type.
    """

    def __init__(self, name: str):
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Abstract method that implements promotion logic.
        Must be overridden by derived classes.
        :param product: The product to which the promotion is applied.
        :param quantity: The quantity that will be purchased.
        :return: The calculated price after applying the promotion.
        """
        pass

class PercentDiscount(Promotion):
    """
    Discount e.g. 30%
    """

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity: int) -> float:
        discount = product.price * (self.percent / 100)
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """
    Second product, for the half of price
    """

    def __init__(self, name: str):
        super().__init__(name)


    def apply_promotion(self, product, quantity: int) -> float:
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        return full_price_items * product.price + half_price_items * (product.price / 2)


class ThirdOneFree(Promotion):
    """
    Order 2, get 3
    """

    def __init__(self, name: str):
        super().__init__(name)


    def apply_promotion(self, product, quantity: int) -> float:
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price


def main():
    """bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()"""


if __name__ == "__main__":
    main()