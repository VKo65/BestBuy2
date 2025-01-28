class Store:
    """Constructor for class Store. """
    def __init__(self, product):
        """Constructor for store attributes with type and value checks."""
        if not isinstance(product, list):
            raise TypeError("Product list must be a list.")
        #if not all(isinstance(item, Product) for item in product):
            #raise TypeError("All items in the product list must be instances of the Product class.")
        if not product:
            raise ValueError("Product list cannot be empty.")

        self.list_of_products = product


    def add_product(self, product):
        """Function to expand list"""
        self.list_of_products.append(product)


    def remove_product(self, product):
        """Function to reduce list of products"""
        if product in self.list_of_products:
            self.list_of_products.remove(product)


    def get_total_quantity(self):
        """Function to add the amount of all products, used in main"""
        return sum(product.quantity for product in self.list_of_products)


    def get_all_products(self):
        """Generates a list of all available products"""
        return [product for product in self.list_of_products if product.active == True]


    def order(self, shopping_list):
        """Function used in main, to order a created list (from user input).
        Check if quantity is available and calculate new quantity and total price.
        Return the total price."""
        total_price = 0
        for product, quantity in shopping_list:
            # Check maximum of quantity
            if hasattr(product, "maximum") and product.maximum is not None:
                if quantity > product.maximum:
                    raise ValueError(f"You can only order a maximum of {product.maximum} units of {product.name}.")
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                print(f"Error with product {product.name}: {e}")

        return total_price


def main():

   """ product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    oproducts = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(oproducts[0], 1), (oproducts[1], 2)]))"""



if __name__ == "__main__":
    main()

