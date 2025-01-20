class Product:

    def __init__(self, name: str, price: float, quantity: int):
        """Constructor for product attributes"""
        if not name or not isinstance(name, str):
            raise ValueError("Product name cannot be empty and must be a string!")  # Korrekt: ValueError
        if price <= 0:
            raise ValueError("Price must be greater than 0!")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def active(self):
        """Returns True if the product is active (quantity > 0)"""
        return self.quantity > 0


    def get_quantity(self: float):
        """Just output of instance quality"""
        return self.quantity


    def set_quantity(self, quantity):
        """Function to be reduce quantity
        """
        self.quantity -= quantity
        if quantity < 1:
            deactivate()
        return


    def is_active(self):
        """Bool to check status of product"""
        return self.active


    def activate(self):
        """Function to activate product"""
        self.active = True
        return


    def deactivate(self):
        """Function to deactivate product"""
        self.active = False
        return


    def show(self):
        """Function to print information of the object """
        print(f"{self.name}, {self.price}, {self.quantity}")

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception(f"There is not enough quantity in store. Available Quantity is: {self.quantity}")

        else:
            if self.quantity >= quantity:
                self.set_quantity(quantity)
                if self.quantity == 0:
                    self.active = False
            return f"Total price is: {self.price * quantity}"


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