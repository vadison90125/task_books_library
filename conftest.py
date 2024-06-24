from helpers.database_helpers import Database
import random
import pytest
import os


@pytest.fixture(scope='function')
def db():
    if not os.path.exists('../database'):
        os.makedirs('../database')
    database = Database()
    database.create_table()
    # for i in range(1, 4):
    #     random_year = random.randint(1990, 2010)
    #     database.add_book(f'Title_{i}', f'Author_{i}', random_year)
    database.add_book(f'Title_1', f'Author_1', 1999)
    database.add_book(f'Title_2', f'Author_2', 2000)
    database.add_book(f'Title_3', f'Author_3', 2010)
    yield None
    database.delete_db()
