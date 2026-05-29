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
        books_genre = collector.get_books_genre()
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert isinstance(books_genre, dict)
        assert len(books_genre) == 2
        assert 'Гордость и предубеждение и зомби' in books_genre
        assert 'Что делать, если ваш кот хочет вас убить' in books_genre

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

 Roma1911-develop
 @pytest.mark.parametrize("book_name,genre", [
        ("Мстители", "Фантастика"),
        ("Крик", "Ужасы"),
        ("Убийство в ночном экспрессе", "Детективы"),
        ("Король Лев", "Мультфильмы"),
        ("Один дома", "Комедии"),

    @pytest.mark.parametrize("book_name,genre", [
    ("Мстители", "Фантастика"),
    ("Крик", "Ужасы"),
    ("Убийство в ночном экспрессе", "Детективы"),
    ("Король Лев", "Мультфильмы"),
    ("Один дома", "Комедии"),
 main
    ])
    def test_add_book_with_valid_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == genre
 Roma1911-develop



    
   
    def test_add_duplicate_book(self):
        collector = BooksCollector()
        book_name = "Мстители"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == genre 


    def test_add_name_book_more_exactly_40_chars(self):
        collector = BooksCollector()
        long_name = 'a' * 40
        collector.add_new_book(long_name)
        assert long_name in collector.books_genre
       

 main
    def test_add_name_book_more_than_40_chars(self):
        collector = BooksCollector()
        long_name = 'Очень очень длинное название книги где больше 40 слов'
        initial_count = len(collector.books_genre)
        collector.add_new_book(long_name)
        assert len(collector.books_genre) == initial_count
        assert long_name not in collector.books_genre


 Roma1911-develop

    def test_add_new_book_more_than_39_chars(self):
        collector = BooksCollector()
        long_name = 'a' * 39
        collector.add_new_book(long_name)
        assert long_name in collector.books_genre
        assert len(long_name) == 39


    def test_add_book_with_empty_name(self):
        collector = BooksCollector()
        empty_name = ''
        initial_count = len(collector.books_genre)
        collector.add_new_book(empty_name)
        assert len(collector.books_genre) == initial_count
        assert empty_name not in collector.books_genre

    def test_add_book_with_name_with_one_letter(self):
        collector = BooksCollector()
        book_name = 'A'
        initial_count = len(collector.books_genre)
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == initial_count + 1
        assert book_name in collector.books_genre


    def test_add_book_with_none_name(self):
        collector = BooksCollector()
        book_name = None
        initial_count =len(collector.books_genre)
        try:
            collector.add_new_book(book_name)
            assert len(collector.books_genre) == initial_count
            assert book_name not in collector.books_genre
        except TypeError:
            pass


    def test_add_book_name_of_the_numbers(self):
        collector = BooksCollector()
        book_name = 123
        initial_count = len(collector.books_genre)
        try: 
            collector.add_new_book(book_name)
            assert len(collector.books_genre) == initial_count
            assert book_name not in collector.books_genre
        except TypeError:
            pass


 main
    def test_set_book_genre_installing_the_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Посёлок')
        collector.set_book_genre('Посёлок', 'Фантастика')
        assert collector.books_genre['Посёлок'] == 'Фантастика'


    def test_get_book_genre_we_get_the_genre(self):
        collector = BooksCollector()
        collector.add_new_book('НЛО')
        collector.set_book_genre('НЛО', 'Фантастика')
        genre = collector.get_book_genre('НЛО')
        assert genre == 'Фантастика', "Жанр книги должен быть 'Фантастика'"


    def test_get_books_with_specific_genre_valid_genre_with_books(self):
        collector = BooksCollector()
        collector.add_new_book('Посёлок')
        collector.set_book_genre('Посёлок', 'Фантастика')

        collector.add_new_book('НЛО')
        collector.set_book_genre('НЛО', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        expected = ['Посёлок', 'НЛО']
        assert result == expected


    def test_get_books_genre_after_adding_books(self):
        collector = BooksCollector()
        collector.add_new_book('Мстители')
        collector.set_book_genre('Мстители', 'Фантастика')

        result = collector.get_books_genre()
        assert 'Мстители' in result
        assert result['Мстители'] == 'Фантастика'
        assert len(result) == 1


    def test_get_books_for_children_filters_adult_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Волшебник изумрудного города')
        collector.set_book_genre('Волшебник изумрудного города', 'Фантастика')

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        result = collector.get_books_for_children()
        assert 'Волшебник изумрудного города' in result
        assert 'Оно' not in result
        assert len(result) == 1


    def test_add_book_in_favorites_from(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в ночном экспрессе')
        collector.set_book_genre('Убийство в ночном экспрессе', 'Детектив')
        collector.add_book_in_favorites('Убийство в ночном экспрессе')
        favorites = collector.favorites
        assert 'Убийство в ночном экспрессе' in favorites
 Roma1911-develop
        assert len(favorites) == 1
        collector.add_book_in_favorites('Несуществующая книга')
        favorites = collector.favorites
        assert 'Несуществующая книга' not in favorites
        assert len(favorites) == 1
 main


    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в ночном экспрессе')
        collector.set_book_genre('Убийство в ночном экспрессе', 'Детектив')
        collector.add_book_in_favorites('Убийство в ночном экспрессе')
        favorites_before = collector.favorites
        assert 'Убийство в ночном экспрессе' in favorites_before
        collector.delete_book_from_favorites('Убийство в ночном экспрессе')
        favorites_after = collector.favorites
        assert 'Убийство в ночном экспрессе' not in favorites_after
        assert len(favorites_after) == 0


    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в ночном экспрессе')
        collector.set_book_genre('Убийство в ночном экспрессе', 'Детектив')
        collector.add_book_in_favorites('Убийство в ночном экспрессе')
        favorites_list = collector.get_list_of_favorites_books()
        assert 'Убийство в ночном экспрессе' in favorites_list
        assert len(favorites_list) == 1
