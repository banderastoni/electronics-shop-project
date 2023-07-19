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

    # @language.setter
    # def language(self, language):
    #     return language


class Keyboard(Item, MixinLang):
    pass

    # def __init__(self, name: str, price: float, quantity: int, language):
    #     super().__init__(name, price, quantity)
    #     self.language = language
