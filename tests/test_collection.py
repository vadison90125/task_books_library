from helpers.database_helpers import Database
from conftest import db
import random


class TestCollection:

    def test_add_book(self, db):
        database = Database()
        database.add_book('Title_4', 'Author_4', 2000)
        assert len(database.get_list_all_books()) == 4

    def test_get_list_all_books(self, db):
        database = Database()
        list_books = database.get_list_all_books()
        assert list_books == [(1, 'Title_1', 'Author_1', 1999),
                              (2, 'Title_2', 'Author_2', 2000),
                              (3, 'Title_3', 'Author_3', 2010)]

    def test_get_info_book_by_id(self, db):
        database = Database()
        number_id = random.randint(1, 4)
        info_books = database.get_info_book_by_id(number_id)
        if number_id == 1:
            assert info_books == ('Title_1', 'Author_1', 1999)
        if number_id == 2:
            assert info_books == ('Title_2', 'Author_2', 2000)
        if number_id == 3:
            assert info_books == ('Title_3', 'Author_3', 2010)

    def test_update_info_book_by_id(self, db):
        database = Database()
        database.update_info_book_by_id(3)
        info_book = database.get_info_book_by_id(3)
        assert info_book == ('Title_4', 'Author_3', 2010)

    def test_delete_book_by_id(self, db):
        database = Database()
        database.delete_book_by_id(2)
        info_book = database.get_info_book_by_id(2)
        assert info_book is None

    def test_get_not_exist_book(self, db):
        database = Database()
        result = database.get_book_by_title('Title_4')
        assert result is None
