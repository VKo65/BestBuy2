import products
import promotions
from store import Store

"""setup initial stock of inventory"""
# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = Store(product_list)

def start():
    """Displays the main menu of the store, processes user input
    and carries out corresponding actions:
    - Displays products
    - Returns the total number of products
    - Fulfills orders
    - Exits the program"""

    print("\n  Store Menu \n  ----------\n1. List all products in store\n"
          "2. Show total amount in store\n3. Make an order\n4. Quit")
    try:
        users_choice = int(input("Please chose a number: "))
    except ValueError:
        print("Please enter a number!")
        return True
    print(f"You chose option {users_choice}.")

    if users_choice > 4:
        raise Exception("Store Menu has only 4 choices!")

    elif users_choice == 1:
        for product in product_list:
            product.show()

    elif users_choice == 2:
        print(f"Total quantity in store: {best_buy.get_total_quantity()}")

    elif users_choice == 3:
        product_name = input("Please enter product name: ")
        try:
            product_quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Quantity should be a whole number!")
            return True
        # Searching for product
        chosen_product = None
        for product in product_list:
            if product.name == product_name:
                chosen_product = product
                break
        if chosen_product is None:
            print(f"Error: Product '{product_name}' not found!")
            return True
        try:
            total_price = chosen_product.buy(product_quantity)
            print(f"Order successful! Total price: ${total_price:.2f}")
        except Exception as e:
            print(f"Order failed: {e}")

    elif users_choice == 4:
        print("Goodbye!")
        return False
    return True


def main():
    start()
    """Starts the main Code and loop it until exit."""
    while start():
       start()

if __name__ == "__main__":
    main()
