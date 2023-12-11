import doctest


class Footballer:
    def __init__(self, position: str, club: str, nationality: str, age: int):

        """
        Создание и подготовка к работе объекта "Футболист"

        :param position: Позиция футболиста на поле
        :param club: Клуб, в котором играет футболист
        :param nationality: Национальность футболиста
        :param age: Возраст футболиста

        Примеры:
        >>> footballer = Footballer('GK', 'Barcelona', 'Spain', 25) # инициализация экземпляра класса
        """
        if not isinstance(position, str):
            raise TypeError("Позиция игрока должна быть типа str")
        self.position = position

        if not isinstance(club, str):
            raise TypeError("Клуб игрока должен быть типа str")
        self.club = club

        if not isinstance(nationality, str):
            raise TypeError("Национальность игрока должна быть типа str")
        self.nationality = nationality

        if not isinstance(age, int):
            raise TypeError("Возраст игрока должен быть типа int")
        if age < 16:
            raise ValueError("Футболист слишком молод и не может привлекаться к взрослой команде!")
        self.age = age

    def is_young(self) -> bool:
        """
        Функция, которая проверяет, достаточно ли молод футболист
        (чтобы выступать за сборную U21, то есть футболист моложе 22)

        :return: Является ли возраст футболиста 21 и менее

        Примеры:
        >>> footballer = Footballer('GK', 'Barcelona', 'Spain', 25)
        >>> footballer.is_young()
        """
        ...

    def get_injured(self, injury: bool) -> str:
        """
        Сообщает, что футболисту нанесли травму (или нет).
        :param injury: Наличие травмы

        :return: Строка о наличии травмы у игрока

        Примеры:
        >>> footballer = Footballer('GK', 'Barcelona', 'Spain', 25)
        >>> footballer.get_injured(True)
        """
        if not isinstance(injury, bool):
            raise TypeError("Информация о травме должна быть типа bool")
        ...

    def change_club(self, club: str) -> None:
        """
        Смена клуба (трансфер)

        Примеры:
        >>> footballer = Footballer('GK', 'Barcelona', 'Spain', 25)
        >>> footballer.change_club('Chelsea')
        """
        if not isinstance(club, str):
            raise TypeError("Футбольный клуб должен быть типа str")
        ...


class FootballField:
    def __init__(self, length: float, width: float, coverage: str):

        """
        Создание и подготовка к работе объекта "Футбольное поле"

        :param length: Длина поля
        :param width: Ширина поля
        :param coverage: Покрытие поля (трава, паркет, песок и тд)

        Примеры:
        >>> football_field = FootballField(37.0, 28.0, 'Sand') # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(coverage, str):
            raise TypeError("Покрытие поля должно быть типа str")
        self.coverage = coverage

    def define_field_type(self) -> str:
        """
        Функция, которая на основе длины, ширины и типа покрытия определяет, к какому виду футбола относится поле

        :return: Сообщение о виде футбольного поля (поле для большого/пляжного/мини-футбола)

        Примеры:
        >>> football_field = FootballField(37.0, 28.0, 'Sand')
        >>> football_field.define_field_type()
        """
        ...

    def change_coverage(self, coverage: str) -> None:
        """
        Замена покрытия поля

        Примеры:
        >>> football_field = FootballField(37.0, 28.0, 'Sand')
        >>> football_field.change_coverage('Grass')
        """
        if not isinstance(coverage, str):
            raise TypeError("Покрытие поля должно быть типа str")
        ...

    def is_under_reconstruction(self, reconstruction: bool) -> str:
        """
        Сообщает, что поле находится на реконструкции (или нет).
        :param reconstruction: Поле на реконструкции или нет

        :return: Строка о статусе поля

        Примеры:
        >>> football_field = FootballField(37.0, 28.0, 'Sand')
        >>> football_field.is_under_reconstruction(False)
        """
        if not isinstance(reconstruction, bool):
            raise TypeError("Информация о реконструкции должна быть типа bool")
        ...


class FootballClub:
    def __init__(self, name: str, budget: float, year: int, players: int):

        """
        Создание и подготовка к работе объекта "Футбольный клуб"

        :param budget: Бюджет клуба (млн)
        :param year: Год основания клуба
        :param players: Количество игроков в клубе

        Примеры:
        >>> football_club = FootballClub('Bayern', 948.15, 1900, 25) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название клуба должно быть типа str")
        self.name = name

        if not isinstance(budget, (int, float)):
            raise TypeError("Бюджет должен быть типа int или float")
        self.budget = budget

        if not isinstance(year, int):
            raise TypeError("Год основания должен быть типа int")
        if year <= 0:
            raise ValueError("Год основания должен быть положительным числом")
        self.year = year

        if not isinstance(players, int):
            raise TypeError("Количество игроков должно быть типа int")
        if players < 7:
            raise ValueError("Количество игроков в составе должно быть не менее 7")
        self.players = players

    def is_bankrupt(self) -> bool:
        """
        Функция, которая на основе бюджета определяет, обанкротился ли клуб

        :return: Является ли клуб банкротом

        Примеры:
        >>> football_club = FootballClub('Bayern', 948.15, 1900, 25)
        >>> football_club.is_bankrupt()
        """
        ...

    def define_centry_of_foundation(self) -> str:
        """
        Определяет век основания футбольного клуба

        :return: Строка о веке основания клуба

        Примеры:
        >>> football_club = FootballClub('Bayern', 948.15, 1900, 25)
        >>> football_club.define_centry_of_foundation()
        """
        ...

    def add_player(self, player: str) -> None:
        """
        Добавляет игрока в команду и увеличивает количество игроков
        :param player: Новый игрок

        Примеры:
        >>> football_club = FootballClub('Bayern', 948.15, 1900, 25)
        >>> football_club.add_player('Kane')
        """
        if not isinstance(player, str):
            raise TypeError("Футболист должен быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
