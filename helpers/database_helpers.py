import sqlite3
import os


class Database:

    def __init__(self):
        self.db = '../database/books_library.db'
        with sqlite3.connect(self.db) as connect:
            self.connect = connect
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)''')
        self.connect.commit()

    def delete_db(self):
        self.connect.close()
        os.remove(self.db)

    def add_book(self, title, author, year):
        self.cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
                            (title, author, year))
        self.connect.commit()

    def get_list_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        results = self.cursor.fetchall()
        self.connect.close()
        return results

    def get_info_book_by_id(self, book_id):
        self.cursor.execute("SELECT title, author, year FROM books WHERE id == ?",
                            (book_id,))
        result = self.cursor.fetchone()
        self.connect.close()
        return result

    def update_info_book_by_id(self, book_id):
        self.cursor.execute("UPDATE books SET title = ? WHERE id == ?",
                            ('Title_4', book_id))
        self.connect.commit()

    def delete_book_by_id(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id == ?",
                            (book_id,))
        self.connect.commit()

    def get_book(self, title):
        self.cursor.execute("SELECT * FROM books WHERE title == ?",
                            (title,))
        results = self.cursor.fetchone()
        self.connect.close()
        return results
