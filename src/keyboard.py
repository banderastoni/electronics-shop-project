from src.item import Item


class MixinLang:
    """Класс миксин, для добавления атрибута language и метода change_lang"""

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLang):
    pass
