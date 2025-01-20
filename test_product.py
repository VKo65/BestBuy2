from products import Product
import pytest

def test_valid_product():
    """Test creating a valid product and its attributes"""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.name == "Bose QuietComfort Earbuds"
    assert bose.price == 250
    assert bose.quantity == 500
    assert bose.active == True  # Prüft die @property active

def test_invalid_product():
    """Test creating a product with invalid attributes"""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Name darf nicht leer sein

    with pytest.raises(ValueError):
        Product("Invalid Product", price=-1, quantity=100)  # Preis darf nicht negativ sein

    with pytest.raises(ValueError):
        Product("Invalid Product", price=1450, quantity=-10)  # Menge darf nicht negativ sein