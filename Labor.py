
def test_creating_invalid_product():
    """Arrange & Assert: Check the Exception for an invalid
    -Name
    -negative Price
    -negative Quantity
    """
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product(name="", price=100, quantity=10)
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        Product(name="Invalid Product", price=-50, quantity=10)
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        Product(name="Invalid Product", price=50, quantity=-30)


def test_quantity_get_zero():
    pass


def test_purchasing_modify_quantity ():
    pass


def test_buying_larger_quantity():
    pass