"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

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


@pytest.fixture
def test_by_fixture():
    item1 = Item("Телефон", 50000, 15)
    return item1


def test_name_setter(test_by_fixture):
    item0 = Item("Часы", 30000, 3)
    item0.name = 'Сеттер'
    assert item0.name == 'Сеттер'

    item0.name = 'Длинный Сеттер'
    assert item0.name == 'Длинный Се'

    test_by_fixture.name = 'Сеттер'
    assert test_by_fixture.name == 'Сеттер'
    test_by_fixture.name = 'Длинный Сеттер'
    assert test_by_fixture.name == 'Длинный Се'
