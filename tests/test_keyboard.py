import pytest

from src.keyboard import Keyboard


def test_keyboard_init(keyboard_test):
    assert keyboard_test.name == 'Nuphy AIR75'
    assert keyboard_test.price == 13490
    assert keyboard_test.quantity == 55


def test_mixinlang(keyboard_test):
    assert str(keyboard_test.language) == "EN"
    # Сделали EN -> RU
    keyboard_test.change_lang()
    assert str(keyboard_test.language) == "RU"

    # Сделали RU -> EN -> RU
    keyboard_test.change_lang().change_lang()
    assert str(keyboard_test.language) == "RU"

    # Сделали RU -> EN -> RU -> EN
    keyboard_test.change_lang().change_lang().change_lang()
    assert str(keyboard_test.language) == "EN"

    # Сделали EN -> RU
    keyboard_test.change_lang()
    assert str(keyboard_test.language) == "RU"

    # Сделали RU -> EN
    keyboard_test.change_lang()
    assert str(keyboard_test.language) == "EN"


@pytest.fixture
def keyboard_test():
    keyboard1 = Keyboard("Nuphy AIR75", 13490, 55)
    return keyboard1
