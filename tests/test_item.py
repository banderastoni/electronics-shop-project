"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item3 = Item("Часы", 30000, 3)


def test_init():
    assert item3.name == "Часы"
    assert item3.price == 30000
    assert item3.quantity == 3


def test_calculate_total_price():
    assert item3.calculate_total_price() == 90000


def test_apply_discount():
    Item.pay_rate = 0.5
    item3.apply_discount()
    assert item3.price == 15000
