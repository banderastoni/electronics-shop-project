from src.item import Item


class Phone(Item):
    """ Класс унаследовал все атрибуты и методы супер-класса Item,
    + атрибут, содержащий кол-во поддерживаемых сим-карт"""
    def __init__(self, name, price, quantity, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер number_of_sim
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """
        Сеттер number_of_sim + проверка на кол-во сим-карт (целое число и >0)
        """
        if number > 0:
            self.__number_of_sim = number
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
