class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):

    MIN_PAGES = 1  # 1 страница

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < self.MIN_PAGES:
            raise ValueError("Количество страниц меньше минимально допустимого значения")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):

    MIN_DURATION = 0.02  # ~ 1 минута

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float")
        if duration < self.MIN_DURATION:
            raise ValueError("Продолжительность аудиокниги меньше минимально допустимого значения")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == '__main__':
    paper_book = PaperBook("Охота на овец", "Х.Мураками", 356)
    audio_book = AudioBook("Молот Вулкана", "Ф.Дик", 2.5)
    print(paper_book)
    print(repr(paper_book))
    print(audio_book)
    print(repr(audio_book))
    paper_book.pages = 400
    print(paper_book)
    print(repr(paper_book))
    audio_book.duration = 3.0
    print(audio_book)
    print(repr(audio_book))
