from abc import ABC, abstractmethod


class Product:


    def __init__(self, name: str, price: float, quantity: int):
        """Constructor for product attributes with type and value checks."""
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number (int or float).")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price must be non-negative.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None


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


    def show(self):
        """Function to print information of the object """
        promotion_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
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
        # quantity wird auf den Default-Wert zurückgesetzt
        self._quantity = 1000000


    def show(self):
        #super().show()
        promotion_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        print(f"{self.name}, ${self.price:.2f}, Stock: {self.quantity}{promotion_info}")



class LimitedProduct(Product):

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """Initialize LimitedProduct with maximum purchase limit"""
        super().__init__(name, price, quantity)
        self.maximum = maximum  # new attribute for maximum order amount


    def show(self):
        promotion_info = f" | Promotion: {self.promotion.name}" if self.promotion else ""
        print(f"{self.name}, ${self.price:.2f}, Stock: {self.quantity}{promotion_info}")

"""********************
The following clases are not childs of Produkt
*************************"""

class Promotion(ABC):
    """
    Abstrakte Promotion-Klasse, die als Grundlage für spezifische Promotion-Typen dient.
    """

    def __init__(self, name: str):
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Abstrakte Methode, die die Promotion-Logik implementiert.
        Muss von abgeleiteten Klassen überschrieben werden.
        :param product: Das Produkt, auf das die Promotion angewendet wird.
        :param quantity: Die Anzahl, die gekauft wird.
        :return: Der berechnete Preis nach Anwendung der Promotion.
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