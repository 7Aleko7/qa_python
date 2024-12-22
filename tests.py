import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating(поменял rating на genre чтобы пример отрабатывал корректно), имеет длину 2(
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_default_list_of_genres_true(self):
        collector = BooksCollector()

        assert collector.genre==['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_add_new_book_add_book_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.get_book_genre('Гордость и предубеждение и зомби')==''

    @pytest.mark.parametrize('book',['','Сорок один1 символ в название не подходит'])
    def test_add_new_book_with_negative_name(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)

        assert book not in collector.books_genre

    def test_set_book_genre_for_books_added_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак','Фантастика')

        assert collector.books_genre['Ведьмак']=='Фантастика'


    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак','Фантастика')

        assert collector.get_book_genre('Ведьмак')=='Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        books=['Ведьмак', 'Пила', 'Шрек', 'Наруто', 'Хоббит']
        for book in books:
            collector.add_new_book(book)

        books_genre={'Ведьмак':'Фантастика', 'Пила':'Ужасы', 'Шрек':'Мультфильмы', 'Наруто':'Мультфильмы'}
        for key, value in books_genre.items():
            collector.set_book_genre(key, value)

        books_with_cartoon_genre=['Шрек','Наруто']
        assert collector.get_books_with_specific_genre('Мультфильмы')==books_with_cartoon_genre

    def test_get_books_genre(self):
        collector = BooksCollector()

        books=['Ведьмак', 'Пила', 'Шрек', 'Наруто', 'Хоббит',]
        for book in books:
            collector.add_new_book(book)

        added_books_genre={'Ведьмак':'Фантастика', 'Пила':'Ужасы', 'Шрек':'Мультфильмы', 'Наруто':'Мультфильмы'}
        for key, value in added_books_genre.items():
            collector.set_book_genre(key, value)

        books_genre = {'Ведьмак': 'Фантастика', 'Пила': 'Ужасы', 'Шрек': 'Мультфильмы', 'Наруто': 'Мультфильмы','Хоббит':''}
        assert collector.get_books_genre()==books_genre

    def test_get_books_for_children(self):
        collector = BooksCollector()

        books=['Ведьмак', 'Пила', 'Шрек', 'Шерлок', 'Горько']
        for book in books:
            collector.add_new_book(book)

        added_books_genre={'Ведьмак':'Фантастика', 'Пила':'Ужасы', 'Шрек':'Мультфильмы', 'Шерлок':'Детективы','Горько':'Комедии'}
        for key, value in added_books_genre.items():
            collector.set_book_genre(key, value)

        children_books = ['Ведьмак', 'Шрек', 'Горько']
        assert collector.get_books_for_children()==children_books


    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        books = ['Ведьмак', 'Пила', 'Шрек', 'Шерлок', 'Горько']
        for book in books:
            collector.add_new_book(book)

        collector.add_book_in_favorites('Ведьмак')
        assert 'Ведьмак' in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        books = ['Ведьмак', 'Пила', 'Шрек', 'Шерлок', 'Горько']
        for book in books:
            collector.add_new_book(book)

        collector.add_book_in_favorites('Ведьмак')
        collector.delete_book_from_favorites('Ведьмак')
        assert 'Ведьмак' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        books = ['Ведьмак', 'Пила', 'Шрек', 'Шерлок', 'Горько']
        for book in books:
            collector.add_new_book(book)

        collector.add_book_in_favorites('Ведьмак')
        collector.add_book_in_favorites('Пила')
        favorites=['Ведьмак','Пила']
        assert collector.get_list_of_favorites_books()==favorites
