import doctest


class Footballer:
    """ Базовый класс: Футболист """

    MIN_AGE = 16
    MAX_AGE = 50

    def __init__(self, name: str, age: int, nationality: str) -> None:
        """
        Создание и подготовка к работе объекта "Футболист"

        :param name: Фамилия футболиста
        :param age: Возраст футболиста
        :param nationality: Гражданство футболиста
        Атрибуты непубличные, изменять их запрещено, чтобы избежать образования некорректных данных

        Примеры:
        >>> footballer = Footballer('Мбаппе', 25, 'Франция') # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Фамилия должна быть типа str")
        self._name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < self.MIN_AGE or age > self.MAX_AGE:
            raise ValueError("Возраст недопустим")
        self._age = age

        if not isinstance(nationality, str):
            raise TypeError("Гражданство должно быть типа str")
        self._nationality = nationality

    @property
    # только чтение атрибута name
    def name(self) -> str:
        return self._name

    @property
    # только чтение атрибута age
    def age(self) -> int:
        return self._age

    @property
    # только чтение атрибута nationality
    def nationality(self) -> str:
        return self._nationality

    def __str__(self) -> str:
        """ Наследуется, т.к. предполагает возвращение строкового представления объекта,
        куда входят общие для всех классов свойства """

        return f"Футболист: {self._name}. Возраст: {self._age}. Национальность: {self._nationality}."

    def __repr__(self) -> str:
        """ Перегружается, т.к. у дочерних классов появляются новые атрибуты """
        return f"{self.__class__.__name__}(name={self._name!r}, age={self._age!r}, nationality={self._nationality!r})"

    def increase_age(self) -> int:
        """
        Прибавляет футболисту год жизни
        Наследуется в дочерние классы
        """

        self._age = self._age + 1
        if self._age < self.MIN_AGE or self._age > self.MAX_AGE:
            raise ValueError("Возраст недопустим")
        return self._age

    def play_hand(self) -> None:
        """
        Сигнализирует об игре рукой
        Перегружается, т.к. последствия игры рукой у вратаря и полевого игрока трактуются по-разному согласно правилам
        """

        print(f"{self._name} сыграл рукой!")


class FieldPlayer(Footballer):
    """ Дочерний класс: Полевой игрок """

    def __init__(self, name: str, age: int, nationality: str, scored_goals: int) -> None:
        """
        Создание и подготовка к работе объекта "Полевой игрок"

        :param name: Фамилия полевого игрока
        :param age: Возраст полевого игрока
        :param nationality: Гражданство полевого игрока
        :param scored_goals: Забитые голы

        Примеры:
        >>> fieldPlayer1 = FieldPlayer('Мбаппе', 25, 'Франция', 15) # инициализация экземпляра класса
        """

        super().__init__(name, age, nationality)
        if not isinstance(scored_goals, int):
            raise TypeError("Количество забитых голов должно быть типа int")
        self.scored_goals = scored_goals

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, age={self._age!r}, nationality={self._nationality!r}, " \
               f"scored_goals={self.scored_goals!r})"

    def play_hand(self) -> None:
        """ Сообщает о попадании мяча в руку полевого игрока """

        print(f"{self._name} сыграл рукой! Судья назначает пенальти!")

    def score_goal(self) -> None:
        """ Сообщает о забитом футболистом голе """

        self.scored_goals = self.scored_goals + 1
        print(f"{self._name} забил гол! Это его {self.scored_goals} гол в сезоне.")


class Goalkeeper(Footballer):
    """ Дочерний класс: Вратарь """

    def __init__(self, name: str, age: int, nationality: str, missed_goals: int) -> None:
        """
        Создание и подготовка к работе объекта "Вратарь"

        :param name: Фамилия вратаря
        :param age: Возраст вратаря
        :param nationality: Гражданство вратаря
        :param missed_goals: Пропущенные голы

        Примеры:
        >>> goalkeeper1 = Goalkeeper('Куртуа', 31, 'Бельгия', 7) # инициализация экземпляра класса
        """
        super().__init__(name, age, nationality)
        if not isinstance(missed_goals, int):
            raise TypeError("Количество пропущенных голов должно быть типа int")
        self.missed_goals = missed_goals

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, age={self._age!r}, nationality={self._nationality!r}, " \
               f"missed_goals={self.missed_goals!r})"

    def play_hand(self) -> None:
        """ Сообщает о попадании мяча в руку вратарю """

        print(f"{self._name} сыграл рукой! Великолепный сейв!")

    def missed_goal(self) -> None:
        """ Сообщает о пропущенном вратарем голе """

        self.missed_goals = self.missed_goals + 1
        print(f"{self._name} не смог отбить удар! Это его {self.missed_goals} пропущенный мяч в сезоне.")


if __name__ == "__main__":
    doctest.testmod()
    fieldPlayer = FieldPlayer("Роналду", 39, "Португалия", 25)
    print(fieldPlayer)
    print(repr(fieldPlayer))
    fieldPlayer.increase_age()
    print(fieldPlayer)
    fieldPlayer.increase_age()
    print(fieldPlayer)
    fieldPlayer.score_goal()
    fieldPlayer.score_goal()
    print(repr(fieldPlayer))
    goalkeeper = Goalkeeper("Нойер", 37, "Германия", 6)
    print(goalkeeper)
    print(repr(goalkeeper))
    goalkeeper.increase_age()
    goalkeeper.missed_goal()
    goalkeeper.missed_goal()
    goalkeeper.missed_goal()
    fieldPlayer.play_hand()
    goalkeeper.play_hand()
    print(repr(goalkeeper))
    pass
