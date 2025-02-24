import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) == 3:
            self.message = args[0]
        else:
            self.message = '\nФайл item.csv поврежден'


class RowChecker:
    def __init__(self, row):
        self.row = row
        if len(self.row) != 3:
            raise InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    @property
    def name(self):
        """
        Геттер name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер name + проверка на длину имени (не больше 10)
        """
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными
        из файла src/items.csv
        """
        cls.all = []
        try:

            with open(path, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    row_check = RowChecker(row)
                    cls.all.append(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

        except InstantiateCSVError as ex:
            # print(ex.message)
            raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(item):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(item))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
