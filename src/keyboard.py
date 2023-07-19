from src.item import Item


class MixinLang:
    """Класс миксин, для добавления атрибута language и метода change_lang"""

    # def __init__(self, language):

    #def __init__(self, name, price, quantity, __language):
    def __init__(self):
        # super().__init__()
        self.__language = 'EN'
        # super().__init__(self, name, price, quantity, __language)

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

    # def __init__(self, name, price, quantity):
    #     super().__init__(name, price, quantity)
    pass
