import pytest

from src.item import Item
from src.phone import Phone


def test_phone_init(phone_test):
    assert phone_test.name == 'Xiaomi 11'
    assert phone_test.price == 30000
    assert phone_test.quantity == 5
    assert phone_test.number_of_sim == 2


def test_phone_item_add(phone_test):
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone_test == 25
    assert phone_test + phone_test == 10


def test_phone_str_repr(phone_test):
    assert str(phone_test) == 'Xiaomi 11'
    assert repr(phone_test) == "Phone('Xiaomi 11', 30000, 5, 2)"


def test_phone_number_of_sim(phone_test):
    assert phone_test.number_of_sim == 2
    phone_test.number_of_sim = 1
    assert phone_test.number_of_sim == 1
    with pytest.raises(ValueError):
        phone_test.number_of_sim = 0


@pytest.fixture
def phone_test():
    phone1 = Phone("Xiaomi 11", 30_000, 5, 2)
    return phone1
