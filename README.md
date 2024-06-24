# Book Library
![Crates.io](https://img.shields.io/badge/Python-PyTest-yellow)
# General info
##### Create a database using SQLite. Write automated tests using pytest to test various database operations, including fixtures for preparing data and performing various testing steps.
# Links
##### Source where I got the information.
* [Source 1](https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-22-osnovy-raboty-s-sqlite-2023-06-15) (Instructions for connecting SQLite)
* [Source 2](https://ru.stackoverflow.com/questions/1193493/Как-достать-из-базы-данных-sqlite3-определённое-значение-по-id-в-python)
# Setup
Installing the PyTest library, type command:
```sh
pip install pytest
```
# Tests
#### Positive Tests:
* [ test_add_book ]
* [ test_get_list_all_books ]
* [ test_get_info_book_by_id ]
* [ test_update_info_book_by_id ]
* [ test_delete_book_by_id ]
#### Negative Tests:
* [ test_get_not_exist_book ]
#### To run tests:
From /task_book_library/tests/, type command:
```sh
pytest
```
